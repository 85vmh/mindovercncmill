from abc import abstractmethod

from .single_operation import SingleOperation


class HolesOperation(SingleOperation):
    def __init__(self, holes=None):
        super(HolesOperation, self).__init__()
        self.z_start = 0.
        self.z_end = 0.
        self.retract = 0.
        self.retract_mode = 'G98'
        self.holes = holes if holes is not None else []

    def has_valid_inputs(self):
        return True

    def generate_gcode(self):
        gcode = self.start_operation()
        if len(self.holes) > 0:
            gcode.append('(Hole #1) G0 X{} Y{}'.format(self.repr_of(self.holes[0][0]), self.repr_of(self.holes[0][1])))
            gcode.append('G0 Z{} (Move to clearance height)'.format(self.repr_of(self.z_clear)))
            gcode.append(self.get_operation_comment())
            gcode.append(self.get_operation_code())
            for hole_number, hole in enumerate(self.holes[1:], start=1):
                gcode.append('(Hole #{}) X{} Y{} '.format(hole_number + 1, self.repr_of(hole[0]), self.repr_of(hole[1])))

        gcode.append('G80 (Cancel canned cycle)')
        gcode.extend(self.end_operation())
        return gcode

    @abstractmethod
    def get_operation_code(self):
        pass

    @abstractmethod
    def get_operation_comment(self):
        pass


class ManualDrillOperation(HolesOperation):
    def __init__(self, holes=None):
        super(ManualDrillOperation, self).__init__(holes)

    def get_operation_name(self):
        return "Manual Drilling"

    def get_operation_code(self):
        return 'M0'

    def get_operation_comment(self):
        return '(Manual drilling, will stop after each hole coordinate)'

    def generate_gcode(self):
        gcode = self.start_operation()
        if len(self.holes) > 0:
            for h in self.holes:
                gcode.append('G0 X{} Y{}'.format(self.repr_of(h[0]), self.repr_of(h[1])))
                gcode.append('G0 Z{}'.format(self.repr_of(self.z_start + self.retract)))
                gcode.append(self.get_operation_code())
                if self.retract_mode == 'G98':
                    gcode.append('G0 Z{}'.format(self.repr_of(self.z_clear)))

        gcode.extend(self.end_operation())
        return gcode


class DeepDrillOperation(HolesOperation):
    def __init__(self, holes=None):
        super(DeepDrillOperation, self).__init__(holes)

    def get_operation_name(self):
        return "Deep Drilling"

    def get_operation_comment(self):
        return '(Use G81 drilling cycle)'

    def get_operation_code(self):
        return '{} G81 R{} Z{} F{}'.format(self.retract_mode,
                                           self.repr_of(self.z_start + self.retract),
                                           self.repr_of(self.z_end),
                                           self.repr_of(self.z_feed))


class DwellOperation(HolesOperation):
    def __init__(self, holes=None, dwell_time=0.):
        super(DwellOperation, self).__init__(holes)
        self.dwell_time = dwell_time

    def get_operation_name(self):
        return "Dwell"

    def get_operation_comment(self):
        return '(Use G82 drilling cycle that dwells at the bottom of the hole)'

    def get_operation_code(self):
        return '{} G82 R{} Z{} P{} F{}'.format(self.retract_mode,
                                               self.repr_of(self.z_start + self.retract),
                                               self.repr_of(self.z_end),
                                               self.repr_of(self.dwell_time),
                                               self.repr_of(self.z_feed))


class PeckOperation(HolesOperation):
    def __init__(self, holes=None, peck_depth=0.1):
        super(PeckOperation, self).__init__(holes)
        self.peck_depth = peck_depth

    def get_operation_name(self):
        return "Pecking"

    def get_operation_comment(self):
        return '(Use G83 peck drilling with chip breaking)'

    def get_operation_code(self):
        return '{} G83 R{} Z{} Q{} F{}'.format(self.retract_mode,
                                               self.repr_of(self.z_start + self.retract),
                                               self.repr_of(self.z_end),
                                               self.repr_of(self.peck_depth),
                                               self.repr_of(self.z_feed))


class ChipBreakingOperation(HolesOperation):
    def __init__(self, holes=None, break_dist=0.1):
        super(ChipBreakingOperation, self).__init__(holes)
        self.break_dist = break_dist

    def get_operation_name(self):
        return "Chip Breaking"

    def get_operation_comment(self):
        return '(Use G73 Drilling Cycle with Chip Breaking)'

    def get_operation_code(self):
        return '{} G73 R{} Z{} Q{} F{}'.format(self.retract_mode,
                                               self.repr_of(self.z_start + self.retract),
                                               self.repr_of(self.z_end),
                                               self.repr_of(self.break_dist),
                                               self.repr_of(self.z_feed))


class RigidTappingOperation(HolesOperation):
    def __init__(self, holes=None, pitch=1):
        super(RigidTappingOperation, self).__init__(holes)
        self.pitch = pitch

    def get_operation_name(self):
        return "Rigid Tapping"

    def get_operation_comment(self):
        return '(Use G33.1 Rigid tapping cycle)'

    def get_operation_code(self):
        return 'G33.1 Z{} K{}'.format(self.repr_of(self.z_end), self.repr_of(self.pitch))
