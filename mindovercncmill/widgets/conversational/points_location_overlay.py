import os
from mindovercncmill.widgets.input_overlay import InputOverlay
from dataclass.points_locations import PointsLocations
from qtpy.QtCore import Signal

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/hole_locations.ui")


class PointsLocationOverlay(InputOverlay):
    pointsLocationsChanged = Signal(object)

    def __init__(self, pointsLocations=PointsLocations(), parent=None):
        super(PointsLocationOverlay, self).__init__(UI_FILE, parent)

        self._pointsLocations = pointsLocations
        if self._pointsLocations is not None:
            self.populateInitialValues(self._pointsLocations)

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDoneEditing.clicked.connect(self.handleDoneClicked)

    def populateInitialValues(self, pointsLocations):
        self.dialog.diameter_input.default_value = pointsLocations.circle_diameter
        self.dialog.center_x_input.default_value = pointsLocations.circle_xy_coord[0]
        self.dialog.center_y_input.default_value = pointsLocations.circle_xy_coord[1]
        self.dialog.num_holes_input.default_value = pointsLocations.num_holes
        self.dialog.start_angle_input.default_value = pointsLocations.start_angle

    def handleDoneClicked(self):
        # TODO: validation
        self._pointsLocations.circle_diameter = self.dialog.diameter_input.value()
        self._pointsLocations.circle_xy_coord = [self.dialog.center_x_input.value(), self.dialog.center_y_input.value()]
        self._pointsLocations.num_holes = self.dialog.num_holes_input.value()
        self._pointsLocations.start_angle = self.dialog.start_angle_input.value()
        self.pointsLocationsChanged.emit(self._pointsLocations)
        self.hide()
