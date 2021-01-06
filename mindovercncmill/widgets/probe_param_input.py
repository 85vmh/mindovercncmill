import os
from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import Property
from qtpyvcp.utilities.settings import getSetting, connectSetting
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

UI_FILE = os.path.join(os.path.dirname(__file__), "probe_param_input.ui")

class ProbeParamInputWidget(QWidget):
    def __init__(self, parent=None, inputObjectName=""):
        super(ProbeParamInputWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)

        labelSetting = getSetting("probewizard." + inputObjectName)
        if labelSetting != None:
            self.param_label.setText(labelSetting.__doc__ + ":")

        self.param_input.setObjectName(inputObjectName)
        valueSetting = getSetting("probewizard." + inputObjectName)
        if valueSetting != None:
            self.param_input.setText(str(valueSetting.value))

    def get_inputValue(self):
        """Gets or sets the value from the input field of this widget (str).
        """
        return self.param_input.text()
