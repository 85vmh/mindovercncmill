from enum import IntEnum
import os
import linuxcnc

from qtpyvcp.utilities import logger
from program_header_overlay import ProgramHeaderOverlay
from base_widget import ConversationalBaseWidget
from qtpy.QtWidgets import QApplication
from dataclass.program_header import ProgramHeader
from dataclass.facing_operation import FacingOperation
from facing_op_overlay import FacingOpOverlay
from dataclass.conversational_program import ConversationalProgram
from qtpyvcp.actions.program_actions import load as loadProgram

LOG = logger.getLogger(__name__)

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))

class WizardPage(IntEnum):
    PROGRAMS_LIST = 0
    NEW_PROGRAM = 1


class ConversationalWizardWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(ConversationalWizardWidget, self).__init__(parent, "ui/conversational.ui")

        self.btnNewProgram.clicked.connect(self.newProgram)
        self.btnBackToPrograms.clicked.connect(self.backToPrograms)
        self.btnHeader.clicked.connect(self.showHeaderDialog)
        self.btnAddOperation.clicked.connect(self.addFacingOperation)
        self.btnGenerateAndLoad.clicked.connect(self.generateAndLoad)

        self._header = ProgramHeader()
        self._facingOperation = FacingOperation()
        operations = [self._facingOperation]

        LOG.debug("------header: {}".format(self._header))
        LOG.debug("------header type: {}".format(type(self._header)))

        self.conv_program = ConversationalProgram(header=self._header, operations=operations)

        LOG.debug("------conv_program - header: {}".format(self.conv_program.header))
        LOG.debug("------conv_program - header type: {}".format(type(self.conv_program.header)))
        LOG.debug("------conv_program - op: {}".format(self.conv_program.operations))

        self.header_dialog = ProgramHeaderOverlay(self.conv_program.header)
        self.facing_dialog = FacingOpOverlay(self.conv_program.operations[0])

    def newProgram(self):
        self.stackedWidget.setCurrentIndex(WizardPage.NEW_PROGRAM)

    def backToPrograms(self):
        self.stackedWidget.setCurrentIndex(WizardPage.PROGRAMS_LIST)

    def showHeaderDialog(self):
        win = QApplication.instance().activeWindow()
        win_pos = win.mapToGlobal(win.rect().center())
        self.header_dialog.move(win_pos.x() - self.header_dialog.width() / 2, win_pos.y() - self.header_dialog.height() / 2)
        self.header_dialog.show()

    def addFacingOperation(self):
        win = QApplication.instance().activeWindow()
        win_pos = win.mapToGlobal(win.rect().center())
        self.facing_dialog.move(win_pos.x() - self.facing_dialog.width() / 2, win_pos.y() - self.facing_dialog.height() / 2)
        self.facing_dialog.show()

    def generateAndLoad(self):
        text = self.conv_program.generate_gcode()
        LOG.debug(text)

        program_base = os.path.join(PROGRAM_PREFIX, self.conv_program.name)
        program_path = program_base + '.ngc'

        i = 1
        while os.path.exists(program_path):
            program_path = '{}_{:d}.ngc'.format(program_base, i)
            i += 1

        self.write_to_file(program_path, text)
        loadProgram(program_path)


    def write_to_file(self, filename, content):
        f = open(filename, 'w')
        try:
            f.write(content)
        finally:
            f.close()

    # def _get_next_available_file_name(self):
    #     if self.name() == '':
    #         self.name_input.setText('Untitled')
    #
    #     program_base = os.path.join(PROGRAM_PREFIX, self.name())
    #     program_path = program_base + '.ngc'
    #
    #     i = 1
    #     while os.path.exists(program_path):
    #         program_path = '{}_{:d}.ngc'.format(program_base, i)
    #         i += 1
    #
    #     return program_path