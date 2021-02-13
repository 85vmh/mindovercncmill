import os
from mindovercncmill.widgets.input_overlay import InputOverlay
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/program_header.ui")
STATUS = getPlugin('status')
WCS = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G59.1', 'G59.2', 'G59.3']
UNITS = ['IN', 'MM']


class ProgramHeaderOverlay(InputOverlay):
    def __init__(self, programHeader, parent=None):
        super(ProgramHeaderOverlay, self).__init__(UI_FILE, parent)
        self._programHeader = programHeader

        for a_wcs in WCS:
            self.dialog.wcs_input.addItem(a_wcs)

        for an_unit in UNITS:
            self.dialog.unit_input.addItem(an_unit)

        if programHeader.name != '':
            self.dialog.name_input.setText(programHeader.name)

        if programHeader.wcs != '':
            self.dialog.wcs_input.setCurrentIndex(WCS.index(programHeader.wcs))
        else:
            self.dialog.wcs_input.setCurrentIndex(STATUS.g5x_index() - 1)

        if programHeader.units != '':
            self.dialog.unit_input.setCurrentIndex(UNITS.index(programHeader.units.upper()))
        else:
            self.dialog.unit_input.setCurrentIndex(STATUS.program_units() - 1)

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDone.clicked.connect(self.handleDoneClicked)

    def handleDoneClicked(self):
        # TODO: add program name validation
        self._programHeader.name = self.dialog.name_input.text()
        self._programHeader.wcs = self.dialog.wcs_input.currentText()
        self._programHeader.units = self.dialog.unit_input.currentText()
        self.hide()

