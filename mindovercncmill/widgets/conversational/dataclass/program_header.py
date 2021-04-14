
class ProgramHeader:
    def __init__(self, name='', wcs='G54', units='mm'):
        self.name = name
        self.wcs = wcs
        self.units = units

    def isMetric(self):
        return self.units.lower() == 'mm'
