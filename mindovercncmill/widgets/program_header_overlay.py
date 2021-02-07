import os
from input_overlay import InputOverlay

UI_FILE = os.path.join(os.path.dirname(__file__), "program_header.ui")

class ProgramHeaderOverlay(InputOverlay):
    def __init__(self, parent=None):
        super(ProgramHeaderOverlay, self).__init__(UI_FILE, parent)

        self.dialog.wcs_input.addItem('G54')
        self.dialog.wcs_input.addItem('G55')
        self.dialog.wcs_input.addItem('G56')
        self.dialog.wcs_input.addItem('G57')
        self.dialog.wcs_input.addItem('G58')
        self.dialog.wcs_input.addItem('G59')
        self.dialog.wcs_input.addItem('G59.1')
        self.dialog.wcs_input.addItem('G59.2')
        self.dialog.wcs_input.addItem('G59.3')

        self.dialog.unit_input.addItem('IN')
        self.dialog.unit_input.addItem('MM')

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDone.clicked.connect(self.hide)

