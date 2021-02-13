from program_header import ProgramHeader
from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)
from datetime import datetime

class ConversationalProgram:
    def __init__(self, header=None, operations=None):
        if operations is None:
            operations = []
        self._header = header
        self._operations = operations
        self.epilog = ['G53 G0 Z0', 'M30', '%']

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def operations(self):
        return self._operations

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

        for an_operation in self._operations:
            an_operation.isMetric = self.header.isMetric()
            gcode.extend(an_operation.generate_code())

        gcode.extend(self.epilog)
        LOG.debug("---- program gcode: {}".format(gcode))

        return '\n'.join(gcode)
