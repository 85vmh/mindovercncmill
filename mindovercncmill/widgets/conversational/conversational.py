from enum import IntEnum
import os
import linuxcnc
import json
from PyQt5 import QtWidgets, QtCore
from qtpyvcp.utilities import logger
from program_header_overlay import ProgramHeaderOverlay
from program_details_overlay import ProgramDetailsOverlay
from points_location_overlay import PointsLocationOverlay
from hole_op_overlay import HoleOpOverlay
from base_widget import ConversationalBaseWidget
from qtpy.QtWidgets import QApplication
from dataclass.holes_operation import *
from dataclass.multi_operation import MultiOperation
from dataclass.program_header import ProgramHeader
from dataclass.program_details import ProgramDetails
from facing_op_overlay import FacingOpOverlay
from dataclass.conversational_program import ConversationalProgram
from qtpyvcp.actions.program_actions import load as loadProgram
from conv_program_item import ConvProgramItemWidget
from facing_op_item import FacingOpItemWidget
from point_ops_item import PointOpsItemWidget
from dataclass.facing_operation import FacingOperation
from dataclass.points_locations import PointsLocations

LOG = logger.getLogger(__name__)

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))
CONVERSATIONAL_TEMPLATE_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'CONVERSATIONAL_TEMPLATE_PREFIX') or '/tmp'))
CONVERSATIONAL_PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'CONVERSATIONAL_PROGRAM_PREFIX') or '/tmp'))


class WizardPage(IntEnum):
    PROGRAMS_LIST = 0
    NEW_PROGRAM = 1


class ConversationalWizardWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(ConversationalWizardWidget, self).__init__(parent, "ui/conversational.ui")

        self.btnNewProgram.clicked.connect(self.newProgram)
        self.btnBackToPrograms.clicked.connect(self.backToPrograms)
        self.btnHeader.clicked.connect(self.showHeaderDialog)
        self.btnDetails.clicked.connect(self.showDetailsDialog)
        self.btnAddOperation.clicked.connect(self.addFacingOperation)
        self.btnAddPointLocations.clicked.connect(self.addPointsLocation)
        self.btnDwell.clicked.connect(self.dwellOperation)
        self.btnPeck.clicked.connect(self.peckOperation)
        self.btnRigidTap.clicked.connect(self.rigidTapOperation)
        self.btnGenerateAndLoad.clicked.connect(self.generateAndLoad)
        self.header_dialog = None
        self.details_dialog = None
        self.facing_dialog = None
        self.points_location_dialog = None
        self.holes_op_dialog = None
        self.conv_program = None
        self.multi_operation = None

        self.loadConvPrograms()

    def newProgram(self):
        self.conv_program = ConversationalProgram(ProgramHeader(), ProgramDetails(), [])
        self.stackedWidget.setCurrentIndex(WizardPage.NEW_PROGRAM)

    def backToPrograms(self):
        self.stackedWidget.setCurrentIndex(WizardPage.PROGRAMS_LIST)
        self.loadConvPrograms()

    def showHeaderDialog(self):
        if self.conv_program.header is not None:
            self.header_dialog = ProgramHeaderOverlay(self.conv_program.header)
        else:
            self.header_dialog = ProgramHeaderOverlay()
        self.header_dialog.programHeaderChanged.connect(self.headerChanged)
        self.showInputOverlayDialog(self.header_dialog)

    def showDetailsDialog(self):
        if self.conv_program.details is not None:
            self.details_dialog = ProgramDetailsOverlay(self.conv_program.details)
        else:
            self.details_dialog = ProgramDetailsOverlay()
        self.details_dialog.programDetailsChanged.connect(self.detailsChanged)
        self.showInputOverlayDialog(self.details_dialog)

    def headerChanged(self, header):
        #LOG.debug("------header changed: {}".format(self.toJson(header)))
        self.conv_program.header = header
        self.loadProgramDetails()

    def detailsChanged(self, details):
        LOG.debug("------details changed: {}".format(details))
        self.conv_program.details = details
        self.loadProgramDetails()

    def addFacingOperation(self):
        self.editFacingOperation()

    def editFacingOperation(self, initial_value=None):
        self.facing_dialog = FacingOpOverlay(facingOperation=initial_value)
        self.facing_dialog.facingOperationChanged.connect(self.facingOperationChanged)
        self.showInputOverlayDialog(self.facing_dialog)

    def facingOperationChanged(self, operation):
        #LOG.debug("------facing operation changed: {}".format(self.toJson(operation)))
        if operation is not None:
            # if an operation was created, append it to the program, otherwise just reload
            self.conv_program.operations.append(operation)
        self.loadProgramDetails()

    def addPointsLocation(self):
        self.editPointsLocation()

    def editPointsLocation(self, initial_value=None):
        self.points_location_dialog = PointsLocationOverlay(pointsLocations=initial_value)
        self.points_location_dialog.pointsLocationsChanged.connect(self.pointsLocationsChanged)
        self.showInputOverlayDialog(self.points_location_dialog)

    def pointsLocationsChanged(self, pointsLocations):
        #LOG.debug("------pointsLocations changed: {}".format(self.toJson(pointsLocations)))
        if pointsLocations is not None:
            multi_operation = MultiOperation(pointsLocations)
            self.conv_program.operations.append(multi_operation)
        self.loadProgramDetails()

    def dwellOperation(self):
        self.holes_op_dialog = HoleOpOverlay(holeOp=DwellOperation())
        self.holes_op_dialog.holeOperationChanged.connect(self.holeOpChanged)
        self.showInputOverlayDialog(self.holes_op_dialog)

    def peckOperation(self):
        self.holes_op_dialog = HoleOpOverlay(holeOp=PeckOperation())
        self.holes_op_dialog.holeOperationChanged.connect(self.holeOpChanged)
        self.showInputOverlayDialog(self.holes_op_dialog)

    def rigidTapOperation(self):
        self.holes_op_dialog = HoleOpOverlay(holeOp=RigidTappingOperation())
        self.holes_op_dialog.holeOperationChanged.connect(self.holeOpChanged)
        self.showInputOverlayDialog(self.holes_op_dialog)

    def holeOpChanged(self, holeOp):
        LOG.debug("------holeOpChanged changed: {}".format(holeOp))
        for rootOp in self.conv_program.operations:
            if isinstance(rootOp, MultiOperation):
                rootOp.hole_operations.append(holeOp)

        self.loadProgramDetails()

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

        json_template = json.dumps(self.conv_program, default=ConversationalProgram.encode, indent=4)
        LOG.debug("-------Conversational program json: {}".format(json_template))

        program_base = os.path.join(CONVERSATIONAL_PROGRAM_PREFIX, self.conv_program.name)
        template_path = os.path.join(CONVERSATIONAL_TEMPLATE_PREFIX, self.conv_program.name + '.json')

        program_path = program_base + '.ngc'

        #i = 1
        #while os.path.exists(program_path):
        #    program_path = '{}_{:d}.ngc'.format(program_base, i)
        #    i += 1

        self.write_to_file(program_path, text)
        self.write_to_file(template_path, json_template)
        loadProgram(program_path)

    def loadConvPrograms(self):
        # TODO: take json only
        # conversational_programs = []
        # for filename in os.listdir(CONVERSATIONAL_TEMPLATE_PREFIX):
        #     with open(os.path.join(CONVERSATIONAL_TEMPLATE_PREFIX, filename), 'r') as f:  # open in readonly mode
        #         content = f.read()
        #         LOG.debug("-------file content {}".format(content))
        #         decoded_conv = ConversationalProgram.decode(json.loads(content))
        #         conversational_programs.append(decoded_conv)
        #         # json_template = json.dumps(decoded_conv, default=ConversationalProgram.encode, indent=4)
        #         # LOG.debug("-------Decoded Conversational:{} {}".format(filename, json_template))
        #
        # self.programsListWidget.clear()
        # for conv_prg in conversational_programs:
        #     convProgramItemWidget = ConvProgramItemWidget(conv_prg)
        #     convProgramItemWidget.viewConvProgram.connect(self.handleViewProgram)
        #     listWidgetItem = QtWidgets.QListWidgetItem(self.programsListWidget)
        #     # Set size hint, hardcoded, cannot find how to obtain it
        #     listWidgetItem.setSizeHint(QtCore.QSize(800, 100))
        #     # Add QListWidgetItem into QListWidget
        #     self.programsListWidget.addItem(listWidgetItem)
        #     self.programsListWidget.setItemWidget(listWidgetItem, convProgramItemWidget)
        pass

    def loadProgramDetails(self):
        self.labelProgramName.setText(self.conv_program.header.name)
        self.labelWcs.setText(self.conv_program.header.wcs)
        self.labelUnits.setText(self.conv_program.header.units)
        self.labelAuthorName.setText(self.conv_program.details.author)
        self.labelMaterial.setText(self.conv_program.details.material)
        self.labelDescription.setText(self.conv_program.details.description)

        self.opsListWidget.clear()
        operation_no = 0
        for an_op in self.conv_program.operations:
            operation_no = operation_no+1
            if isinstance(an_op, FacingOperation):
                facingOpItem = FacingOpItemWidget(facing_op=an_op, op_number=operation_no)
                facingOpItem.editFacingOp.connect(self.editFacingOperation)
                listWidgetItem = QtWidgets.QListWidgetItem(self.opsListWidget)
                # Set size hint, hardcoded, cannot find how to obtain it
                listWidgetItem.setSizeHint(QtCore.QSize(1090, 125))
                self.opsListWidget.addItem(listWidgetItem)
                self.opsListWidget.setItemWidget(listWidgetItem, facingOpItem)
            if isinstance(an_op, MultiOperation):
                LOG.debug("-------point locations: {}".format(an_op.points_locations.__dict__))
                pointOpsItem = PointOpsItemWidget(points_locations=an_op.points_locations, op_number=operation_no)
                pointOpsItem.editPointLocations.connect(self.editPointsLocation)
                listWidgetItem = QtWidgets.QListWidgetItem(self.opsListWidget)
                # Set size hint, hardcoded, cannot find how to obtain it
                listWidgetItem.setSizeHint(QtCore.QSize(1090, 160))
                self.opsListWidget.addItem(listWidgetItem)
                self.opsListWidget.setItemWidget(listWidgetItem, pointOpsItem)

    def handleViewProgram(self, selected_program):
        self.conv_program = selected_program
        self.stackedWidget.setCurrentIndex(WizardPage.NEW_PROGRAM)
        self.loadProgramDetails()


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