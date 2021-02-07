import os
from base_widget import ConversationalBaseWidget
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)


class ProgramHeaderWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(ProgramHeaderWidget, self).__init__(parent, "program_header.ui")

        self.wcs_input.addItem('G54')
        self.wcs_input.addItem('G55')
        self.wcs_input.addItem('G56')
        self.wcs_input.addItem('G57')
        self.wcs_input.addItem('G58')
        self.wcs_input.addItem('G59')
        self.wcs_input.addItem('G59.1')
        self.wcs_input.addItem('G59.2')
        self.wcs_input.addItem('G59.3')

        self.unit_input.addItem('IN')
        self.unit_input.addItem('MM')
        self.update_selected_unit()

        self.status.g5x_index.onValueChanged(self.update_wcs)
        self.status.program_units.onValueChanged(self.update_selected_unit)
        self.status.tool_in_spindle.onValueChanged(self.update_tool_number)

    def name(self):
        return self.name_input.text()

    def wcs(self):
        return self.wcs_input.currentText()

    def unit(self):
        return self.unit_input.currentText()

    def update_wcs(self):
        self.wcs_input.setCurrentIndex(self.status.g5x_index() - 1)

    def update_selected_unit(self):
        self.unit_input.setCurrentIndex(self.status.program_units() - 1)

    def update_tool_number(self):
        self.tool_number_input.setText('{}'.format(self.status.tool_in_spindle))
        self.set_tool_description_from_tool_num()

    def _get_next_available_file_name(self):
        if self.name() == '':
            self.name_input.setText('Untitled')

        program_base = os.path.join(self.program_prefix, self.name())
        program_path = program_base + '.ngc'

        i = 1
        while os.path.exists(program_path):
            program_path = '{}_{:d}.ngc'.format(program_base, i)
            i += 1

        return program_path