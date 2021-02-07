from enum import IntEnum

from qtpyvcp.utilities import logger

from base_widget import ConversationalBaseWidget

LOG = logger.getLogger(__name__)

class WizardPage(IntEnum):
    PROGRAMS_LIST = 0
    NEW_PROGRAM = 1


class ConversationalWizardWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(ConversationalWizardWidget, self).__init__(parent, "conversational.ui")

        self.btnNewProgram.clicked.connect(self.newProgram)
        self.btnBackToPrograms.clicked.connect(self.backToPrograms)

    def newProgram(self):
        self.stackedWidget.setCurrentIndex(WizardPage.NEW_PROGRAM)

    def backToPrograms(self):
        self.stackedWidget.setCurrentIndex(WizardPage.PROGRAMS_LIST)