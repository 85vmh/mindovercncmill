import os
import re

from qtpy import uic
from qtpy.QtCore import Slot, Signal
from qtpy.QtWidgets import QWidget, QWidgetItem
from qtpyvcp.actions.program_actions import load as loadProgram

from qtpyvcp.utilities.info import Info
from probe_param_input import ProbeParamInputWidget
from probe_push_button import ProbePushButton
from enum import IntEnum
from qtpy.QtWidgets import qApp

# from statemachine import StateMachine, State

from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
INFO = Info()
SUBROUTINE_SEARCH_DIRS = INFO.getSubroutineSearchDirs()
PROGRAM_PREFIX = INFO.getProgramPrefix()
UI_FILE = os.path.join(os.path.dirname(__file__), "probe_wizard_widget.ui")
MAX_NUMBER_OF_PARAMS = 30
PROBE_MODE_PARAM_NAME = "setting_probe_mode"

# input: #<input_param_name> = #1 (=0.125 comment)
# result: [("input_param_name", "1", "0.125", "comment")]
# if a group is not present it will be an empty string
PARSE_SETTING_ARGS = re.compile(r' *# *<(setting_[a-z0-9_-]+)> *= *#([0-9]+) *(?:\(= *([0-9.+-]+[0-9.]*?|) *(.*)\))?',
                                re.I)
PARSE_INPUT_ARGS = re.compile(r' *# *<(input_[a-z0-9_-]+)> *= *#([0-9]+) *(?:\(= *([0-9.+-]+[0-9.]*?|) *(.*)\))?', re.I)


class WizardPage(IntEnum):
    LOAD_PROBE_TOOL = 0
    TRIP_PROBE_TIP = 1
    SELECT_PROBE_OPERATION = 2
    ENTER_PARAMETERS = 3
    SHOW_PROBE_RESULTS = 4


# class ProbeWizardStateMachine(StateMachine):
#     startWizard = State('StartWizard', initial=True)
#     loadProbeTool = State('LoadProbeTool')
#     tipProbeTip = State('TipProbeTip')
#     selectProbeOperation = State('SelectProbeOperation')
#     enterProbingParameters = State('EnterProbingParameters')
#     # showProbingResults = State('ShowProbingResults')
#
#     start_wizard = startWizard.to(loadProbeTool)
#     probe_plugged = loadProbeTool.to(tipProbeTip)
#     probe_tripped = tipProbeTip.to(selectProbeOperation)
#     probe_routine_selected = selectProbeOperation.to(enterProbingParameters)
#
#     def on_enter_loadProbeTool(self):
#         LOG.debug('-----Entered LoadProbeTool')
#
#     def on_enter_tipProbeTip(self):
#         LOG.debug('-----Entered tipProbeTip')
#
#     def on_enter_selectProbeOperation(self):
#         LOG.debug('-----Entered selectProbeOperation')

def getCommentFormat():
    return " ({} : {})"


class ProbeWizardWidget(QWidget):
    probingFinished = Signal(object)
    probingCodeReady = Signal(object)

    def __init__(self, parent=None):
        super(ProbeWizardWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)

        self._setting_args = [] * MAX_NUMBER_OF_PARAMS
        self._input_args = [] * MAX_NUMBER_OF_PARAMS
        self._probe_plugged = False
        self._routineName = ""

        self.probeButtonGroup.buttonClicked.connect(self.handleProbeRoutineSelected)
        self.buttonChangeRoutine.clicked.connect(self.changeRoutine)
        self.buttonGenerateCode.clicked.connect(self.generateCode)
        self.buttonChangeParams.clicked.connect(self.changeParams)
        self.buttonResetResults.clicked.connect(self.resetResults)

        self.stackedWidget.setCurrentIndex(WizardPage.SELECT_PROBE_OPERATION)

        # self.wizard_machine = ProbeWizardStateMachine(self)
        # self.wizard_machine.start_wizard()

    @Slot(bool)
    def set_probe_plugged(self, plugged):
        LOG.error('---------set_probe_plugged: <{}>'.format(plugged))
        self._probe_plugged = plugged
        if plugged:
            # self.wizard_machine.probe_plugged()
            self.stackedWidget.setCurrentIndex(WizardPage.TRIP_PROBE_TIP)
        else:
            self.stackedWidget.setCurrentIndex(WizardPage.LOAD_PROBE_TOOL)

    @Slot(bool)
    def set_probe_tripped(self, tripped):
        LOG.error('---------set_probe_tripped: <{}>'.format(tripped))
        if self._probe_plugged and tripped:
            # self.wizard_machine.probe_tripped()
            self.stackedWidget.setCurrentIndex(WizardPage.SELECT_PROBE_OPERATION)

    def handleProbeRoutineSelected(self, button):
        self._routineName = str(button.filename)
        # re init values each time
        self._setting_args = [] * MAX_NUMBER_OF_PARAMS
        self._input_args = [] * MAX_NUMBER_OF_PARAMS

        LOG.debug('---------Select routine is: <{}>'.format(self._routineName))
        if self._routineName != "":
            self.stackedWidget.setCurrentIndex(WizardPage.ENTER_PARAMETERS)  # routineSelected, enter the parameters
            self.labelSelectedRoutine.setText(self._routineName)

            subfile = None
            LOG.debug('---------routine folder is: {}'.format(SUBROUTINE_SEARCH_DIRS))
            for dir in SUBROUTINE_SEARCH_DIRS:
                subfile = os.path.join(dir, self._routineName)
                if os.path.isfile(subfile):
                    LOG.debug('---------routine path is: {}'.format(subfile))
                    break

            if subfile is None:
                LOG.error('Subroutine file could not be found: yellow<{}>'.format(self._routineName))
                return False

            with open(subfile, 'r') as fh:
                lines = fh.readlines()

            LOG.debug('---------routine has {} lines'.format(len(lines)))

            # input_index = 0
            for line in lines:
                line = line.strip()
                if not line.startswith('#'):
                    continue

                # input_elements contains a string like the following in the split form:
                # <input_param_name> = #1 (=0.125 comment)

                setting_elements = PARSE_SETTING_ARGS.findall(line)
                LOG.debug('---------routine has {} setting_elements'.format(len(setting_elements)))
                if len(setting_elements) != 0:
                    # store them for later
                    self._setting_args.append(setting_elements[0])

                input_elements = PARSE_INPUT_ARGS.findall(line)
                LOG.debug('---------routine has {} input_elements'.format(len(input_elements)))
                if len(input_elements) != 0:
                    param_name, param_number, default_val, comment = input_elements[0]
                    # store them for later
                    self._input_args.append(input_elements[0])
                    self.renderInput(param_name)
                # finished adding all inputs
            self.verticalLayout.addStretch()
            # load detailed image of routine
        else:
            LOG.debug('---------routine name is empty')

    def changeRoutine(self):
        self.stackedWidget.setCurrentIndex(WizardPage.SELECT_PROBE_OPERATION)  # available routines page
        self._routineName = ""
        self.removeDynamicInputs()

    def showProbingResults(self):
        self.probingFinished.emit(self)
        self.stackedWidget.setCurrentIndex(WizardPage.SHOW_PROBE_RESULTS)

        has_z = self.z_minus_probed_position.text() != ""
        has_x = self.x_minus_probed_position.text() != "" or self.x_plus_probed_position.text() != ""
        has_y = self.y_minus_probed_position.text() != "" or self.y_plus_probed_position.text() != ""

        if has_z and not has_x or has_y:
            self.buttonNextAction.setText('Probe edge or corner')
            self.buttonNextAction.buttonClicked.connect(self.changeRoutine)
        else:
            self.buttonNextAction.setText('Probe top')
            fake_button = ProbePushButton(filename='probe_z_minus_wco.ngc')
            self.buttonNextAction.buttonClicked.connect(self.handleProbeRoutineSelected(fake_button))

    def changeParams(self):
        self.stackedWidget.setCurrentIndex(WizardPage.ENTER_PARAMETERS)

    def generateCode(self):
        LOG.debug('generateCode')
        sub_args = [] * MAX_NUMBER_OF_PARAMS
        param_details = [] * MAX_NUMBER_OF_PARAMS

        window = qApp.activeWindow()
        for aSetting in self._setting_args:
            param_name, param_number, default_val, comment = aSetting

            LOG.debug('-----settings param: {}'.format(param_name))

            if param_name == PROBE_MODE_PARAM_NAME:
                val = 0 if self.probe_wcs.isChecked() else 1
            else:
                try:
                    # get the value from the GUI input widget
                    val = getattr(window, param_name).text() or default_val
                except:
                    val = default_val
                    LOG.warning('No input for red<{}> parameter, using default value blue<{}>'.format(param_name, val))

            if val == '':
                LOG.error('No value given for parameter red<{}>, and no default specified'.format(param_name))
                return False

            try:
                val = float(val)
            except ValueError:
                LOG.error('Input value "{}" given for parameter "{}" is not a valid number'.format(val, param_name))
                return False

            index = int(param_number) - 1
            while len(sub_args) <= index:
                sub_args.append("[0.0000]")
                param_details.append("---")

            sub_args[index] = "[{}]".format(val)
            param_details[index] = getCommentFormat().format(param_name, val)

        input_items = (self.verticalLayout.itemAt(i) for i in range(self.verticalLayout.count()))

        input_index = 0
        for anInput in input_items:
            if isinstance(anInput, QWidgetItem):
                entered_value = anInput.widget().get_inputValue()
                LOG.debug('Entered value: <{}>'.format(entered_value))

                param_name, param_number, default_val, comment = self._input_args[input_index]
                LOG.debug('-----input param: {}'.format(param_name))
                input_index += 1

                try:
                    val = entered_value or default_val
                except:
                    val = default_val
                    LOG.warning('No input for red<{}> parameter, using default value blue<{}>'.format(param_name, val))

                if val == '':
                    LOG.error('No value given for parameter red<{}>, and no default specified'.format(param_name))
                    return False

                try:
                    val = float(val)
                except ValueError:
                    LOG.error('Input value "{}" given for parameter "{}" is not a valid number'.format(val, param_name))
                    return False

                index = int(param_number) - 1
                while len(sub_args) <= index:
                    sub_args.append("[0.0000]")
                    param_details.append("---")

                sub_args[index] = "[{}]".format(val)
                param_details[index] = getCommentFormat().format(param_name, val)

        params_list = '\n'.join(param_details)
        arg_str = ' '.join(sub_args)
        sub_name = os.path.splitext(self._routineName)[0]
        program_text = "(Call the probing subroutine with user's entered values)\n" \
                       + params_list + "\n" \
                                       "o<{}> call {}\nM2".format(sub_name, arg_str)

        new_file_path = os.path.join(PROGRAM_PREFIX, "with_vals_" + self._routineName)
        LOG.debug('Writting output file: <%s>', new_file_path)
        outputFile = open(new_file_path, "w")
        outputFile.write(program_text)
        outputFile.close()
        loadProgram(new_file_path, add_to_recents=False)
        self.probingCodeReady.emit(self)

    def removeDynamicInputs(self, L=False):
        if not L:
            L = self.verticalLayout
        if L is not None:
            while L.count():
                item = L.takeAt(0)
                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
                else:
                    self.removeDynamicInputs(item.layout())

    def renderInput(self, param_name):
        probeparaminputwidget = ProbeParamInputWidget(self, param_name)
        probeparaminputwidget.setObjectName("child_" + param_name)
        self.verticalLayout.addWidget(probeparaminputwidget)

    def displayXMinus(self, value):
        self.x_minus_probed_position.setText(str(value))
        self.showProbingResults()

    def displayXPlus(self, value):
        self.x_plus_probed_position.setText(str(value))
        self.showProbingResults()

    def displayXCenter(self, value):
        self.x_center_probed_position.setText(str(value))
        self.showProbingResults()

    def displayXWidth(self, value):
        self.x_probed_width.setText(str(value))
        self.showProbingResults()

    def displayYMinus(self, value):
        self.y_minus_probed_position.setText(str(value))
        self.showProbingResults()

    def displayYPlus(self, value):
        self.y_plus_probed_position.setText(str(value))
        self.showProbingResults()

    def displayYCenter(self, value):
        self.y_center_probed_position.setText(str(value))
        self.showProbingResults()

    def displayYWidth(self, value):
        self.y_probed_width.setText(str(value))
        self.showProbingResults()

    def displayZMinus(self, value):
        self.z_minus_probed_position.setText(str(value))
        self.showProbingResults()

    def displayDiameter(self, value):
        self.probed_diameter.setText(str(value))
        self.showProbingResults()

    def displayEdgeDelta(self, value):
        self.edge_delta.setText(str(value))
        self.showProbingResults()

    def displayEdgeAngle(self, value):
        self.edge_angle.setText(str(value))
        self.showProbingResults()

    def resetResults(self):
        self.x_minus_probed_position.setText("")
        self.x_plus_probed_position.setText("")
        self.x_center_probed_position.setText("")
        self.x_probed_width.setText("")
        self.y_minus_probed_position.setText("")
        self.y_plus_probed_position.setText("")
        self.y_center_probed_position.setText("")
        self.y_probed_width.setText("")
        self.z_minus_probed_position.setText("")
        self.probed_diameter.setText("")
        self.edge_delta.setText("")
        self.edge_angle.setText("")
