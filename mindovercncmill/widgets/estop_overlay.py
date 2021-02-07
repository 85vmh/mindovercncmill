import os
from input_overlay import InputOverlay
from qtpy.QtGui import QColor

UI_FILE = os.path.join(os.path.dirname(__file__), "estop.ui")

class EstopOverlay(InputOverlay):
    def __init__(self, parent=None):
        super(EstopOverlay, self).__init__(UI_FILE, parent)
        self.bg_color = QColor(200, 67, 67, 200)
        #self.dialog.btnAddFacingOp.clicked.connect(self.hide)
