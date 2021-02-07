from base_widget import ConversationalBaseWidget
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

class GeneralParamsWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(GeneralParamsWidget, self).__init__(parent, "general_params.ui")

        self._tool_is_valid = False
        self._tool_table = self.tooltable.getToolTable()

        self._validators = [self._validate_spindle_rpm,
                            self._validate_xy_feed_rate,
                            self._validate_z_feed_rate,
                            self._validate_tool_number]

        self.coolant_input.addItem('OFF')
        self.coolant_input.addItem('MIST')
        self.coolant_input.addItem('FLOOD')

        self.spindle_direction_input.addItem('CW')
        self.spindle_direction_input.addItem('CCW')

        self.xy_feed_rate_input.setText('{0:.3f}'.format(self.default_linear_velocity))
        self.spindle_rpm_input.setText('{0:.3f}'.format(self.default_spindle_speed))

        self.tool_number_input.editingFinished.connect(self.set_tool_description_from_tool_num)
        self.tool_number_input.editingFinished.connect(self._validate_tool_number)

        self.spindle_rpm_input.editingFinished.connect(self._validate_spindle_rpm)
        self.xy_feed_rate_input.editingFinished.connect(self._validate_xy_feed_rate)
        self.z_feed_rate_input.editingFinished.connect(self._validate_z_feed_rate)

    def set_tool_description_from_tool_num(self):
        tool_table = self._tool_table
        tool_number = self.tool_number()
        try:
            desc = tool_table[tool_number]['R']
            self.tool_description.setText((desc[:30] + '...') if len(desc) > 30 else desc)
            self.tool_description.setToolTip(desc)
            self._tool_is_valid = (tool_number > 0)
        except KeyError:
            self._tool_is_valid = False
            self.tool_description.setText('TOOL NOT IN TOOL TABLE')
            self.tool_description.setToolTip('TOOL NOT IN TOOL TABLE')

    def tool_number(self):
        return self.tool_number_input.value()

    def tool_diameter(self):
        if self._tool_is_valid:
            return self._tool_table[self.tool_number()]['D']
        else:
            return 0.

    def spindle_rpm(self):
        return self.spindle_rpm_input.value()

    def spindle_direction(self):
        return self.spindle_direction_input.currentText()

    def coolant(self):
        return self.coolant_input.currentText()

    def xy_feed_rate(self):
        return self.xy_feed_rate_input.value()

    def z_feed_rate(self):
        return self.z_feed_rate_input.value()

    def clearance_height(self):
        return self.clearance_height_input.value()

    def retract_height(self):
        return self.retract_height_input.value()

    def z_start(self):
        return self.z_start_input.value()

    def z_end(self):
        return self.z_end_input.value()


    def _validate_spindle_rpm(self):
        if self.spindle_rpm() > 0:
            self.spindle_rpm_input.setStyleSheet('')
            return True, None
        else:
            self.spindle_rpm_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Spindle RPM must be greater than 0.'
            self.spindle_rpm_input.setToolTip(error)
            return False, error

    def _validate_xy_feed_rate(self):
        if self.xy_feed_rate() > 0:
            self.xy_feed_rate_input.setStyleSheet('')
            return True, None
        else:
            self.xy_feed_rate_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'XY feed rate must be greater than 0.'
            self.xy_feed_rate_input.setToolTip(error)
            return False, error

    def _validate_z_feed_rate(self):
        if self.z_feed_rate() > 0:
            self.z_feed_rate_input.setStyleSheet('')
            return True, None
        else:
            self.z_feed_rate_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Z feed rate must be greater than 0.'
            self.z_feed_rate_input.setToolTip(error)
            return False, error

    def _validate_tool_number(self):
        if self._tool_is_valid:
            self.tool_number_input.setStyleSheet('')
            return True, None
        else:
            self.tool_number_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Tool is not valid.'
            self.tool_number_input.setToolTip(error)
            return False, error


