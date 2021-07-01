import os
from mindovercncmill.widgets.input_overlay import InputOverlay
from dataclass.holes_operation import *
from qtpy.QtCore import Signal
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/hole_op.ui")


class HoleOpOverlay(InputOverlay):
    holeOperationChanged = Signal(object)

    def __init__(self, holeOp, parent=None):
        super(HoleOpOverlay, self).__init__(UI_FILE, parent)

        self._holeOperation = holeOp

        self.dialog.generalparamswidget.programOperation = holeOp

        self.populateInitialValues(self._holeOperation)

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDoneEditing.clicked.connect(self.handleDoneClicked)

    def populateInitialValues(self, _holeOperation):
        if isinstance(_holeOperation, DwellOperation):
            self.dialog.dialog_title.setText("Dwell Drilling")
            self.dialog.custom_input_label.setText("Dwell Time:")
            self.dialog.custom_field_input.setText(str(_holeOperation.dwell_time))
            self.dialog.custom_field_unit.setText("seconds")
        elif isinstance(_holeOperation, PeckOperation):
            self.dialog.dialog_title.setText("Peck Drilling")
            self.dialog.custom_input_label.setText("Peck Depth:")
            self.dialog.custom_field_input.setText(str(_holeOperation.peck_depth))
            self.dialog.custom_field_unit.setText("mm")
        elif isinstance(_holeOperation, ChipBreakingOperation):
            self.dialog.dialog_title.setText("Chip Break Drilling")
            self.dialog.custom_input_label.setText("Break Dist:")
            self.dialog.custom_field_input.setText(str(_holeOperation.break_dist))
            self.dialog.custom_field_unit.setText("mm")
        elif isinstance(_holeOperation, RigidTappingOperation):
            self.dialog.dialog_title.setText("Rigid Tapping")
            self.dialog.custom_input_label.setText("Thread Pitch:")
            self.dialog.custom_field_input.setText(str(_holeOperation.pitch))
            self.dialog.custom_field_unit.setText("mm")

        self.dialog.z_start_input.setText(str(_holeOperation.z_start))
        self.dialog.z_end_input.setText(str(_holeOperation.z_end))
        self.dialog.z_feed_input.setText(str(_holeOperation.z_feed))
        self.dialog.retract_height_input.setText(str(_holeOperation.retract))

    def handleDoneClicked(self):
        self.dialog.generalparamswidget.populateWithValues(self._holeOperation)
        if isinstance(self._holeOperation, DwellOperation):
            self._holeOperation.dwell_time = self.custom_field()
        elif isinstance(self._holeOperation, PeckOperation):
            self._holeOperation.peck_depth = self.custom_field()
        elif isinstance(self._holeOperation, ChipBreakingOperation):
            self._holeOperation.break_dist = self.custom_field()
        elif isinstance(self._holeOperation, RigidTappingOperation):
            self._holeOperation.pitch = self.custom_field()

        self._holeOperation.z_start = self.z_start()
        self._holeOperation.z_end = self.z_end()
        self._holeOperation.z_feed = self.z_feed()
        self._holeOperation.retract = self.retract_height()

        self.holeOperationChanged.emit(self._holeOperation)
        self.hide()

    def z_feed(self):
        return self.dialog.z_feed_input.value()

    def z_start(self):
        return self.dialog.z_start_input.value()

    def z_end(self):
        return self.dialog.z_end_input.value()

    def retract_height(self):
        return self.dialog.retract_height_input.value()

    def custom_field(self):
        return self.dialog.custom_field_input.value()
