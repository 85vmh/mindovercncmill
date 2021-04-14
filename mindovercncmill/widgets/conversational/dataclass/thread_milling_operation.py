from abc import abstractmethod

from mindovercncmill.widgets.conversational.dataclass.single_operation import SingleOperation

class ThreadMillingOperation(SingleOperation):
    def get_operation_name(self):
        return "Thread milling"

    def __init__(self):
        SingleOperation.__init__(self)
        self.z_start = 0.
        self.z_end = 0.
        self.retract = 0.
        self.retract_mode = 'G98'
        self.holes = []

    def has_valid_inputs(self):
        return True

    def generate_gcode(self):
        gcode = self.start_operation()

        gcode.append('G0 Z{}'.format(self.repr_of(self.z_end)))

        gcode.extend(self.end_operation())
        return gcode

