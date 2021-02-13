import os

from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/operation_summary.ui")


class OperationSummaryItem(QWidget):
    def __init__(self, parent=None):
        super(OperationSummaryItem, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
