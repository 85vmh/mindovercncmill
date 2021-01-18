import os
from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import Property, Slot
from qtpyvcp.utilities.settings import getSetting, connectSetting
from qtpyvcp.utilities import logger
from qtpyvcp.actions.machine_actions import issue_mdi
from qtpyvcp.plugins import getPlugin

LOG = logger.getLogger(__name__)
from enum import IntEnum
import linuxcnc
from qtpyvcp import hal
from qtpy.QtCore import Slot, Signal
from qtpyvcp.widgets import HALWidget

CMD = linuxcnc.command()
UI_FILE = os.path.join(os.path.dirname(__file__), "spindle_widget.ui")


class SpindleState(IntEnum):
    SPINDLE_EMPTY = 0
    PREPARING_TOOL_CHANGE = 1
    CONFIRM_TOOL_CHANGE = 2
    PROBE_IN_SPINDLE = 3
    SPINDLE_LOADED = 4
    SPINDLE_RUNNING = 5


class SpindleWidget(QWidget, HALWidget):
    measureTool = Signal(bool)

    def initialize(self):
        comp = hal.getComponent()
        self._tool_change_confirmed = comp.addPin("tool-change-confirmed", "bit", "io")
        self._tool_change_confirm = comp.addPin("tool-change-confirm", "bit", "in")
        self._tool_change_prep_number = comp.addPin("tool-change-prep-number", "s32", "in")
        self._tool_change_confirm.valueChanged.connect(self.readyToConfirm)
        self._tool_change_prep_number.valueChanged.connect(self.preparingToLoadTool)

    def __init__(self, parent=None):
        super(SpindleWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self.STATUS = getPlugin('status')
        self._probe_plugged = False
        self._probe_tripped = False
        self._loadedTool = 0

        self._tool_change_confirmed = None
        self._tool_change_confirm = None
        self._tool_change_prep_number = None

        self.loadToolBtn.clicked.connect(self.loadTool)
        self.confirmToolChangeBtn.clicked.connect(self.confirmToolChange)
        self.measureToolBtn.clicked.connect(self.confirmToolChangeAndMeasure)
        self.changeToolBtn.clicked.connect(self.changeTool)
        self.spindleRevBtn.clicked.connect(self.spindleReverse)
        self.spindleFwdBtn.clicked.connect(self.spindleForward)

        self.STATUS.spindle[0].speed.notify(self.determineSpindleState)
        self.STATUS.tool_in_spindle.notify(self.determineSpindleState)
        self.determineSpindleState()

    @Slot(bool)
    def set_probe_plugged(self, plugged):
        self._probe_plugged = plugged
        if plugged:
            self.spindleStates.setCurrentIndex(SpindleState.PROBE_IN_SPINDLE)
        else:
            self.determineSpindleState()

    @Slot(bool)
    def set_probe_tripped(self, tripped):
        self._probe_tripped = tripped
        if (self._probe_plugged & tripped):
            # do smth to reflect the tripping
            pass

    def determineSpindleState(self):
        LOG.debug('-----determineState called')

        spindleSpeed = self.STATUS.spindle[0].speed.getValue()
        self._loadedTool = self.STATUS.tool_in_spindle.getValue()

        if self._loadedTool == 0:
            LOG.debug('-----SPINDLE_EMPTY called')
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_EMPTY)
        elif spindleSpeed == 0.0:
            LOG.debug('-----SPINDLE_LOADED called')
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_LOADED)
            self.spindleSpeed.setFocus()
        else:
            LOG.debug('-----SPINDLE_Running called')
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_RUNNING)

    def changeTool(self):
        self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_EMPTY)
        self.toolNumberInput.setFocus()

    def loadTool(self):
        if int(self.toolNumberInput.text()) != self._loadedTool:
            # proceed with tool change
            issue_mdi("M6 T{} G43".format(self.toolNumberInput.text()))
        elif self._loadedTool == 0:
            pass
        else:
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_LOADED)
            self.spindleSpeed.setFocus()

    def spindleForward(self):
        CMD.spindle(linuxcnc.SPINDLE_FORWARD, int(self.spindleSpeed.text()), 0)

    def spindleReverse(self):
        CMD.spindle(linuxcnc.SPINDLE_REVERSE, int(self.spindleSpeed.text()), 0)

    def confirmToolChange(self):
        self._tool_change_confirmed.value = True

    def confirmToolChangeAndMeasure(self):
        self.measureTool.emit(True)
        self._tool_change_confirmed.value = True

    def preparingToLoadTool(self, tool_number):
        if tool_number != 0:
            self.spindleStates.setCurrentIndex(SpindleState.PREPARING_TOOL_CHANGE)
            self.prepareMessageLabel.setText(
                "Preparing to load T" + str(tool_number) + "...\nMoving to change position...")
        else:
            LOG.debug('-----Prepare tool no become 0')

    def readyToConfirm(self, value):
        if value:
            self.spindleStates.setCurrentIndex(SpindleState.CONFIRM_TOOL_CHANGE)
            self.confirmMessageLabel.setText(
                "Insert T" + str(self._tool_change_prep_number.value) + " in the spindle,\nthen Confirm")
        else:
            self._tool_change_confirmed.value = False
