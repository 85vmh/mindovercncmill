import os

from qtpyvcp.plugins import getPlugin

from mindovercncmill.widgets.input_overlay import InputOverlay

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/facing_op.ui")
STATUS = getPlugin('status')


class FacingOpOverlay(InputOverlay):
    def __init__(self, facingOperation, parent=None):
        super(FacingOpOverlay, self).__init__(UI_FILE, parent)
        self._facingOperation = facingOperation
        self.dialog.generalparamswidget.programOperation = facingOperation

        self.dialog.step_down_input.editingFinished.connect(self._validate_step_down)
        self.dialog.step_over_input.editingFinished.connect(self._validate_step_over)
        self.dialog.x_start_input.editingFinished.connect(self._validate_x_positions)
        self.dialog.x_end_input.editingFinished.connect(self._validate_x_positions)
        self.dialog.y_start_input.editingFinished.connect(self._validate_y_positions)
        self.dialog.y_end_input.editingFinished.connect(self._validate_y_positions)
        self.dialog.z_start_input.editingFinished.connect(self._validate_z_heights)
        self.dialog.z_end_input.editingFinished.connect(self._validate_z_heights)
        self.dialog.retract_height_input.editingFinished.connect(self._validate_retract_height)

        self._validators = [self._validate_step_down,
                            self._validate_step_over,
                            self._validate_x_positions,
                            self._validate_y_positions]

        # self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDoneEditing.clicked.connect(self.handleDoneClicked)

    def handleDoneClicked(self):
        self.dialog.generalparamswidget.populateWithValues(self._facingOperation)
        self._facingOperation.x_start = self.x_start()
        self._facingOperation.x_end = self.x_end()
        self._facingOperation.y_start = self.y_start()
        self._facingOperation.y_end = self.x_end()
        self._facingOperation.step_over = self.step_over()
        self._facingOperation.z_start = self.z_start()
        self._facingOperation.z_end = self.z_end()
        self._facingOperation.step_down = self.step_down()
        self._facingOperation.retract = self.retract_height()
        self.hide()

    def step_over(self):
        return self.dialog.step_over_input.value()

    def step_down(self):
        return self.dialog.step_down_input.value()

    def x_start(self):
        return self.dialog.x_start_input.value()

    def x_end(self):
        return self.dialog.x_end_input.value()

    def y_start(self):
        return self.dialog.y_start_input.value()

    def y_end(self):
        return self.dialog.y_end_input.value()

    def z_start(self):
        return self.dialog.z_start_input.value()

    def z_end(self):
        return self.dialog.z_end_input.value()

    def retract_height(self):
        return self.dialog.retract_height_input.value()

    def _validate_step_over(self):
        if self.step_over() < 0:
            self.dialog.step_over_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Step over cannot be negative.'
            self.dialog.step_over_input.setToolTip(error)
            return False, error
        else:
            self.dialog.step_over_input.setStyleSheet('')
            return True, None

    def _validate_step_down(self):
        if self.step_down() < 0:
            self.dialog.step_down_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Step down cannot be negative.'
            self.dialog.step_down_input.setToolTip(error)
            return False, error
        else:
            self.dialog.step_down_input.setStyleSheet('')
            return True, None

    def _validate_x_positions(self):
        if self.x_start() < self.x_end():
            self.dialog.x_start_input.setStyleSheet('')
            self.dialog.x_end_input.setStyleSheet('')
            return True, None
        else:
            self.dialog.x_start_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            self.dialog.x_end_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'X start position must be less than end position.'
            self.dialog.x_start_input.setToolTip(error)
            self.dialog.x_end_input.setToolTip(error)
            return False, error

    def _validate_y_positions(self):
        if self.y_start() > self.y_end():
            self.dialog.y_start_input.setStyleSheet('')
            self.dialog.y_end_input.setStyleSheet('')
            return True, None
        else:
            self.dialog.y_start_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            self.dialog.y_end_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Y start position must be greater than end position.'
            self.dialog.y_start_input.setToolTip(error)
            self.dialog.y_end_input.setToolTip(error)
            return False, error

    def _validate_z_heights(self):
        if not self.z_start() > self.z_end():
            self.dialog.z_start_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            self.dialog.z_end_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            error = 'Z start position must be greater than end position.'
            self.dialog.z_end_input.setToolTip(error)
            return False, error
        else:
            self.dialog.z_start_input.setStyleSheet('')
            self.dialog.z_end_input.setStyleSheet('')
            return True, None

    def _validate_retract_height(self):
        if self.retract_height() >= 0:
            self.dialog.retract_height_input.setStyleSheet('')
            return True, None
        else:
            self.dialog.retract_height_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Retract height must be 0 or greater.'
            self.dialog.retract_height_input.setToolTip(error)
            return False, error

