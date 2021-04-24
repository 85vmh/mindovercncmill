import os

from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
from qtpy.QtCore import Signal

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/facing_item.ui")


class FacingOpItemWidget(QWidget):
    editFacingOp = Signal(object)

    def __init__(self, facing_op=None, parent=None):
        super(FacingOpItemWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self._facing_op = facing_op

        if self._facing_op is not None:
            self.opName.setText(self._facing_op.get_operation_name())
            self.spindleSpeed.setText(str(self._facing_op.spindle_rpm))
            self.spindleDir.setText(self._facing_op.spindle_dir)
            self.coolant.setText(self._facing_op.coolant)
            self.fromZ.setText(str(self._facing_op.z_start))
            self.toZ.setText(str(self._facing_op.z_end))
            self.xyFeed.setText(str(self._facing_op.xy_feed))
            self.stepOver.setText(str(self._facing_op.step_over))

            self.btnEditOp.clicked.connect(self.handleEditClicked)

    def handleEditClicked(self):
        self.editFacingOp.emit(self._facing_op)

