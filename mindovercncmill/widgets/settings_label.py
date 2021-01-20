from qtpy.QtCore import Property
from qtpy.QtWidgets import QLabel

from qtpyvcp import SETTINGS
from qtpyvcp.widgets import VCPWidget


class SettingsLabel(QLabel, VCPWidget):
    def __init__(self, parent):
        super(SettingsLabel, self).__init__(parent)
        self._setting = None
        self._setting_name = ''
        self._text_format = '{:5.3f}'

    @Property(str)
    def settingName(self):
        return self._setting_name

    @settingName.setter
    def settingName(self, name):
        self._setting_name = name

    def formatValue(self, value):
        if self._setting.value_type in (int, float):
            return self._text_format.format(value)
        if isinstance(value, basestring):
            return value
        else:
            return str(value)

    def setDisplayValue(self, value):
        text_to_show = self.formatValue(value)
        self.setText(text_to_show)

    def initialize(self):
        self._setting = SETTINGS.get(self._setting_name)
        if self._setting is not None:
            self.setDisplayValue(self._setting.getValue())


    @Property(str)
    def textFormat(self):
        return self._text_format

    @textFormat.setter
    def textFormat(self, text_fmt):
        self._text_format = text_fmt
