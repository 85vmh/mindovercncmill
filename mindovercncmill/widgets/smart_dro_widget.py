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

class DynamicAxis(IntEnum):
    STATUS = 0
    MANUAL = 1
    RUNNING = 2

class HomedState(IntEnum):
    UNHOMED = 0
    HOMED_OR_HOMING = 1

class SmartDro(QWidget):
    def __init__(self, parent=None):
        super(SmartDro, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self.status = getPlugin('status')

        self.status.interp_state.notify(self.__update_ui)
        self.status.all_axes_homed.notify(self.__set_state)
        self.status.homed.notify(self.__set_state)
        self.__set_state()

    def __set_state(self):
        homed = self.status.all_axes_homed.getValue()
        homed_per_axis = self.status.homed.getValue()

        if not homed:
            LOG.debug("----not homed per axis: {}".format(homed_per_axis))
            if homed_per_axis[0] == 0 and homed_per_axis[1] == 0 and homed_per_axis[2] == 0:
                self.stackedWidget.setCurrentIndex(HomedState.UNHOMED)
            else:
                LOG.debug("----homing: {}".format(homed_per_axis))
                self.stackedWidget.setCurrentIndex(HomedState.HOMED_OR_HOMING)
                if homed_per_axis[0] == 0 or homed_per_axis[1] == 0 or homed_per_axis[2] == 0:
                    LOG.debug("----set status: {}".format(homed_per_axis))
                    self.dynamicHeader.setCurrentIndex(DynamicAxis.STATUS)
                    self.dynamicX.setCurrentIndex(DynamicAxis.STATUS)
                    self.dynamicY.setCurrentIndex(DynamicAxis.STATUS)
                    self.dynamicZ.setCurrentIndex(DynamicAxis.STATUS)
                    self.dynamicA.setCurrentIndex(DynamicAxis.STATUS)
                    self.x_axis_status.setText('Homing...' if homed_per_axis[0] == 0 else 'Homed')
                    self.y_axis_status.setText('Homing...' if homed_per_axis[1] == 0 else 'Homed')
                    self.z_axis_status.setText('Homing...' if homed_per_axis[2] == 0 else 'Homed')
                    self.a_axis_status.setText('Homing...' if homed_per_axis[3] == 0 else 'Homed')
        else:
            LOG.debug("----homed or homing")
            self.stackedWidget.setCurrentIndex(HomedState.HOMED_OR_HOMING)
            self.__update_ui(self.status.interp_state.getValue())

    def __update_ui(self, interpreter_state):
        LOG.debug("----update ui - all axes homed: {}".format(self.status.all_axes_homed.getValue()))
        if self.status.all_axes_homed.getValue() == True:
            selectedIndex = DynamicAxis.MANUAL if interpreter_state == linuxcnc.INTERP_IDLE else DynamicAxis.RUNNING
            self.dynamicHeader.setCurrentIndex(selectedIndex)
            self.dynamicX.setCurrentIndex(selectedIndex)
            self.dynamicY.setCurrentIndex(selectedIndex)
            self.dynamicZ.setCurrentIndex(selectedIndex)
            self.dynamicA.setCurrentIndex(selectedIndex)
