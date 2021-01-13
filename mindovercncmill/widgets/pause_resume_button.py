import linuxcnc

from qtpy.QtCore import Property
# Set up logging
from qtpyvcp.utilities import logger
from qtpyvcp.widgets import VCPButton

LOG = logger.getLogger(__name__)

from qtpyvcp.utilities.info import Info
from qtpyvcp.plugins import getPlugin

STATUS = getPlugin('status')
STAT = STATUS.stat
INFO = Info()
CMD = linuxcnc.command()


class PauseResumeButton(VCPButton):
    def __init__(self, parent=None, pauseText='Pause', resumeText='Resume'):
        super(PauseResumeButton, self).__init__(parent)
        self._pauseText = pauseText
        self._resumeText = resumeText

        STATUS.state.onValueChanged(lambda: self._processState())
        STATUS.paused.onValueChanged(lambda: self._processState())

        self.clicked.connect(self._handleClick)

    @Property(str)
    def pauseText(self):
        return self._pauseText

    @pauseText.setter
    def pauseText(self, value):
        self._pauseText = value

    @Property(str)
    def resumeText(self):
        return self._resumeText

    @resumeText.setter
    def resumeText(self, value):
        self._resumeText = value

    def _processState(self):
        LOG.debug("--------- _processState called")
        if STAT.state == linuxcnc.RCS_EXEC:
            if STAT.paused:
                text = self._resumeText
                msg = "Resume program execution"
                ok = True
            else:
                text = self._pauseText
                msg = "Pause program execution"
                ok = True
        else:
            text = self._pauseText + "/" + self._resumeText
            msg = "No loaded program to pause/resume"
            ok = False

        self.setText(text)
        self.setEnabled(ok)
        self.setStatusTip(msg)
        self.setToolTip(msg)

    def _handleClick(self):
        if self.text() == self._resumeText:
            LOG.debug("Resuming program execution")
            CMD.auto(linuxcnc.AUTO_RESUME)
        elif self.text() == self._pauseText:
            LOG.debug("Pausing program execution")
            CMD.auto(linuxcnc.AUTO_PAUSE)
        else:
            LOG.debug("Program not running, nothing to do")