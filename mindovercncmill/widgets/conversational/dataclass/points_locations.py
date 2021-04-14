import math
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)


class PointsLocations:
    def __init__(self, circle_xy_coord=None, circle_diameter=0, start_angle=0, num_holes=0, free_xy_coord=None):
        if circle_xy_coord is None:
            self.circle_xy_coord = [0, 0]
        self.circle_diameter = circle_diameter
        self.start_angle = start_angle
        self.num_holes = num_holes
        if free_xy_coord is None:
            self.free_xy_coord = [0, 0]

    def getAllPoints(self):
        return self.__createCircleHoles(self.circle_diameter, self.circle_xy_coord, self.num_holes, self.start_angle)

    def __createCircleHoles(self, circle_diam, circle_center_xy, num_holes, start_angle=0):
        LOG.debug("------createCircleHoles: {}, {}, {}, {}".format(circle_diam, circle_center_xy, num_holes, start_angle))
        holes_result = []
        if num_holes == 0:
            return
        num_holes = abs(num_holes)
        curr_angle = start_angle
        angle_step = (360. / num_holes)

        for _ in range(0, num_holes):
            x = math.cos(math.radians(curr_angle)) * (circle_diam / 2.)
            y = math.sin(math.radians(curr_angle)) * (circle_diam / 2.)
            x += circle_center_xy[0]
            y += circle_center_xy[1]
            curr_angle += angle_step

            holes_result.append((x, y))

        LOG.debug("------holes_result: {}".format(holes_result))
        return holes_result
