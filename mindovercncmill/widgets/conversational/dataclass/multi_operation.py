from .base_operation import BaseOperation
from .points_locations import PointsLocations
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)


class MultiOperation(BaseOperation):
    def __init__(self, points_locations=PointsLocations(), hole_operations=None):
        super(MultiOperation, self).__init__()
        if hole_operations is None:
            hole_operations = []
        self.points_locations = points_locations
        self.hole_operations = hole_operations
        LOG.debug("------MultiOperation constructor: {}".format(points_locations.__dict__))

    def get_serializable_name(self):
        return 'multi_operation'

    def generate_gcode(self):
        xy_points = self.points_locations.getAllPoints()
        LOG.debug("------xy_points changed: {}".format(xy_points))
        gcode = []
        for op in self.hole_operations:
            op.holes = xy_points
            gcode.extend(op.generate_gcode())

        return gcode



