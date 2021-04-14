from abc import abstractmethod


class BaseOperation(object):
    def __init__(self):
        self.isMetric = True

    @abstractmethod
    def generate_gcode(self): pass

    @property
    def precision(self):
        return 3 if self.isMetric else 4

    def repr_of(self, value):
        return ('%.{}f'.format(self.precision) % value).rstrip('0').rstrip('.')