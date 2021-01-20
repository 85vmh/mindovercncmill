# noinspection PyUnresolvedReferences
import resources_rc
import linuxcnc
import os
from enum import IntEnum

from qtpy.QtWidgets import QMessageBox
from qtpyvcp import hal
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.actions.machine_actions import issue_mdi

LOG = logger.getLogger('qtpyvcp.' + __name__)


class MainScreenPage(IntEnum):
    MAIN = 0
    FILE_MANAGER = 1
    TOOLS = 2
    OFFSETS = 3
    PROBING = 4
    SETTINGS = 5


class MainButtonsPage(IntEnum):
    DEFAULT = 0
    COMMAND_RUNNING = 1
    START_PROGRAM = 2
    PROGRAM_RUNNING = 3


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""

    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self._initialMainPage = MainScreenPage.MAIN
        self._initialLeftTopPage = 0
        self._pageBeforeCodesOpen = 0

        self.btnManual.clicked.connect(self.setManualScreen)
        self.btnMdi.clicked.connect(self.setMdiScreen)
        self.btnProgram.clicked.connect(self.setProgramScreen)
        self.btnLoadGCode.clicked.connect(self.loadGCode)
        self.buttonChangeProgram.clicked.connect(self.changeProgram)
        self.buttonGroupMdi.buttonClicked.connect(self.mdiHandleKeys)
        self.btnTools.clicked.connect(self.showToolsPage)
        self.btnOffsets.clicked.connect(self.showOffsetsPage)
        self.btnProbing.clicked.connect(self.showProbingPage)
        self.btnSettings.clicked.connect(self.showSettingsPage)
        self.btnStatus.clicked.connect(self.showStatusPage)
        self.btnActiveCodes.clicked.connect(self.showCodesPage)
        self.probewizardwidget.probingCodeReady.connect(self.loadGCode)
        self.probewizardwidget.probingFinished.connect(self.handleProbingFinished)
        self.spindlewidget.measureTool.connect(self.toggleMeasureFlag)
        self.notificationswidget.notificationsCleared.connect(self.hideNotifications)

        self.STATUS = getPlugin('status')
        self.STATUS.gcodes.notify(self.setActiveCodesButtonText)
        self.STATUS.mcodes.notify(self.setActiveCodesButtonText)
        self.setActiveCodesButtonText()

        self.STATUS.task_mode.notify(self.setMainButtonsState)
        self.STATUS.interp_state.notify(self.setMainButtonsState)
        self.setMainButtonsState()

        self.comp = hal.component('mindovercnc')
        self.comp.addPin('measure_tool', 'bit', 'in')
        self.comp.addPin("search_vel", 'float', 'out')
        self.comp.addPin("probe_vel", 'float', 'out')
        self.comp.addPin("probeheight", 'float', 'out')
        self.comp.addPin("blockheight", 'float', 'out')

        self.comp.addPin('probe-plugged', 'bit', 'in')
        self.comp.addPin('probe-tripped', 'bit', 'in')
        self.comp.addListener('probe-plugged', self.onProbePlugged)
        self.comp.addListener('probe-tripped', self.onProbeTripped)
        self.comp.ready()

        self.comp.getPin('probeheight').value = -290.373
        self.comp.getPin('blockheight').value = -208.065
        self.comp.getPin('search_vel').value = 200.0
        self.comp.getPin('probe_vel').value = 20.0

    def toggleMeasureFlag(self, value):
        self.comp.getPin('measure_tool').value = value

    def setActiveCodesButtonText(self):
        active_g_codes = self.STATUS.gcodes
        active_m_codes = self.STATUS.mcodes
        first_line = '  '.join(map(str, active_g_codes))
        second_line = '  '.join(map(str, active_m_codes))
        self.btnActiveCodes.setText(first_line + "\n" + second_line)

    def setMainButtonsState(self):
        task_mode = self.STATUS.stat.task_mode
        interp_state = self.STATUS.stat.interp_state

        if task_mode == linuxcnc.MODE_MANUAL:
            self.stackedWidgetMainButtons.setCurrentIndex(MainButtonsPage.DEFAULT)
        elif task_mode == linuxcnc.MODE_MDI:
            if interp_state != linuxcnc.INTERP_IDLE:
                self.stackedWidgetMainButtons.setCurrentIndex(MainButtonsPage.COMMAND_RUNNING)
            else:
                self.stackedWidgetMainButtons.setCurrentIndex(MainButtonsPage.DEFAULT)
        elif task_mode == linuxcnc.MODE_AUTO:
            if interp_state != linuxcnc.INTERP_IDLE:
                self.stackedWidgetMainButtons.setCurrentIndex(MainButtonsPage.PROGRAM_RUNNING)
            else:
                self.stackedWidgetMainButtons.setCurrentIndex(MainButtonsPage.START_PROGRAM)

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
        self.btnManual.click()
        if not self.btnProbing.isChecked():
            self.btnProbing.click()
        else:
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.PROBING)

    # add any custom methods here
    def setManualScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        self.jogButtonsArea.setFocus()
        # self.stackedWidgetLeftTop.setCurrentIndex(0)
        # self.stackedWidgetLeftBottom.setCurrentIndex(0)
        # self.stackedWidgetSliders.setCurrentIndex(0)

    def setMdiScreen(self):
        self.stackedWidgetMain.setCurrentIndex(MainScreenPage.MAIN)
        self.mdiArea.setFocus()
        # self.stackedWidgetLeftTop.setCurrentIndex(1)
        # self.stackedWidgetLeftBottom.setCurrentIndex(1)
        # self.stackedWidgetSliders.setCurrentIndex(1)

    def showToolsPage(self):
        if self.btnTools.isChecked():
            self._initialMainPage = self.stackedWidgetMain.currentIndex()
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.TOOLS)
        else:
            self.stackedWidgetMain.setCurrentIndex(self._initialMainPage)

    def showOffsetsPage(self):
        if self.btnOffsets.isChecked():
            self._initialMainPage = self.stackedWidgetMain.currentIndex()
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.OFFSETS)
        else:
            self.stackedWidgetMain.setCurrentIndex(self._initialMainPage)

    def showProbingPage(self):
        if self.btnProbing.isChecked():
            self._initialMainPage = self.stackedWidgetMain.currentIndex()
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.PROBING)
        else:
            self.stackedWidgetMain.setCurrentIndex(self._initialMainPage)

    def showSettingsPage(self):
        if self.btnSettings.isChecked():
            self._initialMainPage = self.stackedWidgetMain.currentIndex()
            self.stackedWidgetMain.setCurrentIndex(MainScreenPage.SETTINGS)
        else:
            self.stackedWidgetMain.setCurrentIndex(self._initialMainPage)

    def showStatusPage(self):
        self.btnStatus.mark_as_seen()
        if self.btnStatus.isChecked():
            self._initialLeftTopPage = self.stackedWidgetLeftTop.currentIndex()
            self.stackedWidgetLeftTop.setCurrentIndex(3)
        else:
            self.stackedWidgetLeftTop.setCurrentIndex(self._initialLeftTopPage)

    def hideNotifications(self):
        self.btnStatus.mark_as_seen()
        self.btnStatus.setChecked(False)
        self.stackedWidgetLeftTop.setCurrentIndex(self._initialLeftTopPage)

    def showCodesPage(self):
        if self.btnActiveCodes.isChecked():
            self._pageBeforeCodesOpen = self.stackedWidgetLeftTop.currentIndex()
            self.stackedWidgetLeftTop.setCurrentIndex(4)
        else:
            self.stackedWidgetLeftTop.setCurrentIndex(self._pageBeforeCodesOpen)

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
        self.probewizardwidget.set_probe_plugged(plugged)
        if plugged:
            if not self.btnProbing.isChecked():
                self.btnProbing.click()
        else:
            if self.btnProbing.isChecked():
                self.btnProbing.click()

    def onProbeTripped(self, tripped):
        self.spindlewidget.set_probe_tripped(tripped)
        self.probewizardwidget.set_probe_tripped(tripped)