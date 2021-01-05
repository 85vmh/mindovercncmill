from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

import resources_rc

# Setup logging
from qtpyvcp.utilities import logger
from enum import IntEnum

LOG = logger.getLogger('qtpyvcp.' + __name__)


class MainScreenPage(IntEnum):
    TOOLS = 0
    MAIN = 1
    FILE_MANAGER = 2
    WCS = 3


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""

    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        # self.btnManual.clicked.connect(self.setManualScreen)
        # self.btnMdi.clicked.connect(self.setMdiScreen)
        self.btnProgram.clicked.connect(self.setProgramScreen)
        self.btnLoadGCode.clicked.connect(self.loadGCode)
        self.change_program_button.clicked.connect(self.changeProgram)
        self.buttonGroupMdi.buttonClicked.connect(self.mdiHandleKeys)
        self.btnChangeTool.clicked.connect(self.changeCurrentTool)
        self.btnTools.clicked.connect(self.showToolsPage)
        self.btnOffsets.clicked.connect(self.showOffsetsPage)
        self.probewizardwidget.probingCodeReady.connect(self.loadGCode)
        self.probewizardwidget.probingFinished.connect(self.handleProbingFinished)

    def mdiHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def handleProbingFinished(self):
        self.setManualScreen()
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.WCS)

    # add any custom methods here
    def setManualScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        self.stackedWidgetLeftTop.setCurrentIndex(0)
        self.stackedWidgetLeftBottom.setCurrentIndex(0)
        self.stackedWidgetSliders.setCurrentIndex(0)

    def setMdiScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        self.stackedWidgetLeftTop.setCurrentIndex(1)
        self.stackedWidgetLeftBottom.setCurrentIndex(1)
        self.stackedWidgetSliders.setCurrentIndex(1)

    def showToolsPage(self):
        if self.btnTools.isChecked():
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.TOOLS)
        else:
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)

    def showOffsetsPage(self):
        if self.btnOffsets.isChecked():
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.WCS)
        else:
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)

    def setProgramScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.FILE_MANAGER)

    def loadGCode(self):
        # self.filesystemtable_left.loadSelected
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        self.stackedWidgetLeftTop.setCurrentIndex(2)
        # self.stackedWidgetLeftBottom.setCurrentIndex(2)
        # self.stackedWidgetSliders.setCurrentIndex(1)

    def changeProgram(self):
        # self.filesystemtable_left.loadSelected
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.FILE_MANAGER)

    def changeCurrentTool(self):
        self.stackedWidgetTool.setCurrentIndex(0)
