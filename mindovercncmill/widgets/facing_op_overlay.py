import os
from input_overlay import InputOverlay

UI_FILE = os.path.join(os.path.dirname(__file__), "facing_op.ui")

class FacingOpOverlay(InputOverlay):
    def __init__(self, parent=None):
        super(FacingOpOverlay, self).__init__(UI_FILE, parent)

        self.dialog.btnAddFacingOp.clicked.connect(self.hide)
