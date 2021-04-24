import os
from mindovercncmill.widgets.input_overlay import InputOverlay
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)
from qtpy.QtCore import Signal
from dataclass.program_details import ProgramDetails

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/program_details.ui")
MATERIALS = ['NONE', 'ALUMINIUM', 'PLASTICS', 'LOW CARBON STEEL', 'HIGH CARBON STEEL']


class ProgramDetailsOverlay(InputOverlay):
    programDetailsChanged = Signal(object)

    def __init__(self, program_details=ProgramDetails(), parent=None):
        super(ProgramDetailsOverlay, self).__init__(UI_FILE, parent)
        self._program_details = program_details

        if program_details.author != '':
            self.dialog.author_input.setText(program_details.author)

        if program_details.description != '':
            self.dialog.description_input.setText(program_details.description)

        for a_material in MATERIALS:
            self.dialog.material_input.addItem(a_material)

        if program_details.setup_instructions != '':
            self.dialog.instructions_input.setPlainText(program_details.setup_instructions)

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDone.clicked.connect(self.handleDoneClicked)

    def handleDoneClicked(self):
        # TODO: add program name validation
        self._program_details.author = self.dialog.author_input.text()
        self._program_details.description = self.dialog.description_input.text()
        self._program_details.material = self.dialog.material_input.currentText()
        self._program_details.setup_instructions = self.dialog.instructions_input.toPlainText()
        self.programDetailsChanged.emit(self._program_details)
        self.hide()

