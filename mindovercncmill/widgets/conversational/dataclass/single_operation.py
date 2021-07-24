from abc import abstractmethod

from .base_operation import BaseOperation


class SingleOperation(BaseOperation):
    def __init__(self):
        super(SingleOperation, self).__init__()
        self.coolant = ''
        self.tool_number = 0
        self.tool_diameter = 0
        self.spindle_rpm = 0.
        self.spindle_dir = 'cw'
        self.z_feed = 0.
        self.z_clear = 0.
        self.xy_feed = 0.

    @abstractmethod
    def get_operation_name(self): pass

    @abstractmethod
    def get_serializable_name(self): pass

    @abstractmethod
    def has_valid_inputs(self): pass

    def isSpindleFwd(self):
        return self.spindle_dir.lower() == 'cw'

    def start_operation(self):
        gcode = [
            '(Start Operation: {})'.format(self.get_operation_name()),
            'T{:d} M6 G43 (Load tool & apply the length offset)'.format(self.tool_number),
            'S{} (Spindle speed)'.format(self.repr_of(self.spindle_rpm)),
            'M3 (Start spindle: forward)' if self.isSpindleFwd() else 'M4 (Start spindle: reverse)',
        ]
        if self.coolant.lower() == 'mist':
            gcode.append('M7 (Start coolant: mist)')
        elif self.coolant.lower() == 'flood':
            gcode.append('M8 (Start coolant: flood)')
        if self.xy_feed > 0:
            gcode.append('F{} (Feed rate in units/minute)'.format(self.repr_of(self.xy_feed)))
        return gcode



    def end_operation(self):
        gcode = []
        if self.coolant.strip() != '':
            gcode.append('M9 (Stop coolant)')
        gcode.append('G0 Z{} (Retract to preset value)'.format(self.repr_of(self.z_clear)))
        gcode.append('(End Operation: {})\n'.format(self.get_operation_name()))
        return gcode