from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

import resources_rc

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

stackedWidgetMain_unhomed_index = 0
stackedWidgetMain_homed_index = 1
stackedWidgetMain_homed_filemanager = 2




class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.btnManual.clicked.connect(self.setManualScreen)
        self.btnMdi.clicked.connect(self.setMdiScreen)
        self.btnProgram.clicked.connect(self.setProgramScreen)
        self.btnLoadGCode.clicked.connect(self.loadGCode)
        self.change_program_button.clicked.connect(self.changeProgram)

    # add any custom methods here
    def setManualScreen(self):
        self.stackedWidgetMain.setCurrentIndex(stackedWidgetMain_homed_index)
        self.stackedWidgetLeftTop.setCurrentIndex(0)
        self.stackedWidgetLeftBottom.setCurrentIndex(0)
        self.stackedWidgetSliders.setCurrentIndex(0)

    def setMdiScreen(self):
        self.stackedWidgetMain.setCurrentIndex(stackedWidgetMain_homed_index)
        self.stackedWidgetLeftTop.setCurrentIndex(1)
        self.stackedWidgetLeftBottom.setCurrentIndex(1)
        self.stackedWidgetSliders.setCurrentIndex(1)

    def setProgramScreen(self):
        self.stackedWidgetMain.setCurrentIndex(stackedWidgetMain_homed_filemanager)

    def loadGCode(self):
        #self.filesystemtable_left.loadSelected
        self.stackedWidgetMain.setCurrentIndex(stackedWidgetMain_homed_index)    
        self.stackedWidgetLeftTop.setCurrentIndex(2)
        self.stackedWidgetLeftBottom.setCurrentIndex(2)
        self.stackedWidgetSliders.setCurrentIndex(1)

    def changeProgram(self):
        #self.filesystemtable_left.loadSelected
        self.stackedWidgetMain.setCurrentIndex(stackedWidgetMain_homed_filemanager)  


	