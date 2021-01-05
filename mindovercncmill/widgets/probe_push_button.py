from qtpyvcp.widgets import VCPButton
from qtpy.QtCore import Property

class ProbePushButton(VCPButton):
    def __init__(self, parent=None, filename=''):
        super(ProbePushButton, self).__init__(parent)
        self._filename = filename

    @Property(str)
    def filename(self):
        """Gets or sets the filename of the subroutine the button should call (str).

        The subroutine file must be on the subroutine path as specified in the INI.
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename