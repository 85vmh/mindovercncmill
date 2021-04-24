import os
from qtpy import uic
from PyQt5 import QtGui, QtWidgets

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/conv_program_item.ui")


class QCustomQWidget (QtWidgets.QWidget):                       # QtWidgets
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)

        self.label.setText("vasi")