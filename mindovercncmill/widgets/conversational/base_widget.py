import os
import linuxcnc
from pyqtgraph import Qt

from qtpy import uic
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QMessageBox

from qtpyvcp.actions.program_actions import load as loadProgram
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

from qtpyvcp_conversational_gcode.ops.gcode_file import GCodeFile

LOG = logger.getLogger(__name__)

class ConversationalBaseWidget(QWidget):
    def __init__(self, parent=None, ui_file=''):
        super(ConversationalBaseWidget, self).__init__(parent)
        uic.loadUi(os.path.join(os.path.dirname(__file__), ui_file), self)

        self.status = getPlugin('status')
        self.tooltable = getPlugin('tooltable')

        self._tool_table = self.tooltable.getToolTable()
        self._ini_file = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
        self.default_spindle_speed = float(self._ini_file.find('DISPLAY', 'DEFAULT_SPINDLE_SPEED') or 0.000)
        self.default_linear_velocity = float(self._ini_file.find('DISPLAY', 'DEFAULT_LINEAR_VELOCITY') or 0.000)
        self.program_prefix = os.path.expandvars(os.path.expanduser(self._ini_file.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))

        self._validators = []

    def tool_diameter(self):
        # if self._tool_is_valid:
        #     return self._tool_table[self.tool_number()]['D']
        # else:
        #     return 0.
        return 3

    def on_post_to_file(self):
        ok, errors = self.is_valid()
        if ok:
            f = GCodeFile()
            f.ops.append(self.create_op())

            program_path = self._get_next_available_file_name()

            f.write_to_file(program_path)
            if self._confirm_action('Load GCode', 'Would you like to open the file in the viewer?'):
                loadProgram(program_path)
        else:
            self._show_error_msg('GCode Error', '\n'.join(errors))

    def is_valid(self):
        errors = []
        for f in self._validators:
            ok, error = f()
            if not ok:
                errors.append(error)

        return len(errors) == 0, errors

    # def _set_common_fields(self, op):
    #     op.wcs = self.wcs()
    #     op.coolant = self.coolant()
    #     op.units = self.unit()
    #     op.tool_number = self.tool_number()
    #     op.spindle_rpm = self.spindle_rpm()
    #     op.spindle_dir = self.spindle_direction()
    #     op.z_clear = self.clearance_height()
    #     op.xy_feed = self.xy_feed_rate()
    #     op.z_start = self.z_start()
    #     op.z_end = self.z_end()
    #     op.retract = self.retract_height()
    #     op.z_feed = self.z_feed_rate()



    def _confirm_action(self, title, message):
        msg = QMessageBox(QMessageBox.Question, title, message, QMessageBox.Yes | QMessageBox.No, self,
                          Qt.FramelessWindowHint)

        return msg.exec_() == QMessageBox.Yes

    def _show_error_msg(self, title, message):
        msg = QMessageBox(QMessageBox.Critical, title, message, QMessageBox.Ok, self,
                          Qt.FramelessWindowHint)

        msg.exec_()
