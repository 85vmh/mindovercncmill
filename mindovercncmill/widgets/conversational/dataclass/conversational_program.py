from qtpyvcp.utilities import logger
from datetime import datetime
from .single_operation import SingleOperation
from .holes_operation import HolesOperation

LOG = logger.getLogger(__name__)


class ConversationalProgram:
    def __init__(self, header=None, operations=None):
        if operations is None:
            operations = []
        self.header = header
        self.operations = operations

    @staticmethod
    def encode(obj):
        LOG.debug("----obj: {} {}".format(obj, type(obj)))

        if isinstance(obj, HolesOperation):
            LOG.debug("----is hole op: {} {}".format(obj, type(obj)))
            obj.__dict__.pop("holes")
            return obj.__dict__
        elif isinstance(obj, SingleOperation):
            return {obj.get_operation_name(): obj.__dict__}

        return obj.__dict__

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
            an_operation.isMetric = self.header.isMetric()
            gcode.extend(an_operation.generate_gcode())

        gcode.append('G53 G0 Z0 (Move spindle up)')
        gcode.append('M30 (End the program)')
        gcode.append('%')
        LOG.debug("---- program gcode: {}".format(gcode))
        return '\n'.join(gcode)
