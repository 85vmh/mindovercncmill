from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BlinkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.default_color = self.getColor()

        self.animation = QPropertyAnimation(self, "color", self)
        self.animation.setDuration(1000)
        self.animation.setLoopCount(100)
        self.animation.setStartValue(self.default_color)
        self.animation.setEndValue(self.default_color)
        self.animation.setKeyValueAt(0.1, QColor(0,255,0))

    def getColor(self):
        return self.palette().color(QPalette.Button)

    def setColor(self, value):
        if value == self.getColor():
            return
        palette = self.palette()
        palette.setColor(self.backgroundRole(), value)
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def reset_color(self):
        self.setColor(self.default_color)

    color = pyqtProperty(QColor, getColor, setColor)

    def startAnimation(self):
        self.animation.start()

    def stopAnimation(self):
        self.animation.stop()
        self.button_stop.reset_color()