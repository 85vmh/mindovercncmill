from enum import IntEnum
import os
import linuxcnc
import json

from qtpyvcp.utilities import logger
from program_header_overlay import ProgramHeaderOverlay
from points_location_overlay import PointsLocationOverlay
from base_widget import ConversationalBaseWidget
from qtpy.QtWidgets import QApplication
from dataclass.program_header import ProgramHeader
from dataclass.facing_operation import FacingOperation
from dataclass.holes_operation import *
from dataclass.multi_operation import MultiOperation
from facing_op_overlay import FacingOpOverlay
from dataclass.conversational_program import ConversationalProgram
from qtpyvcp.actions.program_actions import load as loadProgram

LOG = logger.getLogger(__name__)

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))


class WizardPage(IntEnum):
    PROGRAMS_LIST = 0
    NEW_PROGRAM = 1


class ConversationalWizardWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(ConversationalWizardWidget, self).__init__(parent, "ui/conversational.ui")

        self.btnNewProgram.clicked.connect(self.newProgram)
        self.btnBackToPrograms.clicked.connect(self.backToPrograms)
        self.btnHeader.clicked.connect(self.showHeaderDialog)
        self.btnAddOperation.clicked.connect(self.addFacingOperation)
        self.btnAddPointLocations.clicked.connect(self.addPointsLocation)
        self.btnGenerateAndLoad.clicked.connect(self.generateAndLoad)
        self.header_dialog = None
        self.facing_dialog = None
        self.points_location_dialog = None

        self.conv_program = ConversationalProgram()

    def newProgram(self):
        self.stackedWidget.setCurrentIndex(WizardPage.NEW_PROGRAM)

    def backToPrograms(self):
        self.stackedWidget.setCurrentIndex(WizardPage.PROGRAMS_LIST)

    def showHeaderDialog(self):
        self.header_dialog = ProgramHeaderOverlay()
        self.header_dialog.programHeaderChanged.connect(self.headerChanged)
        self.showInputOverlayDialog(self.header_dialog)

    def headerChanged(self, header):
        #LOG.debug("------header changed: {}".format(self.toJson(header)))
        self.conv_program.header = header

    def addFacingOperation(self):
        self.facing_dialog = FacingOpOverlay()
        self.facing_dialog.operationChanged.connect(self.facingParamsChanged)
        self.showInputOverlayDialog(self.facing_dialog)

    def facingParamsChanged(self, operation):
        #LOG.debug("------facing operation changed: {}".format(self.toJson(operation)))
        self.conv_program.operations.append(operation)

    def addPointsLocation(self):
        self.points_location_dialog = PointsLocationOverlay()
        self.points_location_dialog.pointsLocationsChanged.connect(self.pointsLocationsChanged)
        self.showInputOverlayDialog(self.points_location_dialog)

    def pointsLocationsChanged(self, pointsLocations):
        #LOG.debug("------pointsLocations changed: {}".format(self.toJson(pointsLocations)))

        multi_operation = MultiOperation(pointsLocations)

        peck_op = PeckOperation(peck_depth=0.5)
        peck_op.tool_number = 1
        peck_op.tool_diameter = 8
        peck_op.spindle_rpm = 2000
        peck_op.z_feed = 200
        peck_op.z_clear = 5
        peck_op.retract = 2
        multi_operation.hole_operations.append(peck_op)

        drill_op = DeepDrillOperation()
        drill_op.tool_number = 1
        drill_op.tool_diameter = 8
        drill_op.spindle_rpm = 2000
        drill_op.z_feed = 200
        drill_op.retract = 5
        drill_op.z_clear = 5
        drill_op.z_end = -20
        multi_operation.hole_operations.append(drill_op)

        # tap_op = RigidTappingOperation(pitch=2)
        # tap_op.tool_number = 2
        # tap_op.tool_diameter = 8
        # tap_op.spindle_rpm = 500
        # tap_op.z_feed = 200
        # tap_op.z_clear = 5
        # tap_op.retract = 5
        # tap_op.z_end = -20
        # multi_operation.hole_operations.append(tap_op)

        self.conv_program.operations.append(multi_operation)

    def showInputOverlayDialog(self, inputOverlay):
        win = QApplication.instance().activeWindow()
        win_pos = win.mapToGlobal(win.rect().center())
        inputOverlay.move(win_pos.x() - inputOverlay.width() / 2, win_pos.y() - inputOverlay.height() / 2)
        inputOverlay.show()

    # def toJson(self, instance):
    #     return json.dumps(instance, default=lambda x: x.__dict__)

    def generateAndLoad(self):
        text = self.conv_program.generate_gcode()
        LOG.debug("-------conv_program {}".format(self.conv_program.__dict__))

        jsons = json.dumps(self.conv_program, default=ConversationalProgram.encode)
        LOG.debug("-------Conversational program json: {}".format(jsons))

        program_base = os.path.join(PROGRAM_PREFIX, self.conv_program.name)
        program_path = program_base + '.ngc'

        i = 1
        while os.path.exists(program_path):
            program_path = '{}_{:d}.ngc'.format(program_base, i)
            i += 1

        self.write_to_file(program_path, text)
        loadProgram(program_path)

    def write_to_file(self, filename, content):
        f = open(filename, 'w')
        try:
            f.write(content)
        finally:
            f.close()

    # def _get_next_available_file_name(self):
    #     if self.name() == '':
    #         self.name_input.setText('Untitled')
    #
    #     program_base = os.path.join(PROGRAM_PREFIX, self.name())
    #     program_path = program_base + '.ngc'
    #
    #     i = 1
    #     while os.path.exists(program_path):
    #         program_path = '{}_{:d}.ngc'.format(program_base, i)
    #         i += 1
    #
    #     return program_path


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SingleOperation):
            return {obj.get_operation_name(): obj}

    # return json.JSONEncoder.default(self, obj)