import os
from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import Property
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)
from qtpy.QtCore import Signal

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/conv_program_item.ui")


class ConvProgramItemWidget(QWidget):
    viewConvProgram = Signal(object)

    def __init__(self, conversational_program=None, parent=None):
        super(ConvProgramItemWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self._conv_program = conversational_program

        if self._conv_program is not None:
            self.templateName.setText(self._conv_program.header.name)
            self.author.setText(self._conv_program.details.author)
            self.description.setText(self._conv_program.details.description)
            self.btnView.clicked.connect(self.handleViewClicked)

    def handleViewClicked(self):
        self.viewConvProgram.emit(self._conv_program)

