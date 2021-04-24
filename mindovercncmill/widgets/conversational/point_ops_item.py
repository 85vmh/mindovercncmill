import os

from qtpy import uic
from qtpy.QtWidgets import QWidget
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
from qtpy.QtCore import Signal

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/hole_ops_item.ui")


class PointOpsItemWidget(QWidget):
    editPointLocations = Signal(object)

    def __init__(self, points_locations=None, parent=None):
        super(PointOpsItemWidget, self).__init__(parent)
        uic.loadUi(UI_FILE, self)
        self._points_locations = points_locations

        if self._points_locations is not None:
            self.xCoord.setText(str(self._points_locations.circle_xy_coord[0]))
            self.yCoord.setText(str(self._points_locations.circle_xy_coord[1]))
            self.diameter.setText(str(self._points_locations.circle_diameter))
            self.startAngle.setText(str(self._points_locations.start_angle))
            self.numPoints.setText(str(self._points_locations.num_holes))

            self.btnEditPoints.clicked.connect(self.handleEditClicked)

    def handleEditClicked(self):
        self.editPointLocations.emit(self._points_locations)

