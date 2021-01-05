import os
import re

from qtpy import uic
from qtpy.QtCore import Slot, Signal
from qtpy.QtWidgets import QWidget, QWidgetItem, QAbstractButton
from qtpyvcp.actions.program_actions import load as loadProgram
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.info import Info
from qtpyvcp import hal
from widgets.probe_param_input import ProbeParamInputWidget
from enum import IntEnum
from statemachine import StateMachine, State

LOG = logger.getLogger(__name__)
INFO = Info()
SUBROUTINE_SEARCH_DIRS = INFO.getSubroutineSearchDirs()
PROGRAM_PREFIX = INFO.getProgramPrefix()
UI_FILE = os.path.join(os.path.dirname(__file__), "probe_wizard_widget.ui")
MAX_NUMBER_OF_PARAMS = 30

# input: #<input_param_name> = #1 (=0.125 comment)
# result: [("input_param_name", "1", "0.125", "comment")]
# if a group is not present it will be an empty string
PARSE_POSITIONAL_ARGS = re.compile(r' *# *<(input_[a-z0-9_-]+)> *= *#([0-9]+) *(?:\(= *([0-9.+-]+[0-9.]*?|) *(.*)\))?', re.I)

class WizardPage(IntEnum):
    LOAD_PROBE_TOOL = 0
    TRIP_PROBE_TIP = 1
    SELECT_PROBE_OPERATION = 2
    ENTER_PARAMETERS = 3
    SHOW_PROBE_RESULTS = 4


class ProbeWizardStateMachine(StateMachine):
    startWizard = State('StartWizard', initial=True)
    loadProbeTool = State('LoadProbeTool')
    tipProbeTip = State('TipProbeTip')
    selectProbeOperation = State('SelectProbeOperation')
    enterProbingParameters = State('EnterProbingParameters')
    # showProbingResults = State('ShowProbingResults')

    start_wizard = startWizard.to(loadProbeTool)
    probe_plugged = loadProbeTool.to(tipProbeTip)
    probe_tripped = tipProbeTip.to(selectProbeOperation)
    probe_routine_selected = selectProbeOperation.to(enterProbingParameters)

    def on_enter_loadProbeTool(self):
        LOG.debug('-----Entered LoadProbeTool')

    def on_enter_tipProbeTip(self):
        LOG.debug('-----Entered tipProbeTip')

    def on_enter_selectProbeOperation(self):
        LOG.debug('-----Entered selectProbeOperation')

class ProbeWizardWidget(QWidget):
    probingFinished = Signal(object)
    probingCodeReady = Signal(object)

    def __init__(self, parent=None):
        super(ProbeWizardWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)

        self.probeButtonGroup.buttonClicked.connect(self.handleProbeRoutineSelected)
        self.buttonChangeRoutine.clicked.connect(self.changeRoutine)
        self.buttonGenerateCode.clicked.connect(self.generateCode)
        self.buttonChangeParams.clicked.connect(self.changeParams)

        comp = hal.component('probewizard')
        comp.addPin('probe-plugged', 'bit', 'in')
        comp.addPin('probe-tripped', 'bit', 'in')
        comp.addListener('probe-plugged', self.onProbePlugged)
        comp.addListener('probe-tripped', self.onProbeTripped)
        comp.ready()

        self.stackedWidget.setCurrentIndex(WizardPage.LOAD_PROBE_TOOL)

        self.wizard_machine = ProbeWizardStateMachine(self)
        self.wizard_machine.start_wizard()

    def onProbePlugged(self, probePlugged):
        if probePlugged:
            self.wizard_machine.probe_plugged()
            self.stackedWidget.setCurrentIndex(WizardPage.TRIP_PROBE_TIP)
        else:
            self.stackedWidget.setCurrentIndex(WizardPage.LOAD_PROBE_TOOL)

    def onProbeTripped(self, probeTripped):
        if probeTripped:
            self.wizard_machine.probe_tripped()
            self.stackedWidget.setCurrentIndex(WizardPage.SELECT_PROBE_OPERATION)
        else:
            self.stackedWidget.setCurrentIndex(WizardPage.LOAD_PROBE_TOOL)

    @Slot(QAbstractButton)
    def on_probeTabsGroup_buttonClicked(self, button):
        self.probingCyclesStackedWidget.setCurrentIndex(button.property('page'))

    def handleProbeRoutineSelected(self, button):
        self._routineName = str(button.filename)
        if self._routineName != "":
            self.stackedWidget.setCurrentIndex(WizardPage.ENTER_PARAMETERS) # routineSelected, enter the parameters
            self.labelSelectedRoutine.setText(self._routineName)

            subfile = None
            for dir in SUBROUTINE_SEARCH_DIRS:
                subfile = os.path.join(dir, self._routineName)
                if os.path.isfile(subfile):
                    break

            if subfile is None:
                LOG.error('Subroutine file could not be found: yellow<{}>'.format(self._routineName))
                return False

            with open(subfile, 'r') as fh:
                lines = fh.readlines()

            # input_index = 0
            self._args = [] * MAX_NUMBER_OF_PARAMS
            for line in lines:
                line = line.strip()
                if not line.startswith('#'):
                    continue

                # input_elements contains a string like the following in the splitted form:
                # <input_param_name> = #1 (=0.125 comment)
                input_elements = PARSE_POSITIONAL_ARGS.findall(line)
                if len(input_elements) == 0:
                    continue

                param_name, param_number, default_val, comment = input_elements[0]
                # store them for later
                # self._args[input_index] = input_elements[0]
                self._args.append(input_elements[0])
                self.renderInput(param_name)
                # input_index += 1
                # finished adding all inputs
            self.verticalLayout.addStretch()
            # load detailed image of routine

    def changeRoutine(self):
        self.stackedWidget.setCurrentIndex(WizardPage.SELECT_PROBE_OPERATION) # available routines page
        self._routineName = ""
        self.removeDynamicInputs()

    def showProbingResults(self):
        self.probingFinished.emit(self)
        self.stackedWidget.setCurrentIndex(WizardPage.SHOW_PROBE_RESULTS)

    def changeParams(self):
        self.stackedWidget.setCurrentIndex(WizardPage.ENTER_PARAMETERS)

    def generateCode(self):
        LOG.debug('generateCode')
        items = (self.verticalLayout.itemAt(i) for i in range(self.verticalLayout.count()))
        sub_args = [] * MAX_NUMBER_OF_PARAMS
        input_index = 0
        for anInput in items:
            if isinstance(anInput, QWidgetItem):
                entered_value = anInput.widget().get_inputValue()
                LOG.debug('Entered value: <{}>'.format(entered_value))

                param_name, param_number, default_val, comment = self._args[input_index]
                input_index +=1

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

                sub_args[index] = "[{}]".format(val)

        arg_str = ' '.join(sub_args)
        sub_name = os.path.splitext(self._routineName)[0]
        program_text = "(Call the probing subroutine with user's entered values)\n" \
                      "o<{}> call {}\nM2".format(sub_name, arg_str)

        new_file_path = os.path.join(PROGRAM_PREFIX, "with_vals_" + self._routineName)
        LOG.debug('Writting output file: <%s>', new_file_path)
        outputFile = open(new_file_path, "w")
        outputFile.write(program_text)
        outputFile.close()
        loadProgram(new_file_path)
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
        probeparaminputwidget = ProbeParamInputWidget(self.verticalLayoutWidget, param_name)
        probeparaminputwidget.setObjectName("child_"+param_name)
        self.verticalLayout.addWidget(probeparaminputwidget)

    def displayXMinus(self, value):
        self.showProbingResults()
        self.x_minus_probed_position.setText(str(value))

    def displayXPlus(self, value):
        self.showProbingResults()
        self.x_plus_probed_position.setText(str(value))

    def displayXCenter(self, value):
        self.showProbingResults()
        self.x_center_probed_position.setText(str(value))

    def displayXWidth(self, value):
        self.showProbingResults()
        self.x_probed_width.setText(str(value))


    def displayYMinus(self, value):
        self.showProbingResults()
        self.y_minus_probed_position.setText(str(value))

    def displayYPlus(self, value):
        self.showProbingResults()
        self.y_plus_probed_position.setText(str(value))

    def displayYCenter(self, value):
        self.showProbingResults()
        self.y_center_probed_position.setText(str(value))

    def displayYWidth(self, value):
        self.showProbingResults()
        self.y_probed_width.setText(str(value))

    def displayZMinus(self, value):
        self.showProbingResults()
        self.z_minus_probed_position.setText(str(value))

    def displayProbedDiameter(self, value):
        self.showProbingResults()
        self.probed_diameter.setText(str(value))

    def displayEdgeDelta(self, value):
        self.showProbingResults()
        self.edge_delta.setText(str(value))

    def displayEdgeAngle(self, value):
        self.showProbingResults()
        self.edge_angle.setText(str(value))