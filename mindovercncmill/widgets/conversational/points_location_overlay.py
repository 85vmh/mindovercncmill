import os
from mindovercncmill.widgets.input_overlay import InputOverlay
from dataclass.points_locations import PointsLocations
from qtpy.QtCore import Signal
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

UI_FILE = os.path.join(os.path.dirname(__file__), "ui/hole_locations.ui")


class PointsLocationOverlay(InputOverlay):
    pointsLocationsChanged = Signal(object)

    def __init__(self, pointsLocations, parent=None):
        super(PointsLocationOverlay, self).__init__(UI_FILE, parent)

        LOG.debug("-------PointsLocationOverlay constructor: {}".format(pointsLocations.__dict__))

        self._is_adding_new = False
        if pointsLocations is None:
            self._pointsLocations = PointsLocations()
            self._is_adding_new = True
        else:
            self._pointsLocations = pointsLocations
            self.populateInitialValues(self._pointsLocations)

        self.dialog.btnCancel.clicked.connect(self.hide)
        self.dialog.btnDoneEditing.clicked.connect(self.handleDoneClicked)

    def populateInitialValues(self, pointsLocations):
        LOG.debug("-------populateInitialValues: {}".format(pointsLocations.__dict__))
        self.dialog.diameter_input.setText(str(pointsLocations.circle_diameter))
        self.dialog.center_x_input.setText(str(pointsLocations.circle_xy_coord[0]))
        self.dialog.center_y_input.setText(str(pointsLocations.circle_xy_coord[1]))
        self.dialog.num_holes_input.setText(str(pointsLocations.num_holes))
        self.dialog.start_angle_input.setText(str(pointsLocations.start_angle))

    def handleDoneClicked(self):
        # TODO: validation
        self._pointsLocations.circle_diameter = self.dialog.diameter_input.value()
        self._pointsLocations.circle_xy_coord = [self.dialog.center_x_input.value(), self.dialog.center_y_input.value()]
        self._pointsLocations.num_holes = self.dialog.num_holes_input.value()
        self._pointsLocations.start_angle = self.dialog.start_angle_input.value()

        if self._is_adding_new:
            self.pointsLocationsChanged.emit(self._pointsLocations)
        else:
            self.pointsLocationsChanged.emit(None)

        self.hide()
