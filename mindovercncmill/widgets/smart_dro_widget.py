import os

from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
from enum import IntEnum
import linuxcnc

CMD = linuxcnc.command()
UI_FILE = os.path.join(os.path.dirname(__file__), "smart_dro.ui")


class DynamicHeader(IntEnum):
    INTERPRETER_OFF = 0
    INTERPRETER_ON = 1


class DynamicX(IntEnum):
    INTERPRETER_OFF = 0
    INTERPRETER_ON = 1


class DynamicY(IntEnum):
    INTERPRETER_OFF = 1
    INTERPRETER_ON = 0


class DynamicZ(IntEnum):
    INTERPRETER_OFF = 1
    INTERPRETER_ON = 0


class DynamicA(IntEnum):
    INTERPRETER_OFF = 1
    INTERPRETER_ON = 0


class SmartDro(QWidget):
    def __init__(self, parent=None):
        super(SmartDro, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self.STATUS = getPlugin('status')

        self.STATUS.interp_state.notify(self.__update_ui)

    def __update_ui(self, interpreter_state):
        if interpreter_state == linuxcnc.INTERP_IDLE:
            self.dynamicHeader.setCurrentIndex(DynamicHeader.INTERPRETER_OFF)
            self.dynamicX.setCurrentIndex(DynamicX.INTERPRETER_OFF)
            self.dynamicY.setCurrentIndex(DynamicY.INTERPRETER_OFF)
            self.dynamicZ.setCurrentIndex(DynamicZ.INTERPRETER_OFF)
            self.dynamicA.setCurrentIndex(DynamicA.INTERPRETER_OFF)
        else:
            self.dynamicHeader.setCurrentIndex(DynamicHeader.INTERPRETER_ON)
            self.dynamicX.setCurrentIndex(DynamicX.INTERPRETER_ON)
            self.dynamicY.setCurrentIndex(DynamicY.INTERPRETER_ON)
            self.dynamicZ.setCurrentIndex(DynamicZ.INTERPRETER_ON)
            self.dynamicA.setCurrentIndex(DynamicA.INTERPRETER_ON)
