from qtpy.QtCore import Qt, Slot, Property, QModelIndex, QSortFilterProxyModel
from qtpy.QtGui import QStandardItemModel, QColor, QBrush
from qtpy.QtWidgets import QTableView

from qtpyvcp.plugins import getPlugin
from collections import OrderedDict

from qtpyvcp.utilities import logger
LOG = logger.getLogger(__name__)

GM_CODES = OrderedDict([
    ("G0", "Coordinated Motion at Rapid Rate"),
    ("G1", "Coordinated Motion at Feed Rate"),
    ("G2", "Coordinated Helical Clockwise Motion at Feed Rate"),
    ("G3", "Coordinated Helical Counter Clockwise Motion at Feed Rate"),
    ("G4", "Dwell"),
    ("G5", "Cubic Spline"),
    ("G5.1", "Quadratic B-Spline"),
    ("G5.2", "NURBS, add control point"),
    ("G7", "Diameter Mode"),
    ("G8", "Radius Mode"),
    ("G17", "XY plane selection"),
    ("G18", "XZ plane selection"),
    ("G19", "YZ plane selection"),
    ("G20", "Inch units"),
    ("G21", "Millimeter units"),
    ("G30", "Go to pre-defined position"),
    ("G30.1", "Store predefined position"),
    ("G33", "Spindle synchronized motion"),
    ("G33.1", "Rigid tapping"),
    ("G40", "Cancel cutter compensation"),
    ("G41", "Radius compensation on left"),
    ("G42", "Radius compensation on right"),
    ("G43", "Use Tool Length Offset from Tool Table"),
    ("G43.1", "Dynamic Tool Length Offset"),
    ("G49", "Cancel Tool Length Offset"),
    ("G54", "Active work coordinate system 1"),
    ("G55", "Active work coordinate system 2"),
    ("G56", "Active work coordinate system 3"),
    ("G57", "Active work coordinate system 4"),
    ("G58", "Active work coordinate system 5"),
    ("G59", "Active work coordinate system 6"),
    ("G59.1", "Active work coordinate system 7"),
    ("G59.2", "Active work coordinate system 8"),
    ("G59.3", "Active work coordinate system 9"),
    ("G61", "Exact path mode"),
    ("G61.1", "Exact stop mode"),
    ("G64", "Path blending"),
    ("G73", "Canned cycle - drilling with chip-break"),
    ("G80", "Cancel canned cycle"),
    ("G81", "Canned cycle - drilling"),
    ("G82", "Canned cycle - drilling with dwell"),
    ("G83", "Canned cycle - peck drilling"),
    ("G86", "Canned cycle - boring, spindle stop, rapid out"),
    ("G89", "Canned cycle - boring, dwell, feed out"),
    ("G90", "Absolute distance mode"),
    ("G91", "Incremental distance mode"),
    ("G90.1", "I, J, K absolute distance mode"),
    ("G91.1", "I, J, K incremental distance mode"),
    ("G93", "Feed inverse time mode"),
    ("G94", "Feed per minute mode"),
    ("G95", "Feed per revolution mode"),
    ("G97", "RPM mode"),
    ("G98", "Retract to initial Z height"),
    ("G99", "Retract to R height"),
    ("M0", "Program pause"),
    ("M1", "Program pause"),
    ("M2", "Program end"),
    ("M3", "Start the spindle clockwise at S speed"),
    ("M4", "Start the spindle counterclockwise at S speed"),
    ("M5", "Stop the spindle"),
    ("M6", "Tool change"),
    ("M7", "Turn on mist coolant"),
    ("M8", "Turn on flood coolant"),
    ("M9", "Turn off both M7 and M8"),
    ("M19", "Orient Spindle"),
    ("M30", "Program end"),
    ("M48", "Enable spindle override & feed override controls"),
    ("M49", "Disable spindle override & feed override controls"),
    ("M50", "Feed override control"),
    ("M51", "Spindle override control"),
    ("M52", "Adaptive feed control"),
    ("M53", "Feed stop control"),
    ("M61", "Set current tool number")
])


class ActiveCodesModel(QStandardItemModel):
    def __init__(self, parent=None):
        super(ActiveCodesModel, self).__init__(parent)

        self.status = getPlugin('status')
        self.active_g_codes = self.status.gcodes.getValue('list')
        self.active_m_codes = self.status.mcodes.getValue('list')

        self.active_codes_only = True
        self.active_code_color = QColor(Qt.darkGreen)
        self.active_code_bg = None

        self._column_labels = ["Code", "Description"]

        self.setColumnCount(self.columnCount())
        self.setRowCount(self.rowCount())

        self.status.gcodes.notify(self.refreshModel)
        self.status.mcodes.notify(self.refreshModel)

    def refreshModel(self):
        # refresh model so current G and M codes gets highlighted
        self.beginResetModel()
        self.active_g_codes = self.status.gcodes.getValue('list')
        self.active_m_codes = self.status.mcodes.getValue('list')
        self.setRowCount(self.rowCount())
        self.endResetModel()

    def updateModel(self):
        # update model with new data
        self.beginResetModel()
        pass
        self.endResetModel()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._column_labels[section]

        return QStandardItemModel.headerData(self, section, orientation, role)

    def columnCount(self, parent=None):
        return len(self._column_labels)

    def rowCount(self, parent=None):
        if self.active_codes_only:
            return len(self.active_g_codes) # + len(self.active_m_codes)
        else:
            return len(GM_CODES)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.NoItemFlags

    def data(self, index, role=Qt.DisplayRole):
        row, col = index.row(), index.column()

        #all_active_codes = [self.active_g_codes, self.active_m_codes]

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if self.active_codes_only:
                a_code = self.active_g_codes[row]
            else:
                a_code = GM_CODES.keys()[row]

            if col == 0:
                return a_code
            elif col == 1:
                return GM_CODES[a_code]

        if self.active_codes_only:
            if role == Qt.TextColorRole:
                return QBrush(self.active_code_color)

            elif role == Qt.BackgroundRole and self.active_code_bg is not None:
                return QBrush(self.active_code_bg)
        else:
            if role == Qt.TextColorRole:
                if GM_CODES.keys()[row] in self.active_g_codes:
                    return QBrush(self.active_code_color)

            elif role == Qt.BackgroundRole and self.active_code_bg is not None:
                if GM_CODES.keys()[row] in self.active_g_codes:
                    return QBrush(self.active_code_bg)

        return QStandardItemModel.data(self, index, role)


class GMCodesTable(QTableView):
    def __init__(self, parent=None, activeCodesOnly=False):
        super(GMCodesTable, self).__init__(parent)

        self._activeCodesOnly = activeCodesOnly

        self.active_codes_model = ActiveCodesModel(self)
        self.setModel(self.active_codes_model)

        # Appearance/Behaviour settings
        self.verticalHeader().hide()
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setEditTriggers(QTableView.NoEditTriggers)
        self.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)

    @Slot(bool)
    def setActiveCodesOnly(self, value):
        if value:
            self.model().active_codes_only = True
        else:
            self.model().active_codes_only = False
        self.model().refreshModel()

    @Property(QColor)
    def activeCodeColor(self):
        return self.model().active_code_color

    @activeCodeColor.setter
    def activeCodeColor(self, color):
        self.model().active_code_color = color
        self.model().refreshModel()

    @Property(QColor)
    def activeCodeBackground(self):
        return self.model().active_code_bg or QColor()

    @activeCodeBackground.setter
    def activeCodeBackground(self, color):
        self.model().active_code_bg = color
        self.model().refreshModel()
