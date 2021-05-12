from qtpyvcp.utilities import logger
from datetime import datetime
from .single_operation import SingleOperation
from .holes_operation import *
from .multi_operation import MultiOperation
from .program_header import ProgramHeader
from .program_details import ProgramDetails
from .facing_operation import FacingOperation
from .points_locations import PointsLocations

LOG = logger.getLogger(__name__)


class ConversationalProgram:
    def __init__(self, header=None, details=None, operations=None):
        if operations is None:
            operations = []
        self.header = header
        self.details = details
        self.operations = operations

    @staticmethod
    def encode(obj):
        # LOG.debug("----obj: {} {}".format(obj, type(obj)))

        if isinstance(obj, HolesOperation):
            # LOG.debug("----is hole op: {} {}".format(obj, type(obj)))
            obj.__dict__.pop("holes")
            return {obj.get_serializable_name(): obj.__dict__}
        elif isinstance(obj, SingleOperation):
            return {obj.get_serializable_name(): obj.__dict__}
        elif isinstance(obj, MultiOperation):
            return {obj.get_serializable_name(): obj.__dict__}
        return obj.__dict__

    @classmethod
    def decode(cls, json):
        # LOG.debug("----decoding: {} {}".format(type(json), json))
        header = ProgramHeader(**json["header"])
        details = ProgramDetails(**json["details"])
        operations = []
        for op in json['operations']:
            # LOG.debug("----op: {} {}".format(type(op), op))
            if 'facing' in op:
                facingOp = FacingOperation()
                facingOp.__dict__.update(**op["facing"])
                operations.append(facingOp)
                LOG.debug("----facingOp: {} ".format(facingOp))
            if 'multi_operation' in op:
                pts_locations = PointsLocations()
                pts_locations.__dict__.update(**op["multi_operation"]['points_locations'])
                LOG.debug("----pointsLocations: {} ".format(pts_locations.__dict__))
                multiOp = MultiOperation(points_locations=pts_locations)
                for holeOp in op["multi_operation"]['hole_operations']:
                    if 'peck_drilling' in holeOp:
                        peck = PeckOperation()
                        peck.__dict__.update(**holeOp['peck_drilling'])
                        LOG.debug("----peckOp: {} ".format(peck))
                        multiOp.hole_operations.append(peck)
                    if 'deep_drilling' in holeOp:
                        deepDrill = DeepDrillOperation()
                        deepDrill.__dict__.update(**holeOp['deep_drilling'])
                        LOG.debug("----deepDrill: {} ".format(deepDrill))
                        multiOp.hole_operations.append(deepDrill)

                #multiOp.__dict__.update(**op["multi_operation"])
                operations.append(multiOp)

        LOG.debug("----parsed operations: {} ".format(operations))
        return ConversationalProgram(header, details, operations)

    @property
    def name(self):
        return self.header.name

    def generate_gcode(self):
        gcode = []
        LOG.debug("----header: {}".format(self.header.wcs))
        if self.header is not None:
            gcode.append('(Program created with MindOverCNC Mill - Conversational Wizard)')
            gcode.append('(Creation Date: {})'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            gcode.append('(Program Name: {})\n'.format(self.header.name))
            gcode.append('G17 (Current plane: XY)')
            gcode.append('G21 (Units: mm)' if self.header.isMetric() else 'G20 (units: inch)')
            gcode.append('{} (Active work coordinate system)'.format(self.header.wcs))
            gcode.append('G90 (Distance mode: absolute)')
            gcode.append('G91.1 (Arc distance mode: incremental for I, J & K offsets)')
            gcode.append('G94 (Feed rate mode: units/minute)\n')

        for an_operation in self.operations:
            LOG.debug("------an_operation: {}".format(an_operation))
            an_operation.isMetric = self.header.isMetric()
            gcode.extend(an_operation.generate_gcode())

        gcode.append('G53 G0 Z0 (Move spindle up)')
        gcode.append('M30 (End the program)')
        gcode.append('%')
        LOG.debug("---- program gcode: {}".format(gcode))
        return '\n'.join(gcode)
