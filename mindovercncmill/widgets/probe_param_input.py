import os
from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import Property
from qtpyvcp.utilities.settings import getSetting, connectSetting

UI_FILE = os.path.join(os.path.dirname(__file__), "probe_param_input.ui")

class ProbeParamInputWidget(QWidget):
    def __init__(self, parent=None, inputObjectName=""):
        super(ProbeParamInputWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)

        self.param_label.setText(inputObjectName + ":")
        self.param_input.setObjectName(inputObjectName)
        self.param_input.setProperty("settingName", "probe-input.input_probe_fast_fr")


    def get_inputValue(self):
        """Gets or sets the value from the input field of this widget (str).
        """
        return self.param_input.text()
