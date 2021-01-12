import linuxcnc
import os
from enum import IntEnum

from qtpy.QtWidgets import QMessageBox
from qtpyvcp import hal
from qtpyvcp.plugins import getPlugin
# Setup logging
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

LOG = logger.getLogger('qtpyvcp.' + __name__)


class MainScreenPage(IntEnum):
    TOOLS = 0
    MAIN = 1
    FILE_MANAGER = 2
    WCS = 3
    SETTINGS = 4


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""

    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.btnManual.clicked.connect(self.setManualScreen)
        self.btnMdi.clicked.connect(self.setMdiScreen)
        self.btnProgram.clicked.connect(self.setProgramScreen)
        self.btnLoadGCode.clicked.connect(self.loadGCode)
        self.buttonChangeProgram.clicked.connect(self.changeProgram)
        self.buttonGroupMdi.buttonClicked.connect(self.mdiHandleKeys)
        self.btnTools.clicked.connect(self.showToolsPage)
        self.btnOffsets.clicked.connect(self.showOffsetsPage)
        self.btnSettings.clicked.connect(self.showSettingsPage)
        self.pushStatusButton.clicked.connect(self.showStatusPage)
        self.probewizardwidget.probingCodeReady.connect(self.loadGCode)
        self.probewizardwidget.probingFinished.connect(self.handleProbingFinished)

        self.STATUS = getPlugin('status')
        #self.STATUS.task_mode.notify(self.reflectTaskMode)

        comp = hal.component('mindovercnc')
        comp.addPin('probe-plugged', 'bit', 'in')
        comp.addPin('probe-tripped', 'bit', 'in')
        comp.addListener('probe-plugged', self.onProbePlugged)
        comp.addListener('probe-tripped', self.onProbeTripped)
        comp.ready()

    # def reflectTaskMode(self, taskMode):
    #     self.btnManual.setChecked(taskMode == linuxcnc.MODE_MANUAL)
    #     self.btnMdi.setChecked(taskMode == linuxcnc.MODE_MDI)
    #     self.btnProgram.setChecked(taskMode == linuxcnc.MODE_AUTO)

    def on_btnExit_clicked(self):
        # self.closeEvent(QEvent.Close)
        quit_msg = "Are you sure you want to exit MindOverCNC Mill?"
        reply = QMessageBox.question(self, 'Exit MindOverCNC controller?', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.app.quit()
        else:
            pass

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
        # self.stackedWidgetLeftTop.setCurrentIndex(0)
        # self.stackedWidgetLeftBottom.setCurrentIndex(0)
        # self.stackedWidgetSliders.setCurrentIndex(0)

    def setMdiScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        # self.stackedWidgetLeftTop.setCurrentIndex(1)
        # self.stackedWidgetLeftBottom.setCurrentIndex(1)
        # self.stackedWidgetSliders.setCurrentIndex(1)

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

    def showSettingsPage(self):
        if self.btnSettings.isChecked():
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.SETTINGS)
        else:
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)

    def showStatusPage(self):
        if self.pushStatusButton.isChecked():
            self._initialLeftTopPage = self.stackedWidgetLeftTop.currentIndex()
            self.stackedWidgetLeftTop.setCurrentIndex(3)
        else:
            self.stackedWidgetLeftTop.setCurrentIndex(self._initialLeftTopPage)

    def setProgramScreen(self):
        stat = linuxcnc.stat()
        stat.poll()
        if os.path.exists(stat.file):
            # we already have a file
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
            self.stackedWidgetLeftTop.setCurrentIndex(2)
        else:
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

    def onProbePlugged(self, plugged):
        self.spindlewidget.set_probe_plugged(plugged)

    def onProbeTripped(self):
        pass