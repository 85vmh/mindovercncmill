import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from qtpy.QtCore import Signal, QUrl, Slot
from qtpy.QtQuickWidgets import QQuickWidget

from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
IN_DESIGNER = os.getenv('DESIGNER', False)
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class QmlProbe(QQuickWidget):
    xClearanceSig = Signal(int, arguments=['x_value'])
    zRetractSig = Signal(int, arguments=['z_value'])

    def __init__(self, parent=None):
        super(QmlProbe, self).__init__(parent)

        if IN_DESIGNER:
            return

        self.x_clearance = 10
        self.z_retract = 10

        # qml_probe is our connection to qml signal system
        self.engine().rootContext().setContextProperty("qml_probe", self)
        qml_path = os.path.join(WIDGET_PATH, "qml_probe.qml")
        url = QUrl.fromLocalFile(qml_path)

        self.setSource(url)  # Fixme fails on qtdesigner

    def hideEvent(self, *args, **kwargs):
        pass  # hack to prevent animation glitch when we are on another tab FIXME

    @Slot(int)
    def set_x_clearance(self, value):
        self.x_clearance = value
        self.xClearanceSig.emit(value)

    @Slot(int)
    def set_z_retract(self, value):
        self.z_retract = value
        self.zRetractSig.emit(value)
