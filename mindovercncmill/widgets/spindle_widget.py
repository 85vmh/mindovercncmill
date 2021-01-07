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

CMD = linuxcnc.command()
UI_FILE = os.path.join(os.path.dirname(__file__), "spindle_widget.ui")

class SpindleState(IntEnum):
    PROBE_IN_SPINDLE = 0
    SPINDLE_LOADED = 1
    SPINDLE_RUNNING = 2
    SPINDLE_EMPTY = 3

class SpindleWidget(QWidget):
    def __init__(self, parent=None):
        super(SpindleWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self.STATUS = getPlugin('status')

        self._probe_plugged = False
        self._probe_tripped = False

        self.changeToolBtn.clicked.connect(self.changeTool)
        self.loadToolBtn.clicked.connect(self.loadTool)
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
        else:
            LOG.debug('-----SPINDLE_Running called')
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_RUNNING)

    def changeTool(self):
        self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_EMPTY)
        self.toolNumberInput.setFocus()

    def loadTool(self):
        if int(self.toolNumberInput.text()) != self._loadedTool:
            #proceed with tool change
            issue_mdi("M6 T{} G43".format(self.toolNumberInput.text()))
        elif self._loadedTool == 0:
            pass
        else:
            self.spindleStates.setCurrentIndex(SpindleState.SPINDLE_LOADED)

    def spindleForward(self):
        CMD.spindle(linuxcnc.SPINDLE_FORWARD, int(self.spindleSpeed.text()), 0)

    def spindleReverse(self):
        CMD.spindle(linuxcnc.SPINDLE_REVERSE, int(self.spindleSpeed.text()), 0)