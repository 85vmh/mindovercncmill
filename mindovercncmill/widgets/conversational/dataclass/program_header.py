
class ProgramHeader:
    def __init__(self, name='', wcs='G54', units='mm'):
        self._name = name
        self._wcs = wcs
        self._units = units

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def wcs(self):
        return self._wcs

    @wcs.setter
    def wcs(self, value):
        self._wcs = value

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        self._units = value

    def isMetric(self):
        return self.units.lower() == 'mm'