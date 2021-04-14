from .single_operation import SingleOperation
import math


class FacingOperation(SingleOperation):
    def __init__(self):
        super(FacingOperation, self).__init__()
        self.x_start = 0.
        self.x_end = 0.
        self.y_start = 0.
        self.y_end = 0.
        self.step_over = 0.
        self.z_start = 0.
        self.z_end = 0.
        self.step_down = 0.
        self.retract = 0.

    def get_operation_name(self):
        return "Facing"

    def generate_gcode(self):
        width = abs(self.y_end - self.y_start)
        depth = abs(self.z_end - self.z_start)

        num_step_down = abs(int(math.ceil(depth / self.step_down)))
        num_step_over = abs(int(math.ceil(width / self.step_over)))

        step_over = width / num_step_over
        step_down = depth / num_step_down

        tool_radius = self.tool_diameter / 2
        ramp_radius = self.retract + step_down

        x_start = self.x_start - tool_radius - ramp_radius
        y_start = self.y_start + tool_radius - step_over
        z_start = self.z_start


        z = z_start
        gcode = self.start_operation()
        step_over = - step_over
        for i in xrange(num_step_down):
            x = self.x_end
            y = y_start
            gcode.append('G0 X{} Y{}'.format(self.repr_of(x_start), self.repr_of(y_start)))
            gcode.append('G0 Z{}'.format(self.repr_of(z + self.retract)))
            gcode.append('G18 G2 X{} Z{} I{}'
                         .format(self.repr_of(x_start + ramp_radius), self.repr_of(z + self.retract - ramp_radius), self.repr_of(ramp_radius)))

            z -= step_down

            gcode.append('G1 X{}'.format(self.repr_of(x)))
            for _ in xrange(num_step_over - 1):
                y += step_over
                if x == self.x_end:
                    gcode.append('G17 G2 Y{} J{}'.format(self.repr_of(y), self.repr_of(step_over / 2)))
                    x = self.x_start
                else:
                    gcode.append('G17 G3 Y{} J{}'.format(self.repr_of(y), self.repr_of(step_over / 2)))
                    x = self.x_end

                gcode.append('G1 X{}'.format(self.repr_of(x)))

            if x == self.x_start:
                gcode.append('G18 G3 X{} Z{} K{}'.format(self.repr_of(x - ramp_radius), self.repr_of(z + ramp_radius), self.repr_of(ramp_radius)))
            else:
                gcode.append('G18 G2 X{} Z{} K{}'.format(self.repr_of(x + ramp_radius), self.repr_of(z + ramp_radius), self.repr_of(ramp_radius)))

            if i < (num_step_down - 1):
                gcode.append('G0 Z{}'.format(self.repr_of(self.z_clear)))

        gcode.extend(self.end_operation())

        return gcode

    def has_valid_inputs(self):
        return True
