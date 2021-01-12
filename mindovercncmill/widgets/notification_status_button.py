import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
from qtpy.QtCore import Property
from qtpyvcp.plugins import getPlugin

class NotificationStatusButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)

        #self._animation = QPropertyAnimation(self, "color", self)

        # self._default_color = QtGui.QColor(30,30,30)
        # #
        # self._error_color = QtGui.QColor(255,0,0)
        # self._warning_color = QtGui.QColor(255, 255, 0)
        # self._info_color = QtGui.QColor(51, 184, 255)
        # self._debug_color = QtGui.QColor(0, 255, 0)
        #
        # self._blink_count = 100
        # self._blink_duration = 1000

        self.notification_channel = getPlugin("notifications")

        self.notification_channel.info_message.notify(self.__on_info_message)
        self.notification_channel.warn_message.notify(self.__on_warn_message)
        self.notification_channel.error_message.notify(self.__on_error_message)
        self.notification_channel.debug_message.notify(self.__on_debug_message)

    # def getColor(self):
    #     return self.palette().color(QPalette.Button)
    #
    # def setColor(self, value):
    #     if value == self.getColor():
    #         return
    #     palette = self.palette()
    #     palette.setColor(self.backgroundRole(), value)
    #     self.setAutoFillBackground(True)
    #     self.setPalette(palette)
    #
    # def reset_color(self):
    #     self.setColor(self.default_color)
    #
    # color = pyqtProperty(QColor, getColor, setColor)

    # @Property(str)
    # def errorColor(self):
    #     return self._error_color
    #
    # @errorColor.setter
    # def errorColor(self, value):
    #     self._error_color = value
    #
    # @Property(str)
    # def warningColor(self):
    #     return self._warning_color
    #
    # @warningColor.setter
    # def warningColor(self, value):
    #     self._warning_color = value
    #
    # @Property(str)
    # def infoColor(self):
    #     return self._info_color
    #
    # @infoColor.setter
    # def infoColor(self, value):
    #     self._info_color = value
    #
    # @Property(str)
    # def debugColor(self):
    #     return self._debug_color
    #
    # @debugColor.setter
    # def debugColor(self, value):
    #     self._debug_color = value

    # @Property(str)
    # def blinkCount(self):
    #     return self._blink_count
    #
    # @blinkCount.setter
    # def blinkCount(self, value):
    #     self._blink_count = value

    def mark_as_seen(self):
        # self._animation.stop()
        # self.setColor(self._default_color)
        self.setStyleSheet('QPushButton {border-color: black; color: white;}')

    # private methods
    def __on_info_message(self):
        #self.animate_button(self._info_color)
        self.setStyleSheet('QPushButton {border-color: blue; color: blue;}')

    def __on_warn_message(self):
        #self.animate_button(self._warn_color)
        self.setStyleSheet('QPushButton {border-color: yellow; color: yellow;}')

    def __on_error_message(self):
        #self.animate_button(self._error_color)
        self.setStyleSheet('QPushButton {border-color: red; color: red;}')

    def __on_debug_message(self):
        #self.animate_button(self._debug_color)
        self.setStyleSheet('QPushButton {border-color: green; color: green;}')

    def animate_button(self, target_color):
        # self.animation = QPropertyAnimation(self, "color", self)
        # self.animation.setDuration(1000)
        # self.animation.setLoopCount(100)
        # self.animation.setStartValue(self._default_color)
        # self.animation.setEndValue(self._default_color)
        # self.animation.setKeyValueAt(0.1, QColor(0, 255, 0))
        # self.animation.start()

        self.setStyleSheet('QPushButton {border-color: red; color: red;}')