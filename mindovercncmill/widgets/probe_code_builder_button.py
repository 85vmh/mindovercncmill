import os
import re
from qtpy.QtWidgets import qApp
from qtpy.QtCore import Property

from qtpyvcp.utilities.info import Info
INFO = Info()

from qtpyvcp.widgets import VCPButton
from qtpyvcp.actions.program_actions import load as loadProgram

from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

# input: #<param_name> = #1 (=0.125 comment)
# result: [("param_name", "1", "0.125", "comment")]
# if a group is not present it will be an empty string
PARSE_POSITIONAL_ARGS = re.compile(r' *# *<([a-z0-9_-]+)> *= *#([0-9]+) *(?:\(= *([0-9.+-]+[0-9.]*?|) *(.*)\))?', re.I)

SUBROUTINE_SEARCH_DIRS = INFO.getSubroutineSearchDirs()
PROGRAM_PREFIX = INFO.getProgramPrefix()

class ProbeCodeBuilderButton(VCPButton):
    """Button for calling ngc subroutines.

    Args:
        parent (QWidget, optional) : The parent widget of the button, or None.
        filename (str, optional) : The filename of the NGCGUI style subroutine
            the button should call, including any extension. The subroutine must
            be on the subroutine path specified in the INI. The name of the
            subroutine must match exactly the sub/endsub name. The parameter
            #<parameter1> if found in the VCP the value from that widget will be
            used instead of the default value. If you don't have a default value
            you must have a widget by the same name. The widget can be a line
            edit, a spin box or a double spin box.
    ::

        example.ngc
        o<example> sub
        #<parameter1> = #1
        #<parameter2> = #2 (=default_value)

        ;Body of the subroutine

        o<example> endsub
    """
    def __init__(self, parent=None, filename=''):
        super(ProbeCodeBuilderButton, self).__init__(parent)

        self._filename = filename
        self.clicked.connect(self.parseRoutineAndGenerateCode)

    def parseRoutineAndGenerateCode(self):
        window = qApp.activeWindow()

        subfile = None
        for dir in SUBROUTINE_SEARCH_DIRS:
            subfile = os.path.join(dir, self._filename)
            if os.path.isfile(subfile):
                break

        if subfile is None:
            LOG.error('Subroutine file could not be found: yellow<{}>'.format(self._filename))
            return False

        with open(subfile, 'r') as fh:
            lines = fh.readlines()

        args = []
        for line in lines:
            line = line.strip()
            if not line.startswith('#'):
                continue
            result_list = PARSE_POSITIONAL_ARGS.findall(line)
            if len(result_list) == 0:
                continue

            pname, pnumber, default_val, comment = result_list[0]

            if int(pnumber) > 30:
                # only #1-#30 are passed to the sub
                continue

            try:
                # get the value from the GUI input widget
                val = getattr(window, pname).text() or default_val
            except:
                val = default_val
                LOG.warning('No input for red<{}> parameter, using default value blue<{}>'.format(pname, val))

            if val == '':
                LOG.error('No value given for parameter red<{}>, and no default specified'.format(pname))
                return False

            try:
                val = float(val)
            except ValueError:
                LOG.error('Input value "{}" given for parameter "{}" is not a valid number'.format(val, pname))
                return False

            index = int(pnumber) - 1
            while len(args) <= index:
                args.append("[0.0000]")

            args[index] = "[{}]".format(val)

        arg_str = ' '.join(args)
        sub_name = os.path.splitext(self._filename)[0]
        programText = "(Call the probing subroutine with user's entered values)\n" \
                      "o<{}> call {}\nM2".format(sub_name, arg_str)

        LOG.debug('Program text: <%s>', programText)

        new_file_path = os.path.join(PROGRAM_PREFIX, "with_vals_" + self._filename)
        LOG.debug('Writting output file: <%s>', new_file_path)
        outputFile = open(new_file_path, "w")
        outputFile.write(programText)
        outputFile.close()
        loadProgram(new_file_path)

    @Property(str)
    def filename(self):
        """Gets or sets the filename of the subroutine the button should call (str).

        The subroutine file must be on the subroutine path as specified in the INI.
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

if __name__ == "__main__":
    import sys
    from qtpy.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = SubCallButton()
    w.show()
    sys.exit(app.exec_())
