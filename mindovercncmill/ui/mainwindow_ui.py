# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cnc/mindovercncmill/mindovercncmill/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setStyleSheet("")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.gridFrame)
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame = QtWidgets.QFrame(self.horizontalWidget)
        self.verticalFrame.setStyleSheet("")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setLineWidth(0)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidgetMain = VCPStackedWidget(self.verticalFrame)
        self.stackedWidgetMain.setStyleSheet("")
        self.stackedWidgetMain.setObjectName("stackedWidgetMain")
        self.page_toolsScreen = QtWidgets.QWidget()
        self.page_toolsScreen.setObjectName("page_toolsScreen")
        self.frame_13 = QtWidgets.QFrame(self.page_toolsScreen)
        self.frame_13.setEnabled(True)
        self.frame_13.setGeometry(QtCore.QRect(440, 0, 821, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setContentsMargins(2, 0, 1, 2)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setContentsMargins(5, 5, 5, -1)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.tableWidget_2 = ToolTable(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tableWidget_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setStyleSheet("TootTable,\n"
"QHeaderView {\n"
"    font: 14pt \"Bebas Kai\";\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"ToolTable {\n"
"       border-top: 8px rgb(120, 120, 120);\n"
"    border-left: 4px  rgb(120, 120, 120);\n"
"    border-bottom: 5px rgb(120, 120, 120);\n"
"    border-right: 4px rgb(120, 120, 120);\n"
"    border-radius: 5px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(120, 120, 120);\n"
"    gridline-color: rgb(203, 203, 203);\n"
"    alternate-background-color: rgb(90, 90, 90);\n"
"}")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setLineWidth(3)
        self.tableWidget_2.setMidLineWidth(3)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setProperty("currentToolColor", QtGui.QColor(42, 56, 255))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.horizontalLayout_38.addWidget(self.tableWidget_2)
        self.verticalLayout_20.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.tool_table_delete_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_delete_button.sizePolicy().hasHeightForWidth())
        self.tool_table_delete_button.setSizePolicy(sizePolicy)
        self.tool_table_delete_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_delete_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_delete_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_delete_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_delete_button.setObjectName("tool_table_delete_button")
        self.horizontalLayout_37.addWidget(self.tool_table_delete_button)
        self.tool_table_add_tool_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_add_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_add_tool_button.setSizePolicy(sizePolicy)
        self.tool_table_add_tool_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_add_tool_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_add_tool_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_add_tool_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_add_tool_button.setObjectName("tool_table_add_tool_button")
        self.horizontalLayout_37.addWidget(self.tool_table_add_tool_button)
        self.tool_table_import_tool_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_import_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_import_tool_button.setSizePolicy(sizePolicy)
        self.tool_table_import_tool_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_import_tool_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_import_tool_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_import_tool_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_import_tool_button.setObjectName("tool_table_import_tool_button")
        self.horizontalLayout_37.addWidget(self.tool_table_import_tool_button)
        self.tool_table_export_tool_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_export_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_export_tool_button.setSizePolicy(sizePolicy)
        self.tool_table_export_tool_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_export_tool_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_export_tool_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_export_tool_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_export_tool_button.setObjectName("tool_table_export_tool_button")
        self.horizontalLayout_37.addWidget(self.tool_table_export_tool_button)
        self.tool_table_save_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_save_button.sizePolicy().hasHeightForWidth())
        self.tool_table_save_button.setSizePolicy(sizePolicy)
        self.tool_table_save_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_save_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_save_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_save_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_save_button.setObjectName("tool_table_save_button")
        self.horizontalLayout_37.addWidget(self.tool_table_save_button)
        self.tool_table_reload_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_reload_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reload_button.setSizePolicy(sizePolicy)
        self.tool_table_reload_button.setMinimumSize(QtCore.QSize(140, 33))
        self.tool_table_reload_button.setMaximumSize(QtCore.QSize(140, 33))
        self.tool_table_reload_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_reload_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_reload_button.setObjectName("tool_table_reload_button")
        self.horizontalLayout_37.addWidget(self.tool_table_reload_button)
        self.verticalLayout_20.addLayout(self.horizontalLayout_37)
        self.frame_11 = QtWidgets.QFrame(self.page_toolsScreen)
        self.frame_11.setGeometry(QtCore.QRect(10, 200, 145, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(100, 60))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 58))
        self.frame_11.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_100 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_100.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_50 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QtCore.QSize(48, 33))
        self.label_50.setMaximumSize(QtCore.QSize(48, 33))
        self.label_50.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setWordWrap(True)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_19.addWidget(self.label_50)
        self.tool_length_6 = StatusLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_6.sizePolicy().hasHeightForWidth())
        self.tool_length_6.setSizePolicy(sizePolicy)
        self.tool_length_6.setMinimumSize(QtCore.QSize(70, 33))
        self.tool_length_6.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_length_6.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_length_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length_6.setObjectName("tool_length_6")
        self.horizontalLayout_19.addWidget(self.tool_length_6)
        self.horizontalLayout_100.addLayout(self.horizontalLayout_19)
        self.label_43 = QtWidgets.QLabel(self.page_toolsScreen)
        self.label_43.setGeometry(QtCore.QRect(55, -3, 250, 403))
        self.label_43.setStyleSheet("image: url(:/images/atc_spindle_tool_dimensioned.png);")
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/images/atc_spindle_tool_dimensioned.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.frame_12 = QtWidgets.QFrame(self.page_toolsScreen)
        self.frame_12.setGeometry(QtCore.QRect(11, 365, 161, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(100, 60))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_101.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_51 = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QtCore.QSize(64, 33))
        self.label_51.setMaximumSize(QtCore.QSize(35, 33))
        self.label_51.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setWordWrap(True)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_20.addWidget(self.label_51)
        self.tool_diameter_3 = StatusLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_diameter_3.sizePolicy().hasHeightForWidth())
        self.tool_diameter_3.setSizePolicy(sizePolicy)
        self.tool_diameter_3.setMinimumSize(QtCore.QSize(70, 33))
        self.tool_diameter_3.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_diameter_3.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_diameter_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_diameter_3.setObjectName("tool_diameter_3")
        self.horizontalLayout_20.addWidget(self.tool_diameter_3)
        self.horizontalLayout_101.addLayout(self.horizontalLayout_20)
        self.label_38 = QtWidgets.QLabel(self.page_toolsScreen)
        self.label_38.setGeometry(QtCore.QRect(200, 540, 240, 200))
        self.label_38.setStyleSheet("image: url(:/images/tool_probe.png);")
        self.label_38.setText("")
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.tool_length_7 = StatusLabel(self.page_toolsScreen)
        self.tool_length_7.setGeometry(QtCore.QRect(190, 145, 50, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_7.sizePolicy().hasHeightForWidth())
        self.tool_length_7.setSizePolicy(sizePolicy)
        self.tool_length_7.setMinimumSize(QtCore.QSize(50, 33))
        self.tool_length_7.setMaximumSize(QtCore.QSize(50, 33))
        self.tool_length_7.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 15pt \"Bebas Kai\";\n"
"}")
        self.tool_length_7.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_length_7.setObjectName("tool_length_7")
        self.tool_touch_off_button = SubCallButton(self.page_toolsScreen)
        self.tool_touch_off_button.setGeometry(QtCore.QRect(20, 635, 201, 35))
        self.tool_touch_off_button.setMinimumSize(QtCore.QSize(145, 35))
        self.tool_touch_off_button.setStyleSheet("QPushButton {\n"
"    color: white;    \n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")
        self.tool_touch_off_button.setObjectName("tool_touch_off_button")
        self.halledindicator = HalLedIndicator(self.page_toolsScreen)
        self.halledindicator.setGeometry(QtCore.QRect(295, 605, 20, 20))
        self.halledindicator.setMinimumSize(QtCore.QSize(0, 20))
        self.halledindicator.setMaximumSize(QtCore.QSize(16777215, 20))
        self.halledindicator.setDiameter(20)
        self.halledindicator.setColor(QtGui.QColor(78, 154, 6))
        self.halledindicator.setObjectName("halledindicator")
        self.label_52 = QtWidgets.QLabel(self.page_toolsScreen)
        self.label_52.setGeometry(QtCore.QRect(275, 580, 64, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(64, 25))
        self.label_52.setMaximumSize(QtCore.QSize(35, 25))
        self.label_52.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setWordWrap(True)
        self.label_52.setObjectName("label_52")
        self.frame_13.raise_()
        self.label_43.raise_()
        self.frame_12.raise_()
        self.label_38.raise_()
        self.tool_length_7.raise_()
        self.frame_11.raise_()
        self.tool_touch_off_button.raise_()
        self.halledindicator.raise_()
        self.label_52.raise_()
        self.stackedWidgetMain.addWidget(self.page_toolsScreen)
        self.page_mainScreen = QtWidgets.QWidget()
        self.page_mainScreen.setObjectName("page_mainScreen")
        self.stackedWidgetLeftTop = VCPStackedWidget(self.page_mainScreen)
        self.stackedWidgetLeftTop.setGeometry(QtCore.QRect(5, 55, 491, 376))
        self.stackedWidgetLeftTop.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetLeftTop.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidgetLeftTop.setObjectName("stackedWidgetLeftTop")
        self.page_manual = QtWidgets.QWidget()
        self.page_manual.setObjectName("page_manual")
        self.gridWidget_2 = QtWidgets.QWidget(self.page_manual)
        self.gridWidget_2.setGeometry(QtCore.QRect(5, 60, 481, 316))
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.y_plus_jogbutton = ActionButton(self.gridWidget_2)
        self.y_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.y_plus_jogbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/y_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_plus_jogbutton.setIcon(icon)
        self.y_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_plus_jogbutton.setObjectName("y_plus_jogbutton")
        self.gridLayout_4.addWidget(self.y_plus_jogbutton, 0, 2, 1, 1)
        self.z_plus_jogbutton = ActionButton(self.gridWidget_2)
        self.z_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_plus_jogbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/z_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_plus_jogbutton.setIcon(icon1)
        self.z_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.z_plus_jogbutton.setObjectName("z_plus_jogbutton")
        self.gridLayout_4.addWidget(self.z_plus_jogbutton, 0, 0, 1, 1)
        self.x_minus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.x_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.x_minus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_minus_jogbutton.setStyleSheet("")
        self.x_minus_jogbutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/x_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_minus_jogbutton.setIcon(icon2)
        self.x_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_minus_jogbutton.setObjectName("x_minus_jogbutton")
        self.gridLayout_4.addWidget(self.x_minus_jogbutton, 1, 1, 1, 1)
        self.y_minus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.y_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.y_minus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.y_minus_jogbutton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/y_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_minus_jogbutton.setIcon(icon3)
        self.y_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_minus_jogbutton.setObjectName("y_minus_jogbutton")
        self.gridLayout_4.addWidget(self.y_minus_jogbutton, 3, 2, 1, 1)
        self.x_plus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_plus_jogbutton.setStyleSheet("")
        self.x_plus_jogbutton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/x_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_plus_jogbutton.setIcon(icon4)
        self.x_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_plus_jogbutton.setObjectName("x_plus_jogbutton")
        self.gridLayout_4.addWidget(self.x_plus_jogbutton, 1, 3, 1, 1)
        self.a_minus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton.setSizePolicy(sizePolicy)
        self.a_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.a_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.a_minus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.a_minus_jogbutton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/a_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_minus_jogbutton.setIcon(icon5)
        self.a_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_minus_jogbutton.setObjectName("a_minus_jogbutton")
        self.gridLayout_4.addWidget(self.a_minus_jogbutton, 3, 4, 1, 1)
        self.a_plus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton.setSizePolicy(sizePolicy)
        self.a_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.a_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.a_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.a_plus_jogbutton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/a_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_plus_jogbutton.setIcon(icon6)
        self.a_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_plus_jogbutton.setObjectName("a_plus_jogbutton")
        self.gridLayout_4.addWidget(self.a_plus_jogbutton, 0, 4, 1, 1)
        self.z_minus_jogbutton = ActionButton(self.gridWidget_2)
        self.z_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_minus_jogbutton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/z_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_minus_jogbutton.setIcon(icon7)
        self.z_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.z_minus_jogbutton.setObjectName("z_minus_jogbutton")
        self.gridLayout_4.addWidget(self.z_minus_jogbutton, 3, 0, 1, 1)
        self.jogincrement = JogIncrementWidget(self.page_manual)
        self.jogincrement.setGeometry(QtCore.QRect(5, 5, 481, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jogincrement.sizePolicy().hasHeightForWidth())
        self.jogincrement.setSizePolicy(sizePolicy)
        self.jogincrement.setMinimumSize(QtCore.QSize(0, 30))
        self.jogincrement.setMaximumSize(QtCore.QSize(16777215, 43))
        self.jogincrement.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}\n"
"\n"
"")
        self.jogincrement.setProperty("diameter", 0)
        self.jogincrement.setLayoutSpacing(2)
        self.jogincrement.setObjectName("jogincrement")
        self.stackedWidgetLeftTop.addWidget(self.page_manual)
        self.page_mdi = QtWidgets.QWidget()
        self.page_mdi.setObjectName("page_mdi")
        self.widget = QtWidgets.QWidget(self.page_mdi)
        self.widget.setGeometry(QtCore.QRect(0, 0, 491, 376))
        self.widget.setObjectName("widget")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget)
        self.pushButton_23.setGeometry(QtCore.QRect(220, 315, 50, 40))
        self.pushButton_23.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_23.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_23.setObjectName("pushButton_23")
        self.buttonGroupMdi = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroupMdi.setObjectName("buttonGroupMdi")
        self.buttonGroupMdi.addButton(self.pushButton_23)
        self.pushButton_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_22.setGeometry(QtCore.QRect(220, 261, 50, 40))
        self.pushButton_22.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_22.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.buttonGroupMdi.addButton(self.pushButton_22)
        self.pushButton_28 = QtWidgets.QPushButton(self.widget)
        self.pushButton_28.setGeometry(QtCore.QRect(430, 225, 50, 40))
        self.pushButton_28.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_28.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_28.setObjectName("pushButton_28")
        self.buttonGroupMdi.addButton(self.pushButton_28)
        self.pushButton_27 = QtWidgets.QPushButton(self.widget)
        self.pushButton_27.setGeometry(QtCore.QRect(370, 225, 50, 40))
        self.pushButton_27.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_27.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_27.setObjectName("pushButton_27")
        self.buttonGroupMdi.addButton(self.pushButton_27)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 135, 50, 40))
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_9.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.buttonGroupMdi.addButton(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 90, 50, 40))
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonGroupMdi.addButton(self.pushButton_7)
        self.pushButton_26 = QtWidgets.QPushButton(self.widget)
        self.pushButton_26.setGeometry(QtCore.QRect(430, 180, 50, 40))
        self.pushButton_26.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_26.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_26.setObjectName("pushButton_26")
        self.buttonGroupMdi.addButton(self.pushButton_26)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 90, 50, 40))
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.buttonGroupMdi.addButton(self.pushButton_8)
        self.pushButton_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(430, 135, 50, 40))
        self.pushButton_24.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_24.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_24.setObjectName("pushButton_24")
        self.buttonGroupMdi.addButton(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.widget)
        self.pushButton_25.setGeometry(QtCore.QRect(370, 180, 50, 40))
        self.pushButton_25.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_25.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_25.setObjectName("pushButton_25")
        self.buttonGroupMdi.addButton(self.pushButton_25)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(5, 10, 476, 46))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.runMdiCommand = QtWidgets.QPushButton(self.frame)
        self.runMdiCommand.setGeometry(QtCore.QRect(400, 5, 71, 36))
        self.runMdiCommand.setObjectName("runMdiCommand")
        self.mdiEntry = MDIEntry(self.frame)
        self.mdiEntry.setGeometry(QtCore.QRect(10, 10, 266, 25))
        self.mdiEntry.setClearButtonEnabled(True)
        self.mdiEntry.setProperty("mdi_history_size", 0)
        self.mdiEntry.setObjectName("mdiEntry")
        self.runMdiCommand_2 = QtWidgets.QPushButton(self.frame)
        self.runMdiCommand_2.setGeometry(QtCore.QRect(295, 5, 71, 36))
        self.runMdiCommand_2.setObjectName("runMdiCommand_2")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(5, 85, 276, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 5, 50, 40))
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroupMdi.addButton(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(215, 5, 50, 40))
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroupMdi.addButton(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 5, 50, 40))
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroupMdi.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(135, 5, 50, 40))
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroupMdi.addButton(self.pushButton_5)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(5, 145, 191, 216))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_21.setGeometry(QtCore.QRect(135, 170, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_21.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.buttonGroupMdi.addButton(self.pushButton_21)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(70, 8, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_11.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.buttonGroupMdi.addButton(self.pushButton_11)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(70, 62, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_14.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.buttonGroupMdi.addButton(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(135, 62, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_15.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.buttonGroupMdi.addButton(self.pushButton_15)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(135, 116, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_18.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_18.setObjectName("pushButton_18")
        self.buttonGroupMdi.addButton(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_17.setGeometry(QtCore.QRect(70, 116, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_17.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_17.setObjectName("pushButton_17")
        self.buttonGroupMdi.addButton(self.pushButton_17)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(7, 8, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroupMdi.addButton(self.pushButton_2)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(135, 8, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_12.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.buttonGroupMdi.addButton(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(7, 62, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_13.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.buttonGroupMdi.addButton(self.pushButton_13)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(7, 116, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_16.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_16.setObjectName("pushButton_16")
        self.buttonGroupMdi.addButton(self.pushButton_16)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_20.setGeometry(QtCore.QRect(7, 170, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_20.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_20.setObjectName("pushButton_20")
        self.buttonGroupMdi.addButton(self.pushButton_20)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_19.setGeometry(QtCore.QRect(70, 170, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_19.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_19.setObjectName("pushButton_19")
        self.buttonGroupMdi.addButton(self.pushButton_19)
        self.pushButton_29 = QtWidgets.QPushButton(self.widget)
        self.pushButton_29.setGeometry(QtCore.QRect(370, 315, 50, 40))
        self.pushButton_29.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_29.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_29.setObjectName("pushButton_29")
        self.buttonGroupMdi.addButton(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.widget)
        self.pushButton_30.setGeometry(QtCore.QRect(430, 315, 50, 40))
        self.pushButton_30.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_30.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_30.setObjectName("pushButton_30")
        self.buttonGroupMdi.addButton(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.widget)
        self.pushButton_31.setGeometry(QtCore.QRect(370, 270, 50, 40))
        self.pushButton_31.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_31.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_31.setObjectName("pushButton_31")
        self.buttonGroupMdi.addButton(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.widget)
        self.pushButton_32.setGeometry(QtCore.QRect(430, 270, 50, 40))
        self.pushButton_32.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_32.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButton_32.setObjectName("pushButton_32")
        self.buttonGroupMdi.addButton(self.pushButton_32)
        self.stackedWidgetLeftTop.addWidget(self.page_mdi)
        self.page_program = QtWidgets.QWidget()
        self.page_program.setObjectName("page_program")
        self.gcodeeditor_final = GcodeEditor(self.page_program)
        self.gcodeeditor_final.setGeometry(QtCore.QRect(5, 40, 486, 331))
        self.gcodeeditor_final.setStyleSheet("")
        self.gcodeeditor_final.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gcodeeditor_final.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.gcodeeditor_final.setProperty("is_editor", True)
        self.gcodeeditor_final.setObjectName("gcodeeditor_final")
        self.recentfilecombobox = RecentFileComboBox(self.page_program)
        self.recentfilecombobox.setGeometry(QtCore.QRect(90, 5, 316, 30))
        self.recentfilecombobox.setMinimumSize(QtCore.QSize(142, 30))
        self.recentfilecombobox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.recentfilecombobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"     border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image: url(:/images/combobox-arrow.png);\n"
"}\n"
" \n"
"QComboBox QAbstractItemView{\n"
"    background-color: #4f4f4f;\n"
"    color: #999999;\n"
"     selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}")
        self.recentfilecombobox.setProperty("resource", "")
        self.recentfilecombobox.setObjectName("recentfilecombobox")
        self.change_program_button = QtWidgets.QPushButton(self.page_program)
        self.change_program_button.setGeometry(QtCore.QRect(5, 5, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_program_button.sizePolicy().hasHeightForWidth())
        self.change_program_button.setSizePolicy(sizePolicy)
        self.change_program_button.setMinimumSize(QtCore.QSize(50, 30))
        self.change_program_button.setMaximumSize(QtCore.QSize(80, 30))
        self.change_program_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_program_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/new_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_program_button.setIcon(icon8)
        self.change_program_button.setIconSize(QtCore.QSize(30, 17))
        self.change_program_button.setObjectName("change_program_button")
        self.reload_program_button = QtWidgets.QPushButton(self.page_program)
        self.reload_program_button.setGeometry(QtCore.QRect(410, 5, 76, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_program_button.sizePolicy().hasHeightForWidth())
        self.reload_program_button.setSizePolicy(sizePolicy)
        self.reload_program_button.setMinimumSize(QtCore.QSize(50, 30))
        self.reload_program_button.setMaximumSize(QtCore.QSize(80, 30))
        self.reload_program_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.reload_program_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.reload_program_button.setIconSize(QtCore.QSize(30, 17))
        self.reload_program_button.setObjectName("reload_program_button")
        self.stackedWidgetLeftTop.addWidget(self.page_program)
        self.page_status = QtWidgets.QWidget()
        self.page_status.setObjectName("page_status")
        self.notificationwidget = NotificationWidget(self.page_status)
        self.notificationwidget.setGeometry(QtCore.QRect(0, 0, 491, 376))
        self.notificationwidget.setMaximumSize(QtCore.QSize(491, 16777215))
        self.notificationwidget.setStyleSheet("QLabel {\n"
"    font-family: \"Bebas Kai\";\n"
"    color: white;\n"
"    font-size: 16pt;\n"
"}\n"
"")
        self.notificationwidget.setObjectName("notificationwidget")
        self.stackedWidgetLeftTop.addWidget(self.page_status)
        self.stackedWidgetLeftBottom = VCPStackedWidget(self.page_mainScreen)
        self.stackedWidgetLeftBottom.setGeometry(QtCore.QRect(5, 440, 291, 301))
        self.stackedWidgetLeftBottom.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetLeftBottom.setObjectName("stackedWidgetLeftBottom")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.actionbutton_9 = ActionButton(self.page_5)
        self.actionbutton_9.setGeometry(QtCore.QRect(145, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_9.sizePolicy().hasHeightForWidth())
        self.actionbutton_9.setSizePolicy(sizePolicy)
        self.actionbutton_9.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_9.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_9.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_9.setCheckable(True)
        self.actionbutton_9.setObjectName("actionbutton_9")
        self.actionbutton_8 = ActionButton(self.page_5)
        self.actionbutton_8.setGeometry(QtCore.QRect(10, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_8.sizePolicy().hasHeightForWidth())
        self.actionbutton_8.setSizePolicy(sizePolicy)
        self.actionbutton_8.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_8.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_8.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_8.setCheckable(True)
        self.actionbutton_8.setObjectName("actionbutton_8")
        self.stackedWidgetLeftBottom.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.actionbutton_6 = ActionButton(self.page_6)
        self.actionbutton_6.setGeometry(QtCore.QRect(65, 175, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_6.setSizePolicy(sizePolicy)
        self.actionbutton_6.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_6.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_6.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_6.setObjectName("actionbutton_6")
        self.actionbutton_10 = ActionButton(self.page_6)
        self.actionbutton_10.setGeometry(QtCore.QRect(10, 85, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_10.sizePolicy().hasHeightForWidth())
        self.actionbutton_10.setSizePolicy(sizePolicy)
        self.actionbutton_10.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_10.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_10.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_10.setCheckable(True)
        self.actionbutton_10.setObjectName("actionbutton_10")
        self.actionbutton_11 = ActionButton(self.page_6)
        self.actionbutton_11.setGeometry(QtCore.QRect(10, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_11.sizePolicy().hasHeightForWidth())
        self.actionbutton_11.setSizePolicy(sizePolicy)
        self.actionbutton_11.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_11.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_11.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_11.setCheckable(True)
        self.actionbutton_11.setObjectName("actionbutton_11")
        self.actionbutton_12 = ActionButton(self.page_6)
        self.actionbutton_12.setGeometry(QtCore.QRect(145, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_12.sizePolicy().hasHeightForWidth())
        self.actionbutton_12.setSizePolicy(sizePolicy)
        self.actionbutton_12.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_12.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_12.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_12.setCheckable(True)
        self.actionbutton_12.setObjectName("actionbutton_12")
        self.actionbutton_18 = ActionButton(self.page_6)
        self.actionbutton_18.setGeometry(QtCore.QRect(145, 85, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_18.sizePolicy().hasHeightForWidth())
        self.actionbutton_18.setSizePolicy(sizePolicy)
        self.actionbutton_18.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_18.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_18.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_18.setObjectName("actionbutton_18")
        self.stackedWidgetLeftBottom.addWidget(self.page_6)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.actionbutton_3 = ActionButton(self.page)
        self.actionbutton_3.setGeometry(QtCore.QRect(15, 60, 241, 52))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_3.setSizePolicy(sizePolicy)
        self.actionbutton_3.setMinimumSize(QtCore.QSize(0, 52))
        self.actionbutton_3.setMaximumSize(QtCore.QSize(16777215, 52))
        self.actionbutton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_3.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_3.setObjectName("actionbutton_3")
        self.stackedWidgetLeftBottom.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.actionbutton_13 = ActionButton(self.page_7)
        self.actionbutton_13.setGeometry(QtCore.QRect(145, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_13.sizePolicy().hasHeightForWidth())
        self.actionbutton_13.setSizePolicy(sizePolicy)
        self.actionbutton_13.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_13.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_13.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_13.setCheckable(True)
        self.actionbutton_13.setObjectName("actionbutton_13")
        self.actionbutton_7 = ActionButton(self.page_7)
        self.actionbutton_7.setGeometry(QtCore.QRect(65, 245, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_7.setSizePolicy(sizePolicy)
        self.actionbutton_7.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_7.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_7.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_7.setObjectName("actionbutton_7")
        self.actionbutton_14 = ActionButton(self.page_7)
        self.actionbutton_14.setGeometry(QtCore.QRect(10, 20, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_14.sizePolicy().hasHeightForWidth())
        self.actionbutton_14.setSizePolicy(sizePolicy)
        self.actionbutton_14.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_14.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_14.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_14.setCheckable(True)
        self.actionbutton_14.setObjectName("actionbutton_14")
        self.actionbutton_15 = ActionButton(self.page_7)
        self.actionbutton_15.setGeometry(QtCore.QRect(10, 75, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_15.sizePolicy().hasHeightForWidth())
        self.actionbutton_15.setSizePolicy(sizePolicy)
        self.actionbutton_15.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_15.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_15.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_15.setCheckable(True)
        self.actionbutton_15.setObjectName("actionbutton_15")
        self.actionbutton_16 = ActionButton(self.page_7)
        self.actionbutton_16.setGeometry(QtCore.QRect(10, 135, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_16.sizePolicy().hasHeightForWidth())
        self.actionbutton_16.setSizePolicy(sizePolicy)
        self.actionbutton_16.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_16.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_16.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_16.setCheckable(True)
        self.actionbutton_16.setObjectName("actionbutton_16")
        self.actionbutton_19 = ActionButton(self.page_7)
        self.actionbutton_19.setGeometry(QtCore.QRect(145, 135, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_19.sizePolicy().hasHeightForWidth())
        self.actionbutton_19.setSizePolicy(sizePolicy)
        self.actionbutton_19.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_19.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_19.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_19.setObjectName("actionbutton_19")
        self.actionbutton_17 = ActionButton(self.page_7)
        self.actionbutton_17.setGeometry(QtCore.QRect(145, 75, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_17.sizePolicy().hasHeightForWidth())
        self.actionbutton_17.setSizePolicy(sizePolicy)
        self.actionbutton_17.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_17.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_17.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_17.setObjectName("actionbutton_17")
        self.actionbutton_5 = ActionButton(self.page_7)
        self.actionbutton_5.setGeometry(QtCore.QRect(65, 195, 130, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_5.setSizePolicy(sizePolicy)
        self.actionbutton_5.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_5.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_5.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_5.setCheckable(True)
        self.actionbutton_5.setObjectName("actionbutton_5")
        self.stackedWidgetLeftBottom.addWidget(self.page_7)
        self.frame_dro_zone = QtWidgets.QFrame(self.page_mainScreen)
        self.frame_dro_zone.setGeometry(QtCore.QRect(575, 440, 436, 301))
        self.frame_dro_zone.setStyleSheet(".QFrame {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_dro_zone.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_dro_zone.setObjectName("frame_dro_zone")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_dro_zone)
        self.verticalLayout_56.setContentsMargins(5, 0, 3, 0)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_77.setSpacing(4)
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.frame_43 = QtWidgets.QFrame(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_43.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_43.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_144 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_144.setContentsMargins(15, 0, 22, 0)
        self.horizontalLayout_144.setSpacing(8)
        self.horizontalLayout_144.setObjectName("horizontalLayout_144")
        self.statuslabel_23 = StatusLabel(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_23.sizePolicy().hasHeightForWidth())
        self.statuslabel_23.setSizePolicy(sizePolicy)
        self.statuslabel_23.setMinimumSize(QtCore.QSize(50, 17))
        self.statuslabel_23.setMaximumSize(QtCore.QSize(50, 17))
        self.statuslabel_23.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 20px;\n"
"}")
        self.statuslabel_23.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_23.setObjectName("statuslabel_23")
        self.horizontalLayout_144.addWidget(self.statuslabel_23)
        self.statuslabel_24 = StatusLabel(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_24.sizePolicy().hasHeightForWidth())
        self.statuslabel_24.setSizePolicy(sizePolicy)
        self.statuslabel_24.setMinimumSize(QtCore.QSize(90, 17))
        self.statuslabel_24.setMaximumSize(QtCore.QSize(90, 17))
        self.statuslabel_24.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 6px;\n"
"}")
        self.statuslabel_24.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_24.setObjectName("statuslabel_24")
        self.horizontalLayout_144.addWidget(self.statuslabel_24)
        self.work_column_header_9 = QtWidgets.QLabel(self.frame_43)
        self.work_column_header_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_9.sizePolicy().hasHeightForWidth())
        self.work_column_header_9.setSizePolicy(sizePolicy)
        self.work_column_header_9.setMinimumSize(QtCore.QSize(100, 17))
        self.work_column_header_9.setMaximumSize(QtCore.QSize(100, 17))
        self.work_column_header_9.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_9.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_9.setObjectName("work_column_header_9")
        self.horizontalLayout_144.addWidget(self.work_column_header_9)
        self.dtg_column_header_4 = QtWidgets.QLabel(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtg_column_header_4.sizePolicy().hasHeightForWidth())
        self.dtg_column_header_4.setSizePolicy(sizePolicy)
        self.dtg_column_header_4.setMinimumSize(QtCore.QSize(90, 17))
        self.dtg_column_header_4.setMaximumSize(QtCore.QSize(90, 17))
        self.dtg_column_header_4.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.dtg_column_header_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dtg_column_header_4.setObjectName("dtg_column_header_4")
        self.horizontalLayout_144.addWidget(self.dtg_column_header_4)
        self.statuslabel_25 = StatusLabel(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_25.sizePolicy().hasHeightForWidth())
        self.statuslabel_25.setSizePolicy(sizePolicy)
        self.statuslabel_25.setMinimumSize(QtCore.QSize(40, 17))
        self.statuslabel_25.setMaximumSize(QtCore.QSize(40, 17))
        self.statuslabel_25.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 6px;\n"
"}")
        self.statuslabel_25.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_25.setObjectName("statuslabel_25")
        self.horizontalLayout_144.addWidget(self.statuslabel_25)
        self.horizontalLayout_77.addWidget(self.frame_43)
        self.verticalLayout_56.addLayout(self.horizontalLayout_77)
        self.x_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.x_axis_dro_layout.setContentsMargins(1, 1, 0, 1)
        self.x_axis_dro_layout.setSpacing(7)
        self.x_axis_dro_layout.setObjectName("x_axis_dro_layout")
        self.zero_x_button_3 = MDIButton(self.frame_dro_zone)
        self.zero_x_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_x_button_3.sizePolicy().hasHeightForWidth())
        self.zero_x_button_3.setSizePolicy(sizePolicy)
        self.zero_x_button_3.setMinimumSize(QtCore.QSize(60, 35))
        self.zero_x_button_3.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_x_button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_x_button_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zero_x_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zero_x_button_3.setIcon(icon9)
        self.zero_x_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_x_button_3.setObjectName("zero_x_button_3")
        self.x_axis_dro_layout.addWidget(self.zero_x_button_3)
        self.dro_entry_main_x = DROLineEdit(self.frame_dro_zone)
        self.dro_entry_main_x.setMinimumSize(QtCore.QSize(90, 30))
        self.dro_entry_main_x.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dro_entry_main_x.setFont(font)
        self.dro_entry_main_x.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.dro_entry_main_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_entry_main_x.setObjectName("dro_entry_main_x")
        self.x_axis_dro_layout.addWidget(self.dro_entry_main_x)
        self.drolabel_15 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_15.sizePolicy().hasHeightForWidth())
        self.drolabel_15.setSizePolicy(sizePolicy)
        self.drolabel_15.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_15.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_15.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_15.setProperty("referenceType", 0)
        self.drolabel_15.setProperty("axisNumber", 0)
        self.drolabel_15.setProperty("latheMode", 0)
        self.drolabel_15.setObjectName("drolabel_15")
        self.x_axis_dro_layout.addWidget(self.drolabel_15)
        self.drolabel_16 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_16.sizePolicy().hasHeightForWidth())
        self.drolabel_16.setSizePolicy(sizePolicy)
        self.drolabel_16.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_16.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_16.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_16.setProperty("referenceType", 2)
        self.drolabel_16.setProperty("axisNumber", 0)
        self.drolabel_16.setProperty("latheMode", 0)
        self.drolabel_16.setObjectName("drolabel_16")
        self.x_axis_dro_layout.addWidget(self.drolabel_16)
        self.axisactionbutton_6 = ActionButton(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_6.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_6.setSizePolicy(sizePolicy)
        self.axisactionbutton_6.setMinimumSize(QtCore.QSize(60, 35))
        self.axisactionbutton_6.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_6.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_6.setObjectName("axisactionbutton_6")
        self.x_axis_dro_layout.addWidget(self.axisactionbutton_6)
        self.verticalLayout_56.addLayout(self.x_axis_dro_layout)
        self.y_axis_dro_layout_3 = QtWidgets.QHBoxLayout()
        self.y_axis_dro_layout_3.setContentsMargins(1, 1, 1, 1)
        self.y_axis_dro_layout_3.setSpacing(7)
        self.y_axis_dro_layout_3.setObjectName("y_axis_dro_layout_3")
        self.zero_y_button_5 = MDIButton(self.frame_dro_zone)
        self.zero_y_button_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_y_button_5.sizePolicy().hasHeightForWidth())
        self.zero_y_button_5.setSizePolicy(sizePolicy)
        self.zero_y_button_5.setMinimumSize(QtCore.QSize(60, 35))
        self.zero_y_button_5.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_y_button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_y_button_5.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_y_button_5.setIcon(icon9)
        self.zero_y_button_5.setIconSize(QtCore.QSize(20, 20))
        self.zero_y_button_5.setObjectName("zero_y_button_5")
        self.y_axis_dro_layout_3.addWidget(self.zero_y_button_5)
        self.dro_entry_main_y_2 = DROLineEdit(self.frame_dro_zone)
        self.dro_entry_main_y_2.setMinimumSize(QtCore.QSize(90, 30))
        self.dro_entry_main_y_2.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dro_entry_main_y_2.setFont(font)
        self.dro_entry_main_y_2.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.dro_entry_main_y_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_entry_main_y_2.setProperty("axisNumber", 1)
        self.dro_entry_main_y_2.setObjectName("dro_entry_main_y_2")
        self.y_axis_dro_layout_3.addWidget(self.dro_entry_main_y_2)
        self.drolabel_19 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_19.sizePolicy().hasHeightForWidth())
        self.drolabel_19.setSizePolicy(sizePolicy)
        self.drolabel_19.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_19.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_19.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_19.setProperty("referenceType", 0)
        self.drolabel_19.setProperty("axisNumber", 1)
        self.drolabel_19.setProperty("latheMode", 0)
        self.drolabel_19.setObjectName("drolabel_19")
        self.y_axis_dro_layout_3.addWidget(self.drolabel_19)
        self.drolabel_20 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_20.sizePolicy().hasHeightForWidth())
        self.drolabel_20.setSizePolicy(sizePolicy)
        self.drolabel_20.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_20.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_20.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_20.setProperty("referenceType", 2)
        self.drolabel_20.setProperty("axisNumber", 1)
        self.drolabel_20.setProperty("latheMode", 0)
        self.drolabel_20.setObjectName("drolabel_20")
        self.y_axis_dro_layout_3.addWidget(self.drolabel_20)
        self.axisactionbutton_4 = ActionButton(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_4.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_4.setSizePolicy(sizePolicy)
        self.axisactionbutton_4.setMinimumSize(QtCore.QSize(60, 35))
        self.axisactionbutton_4.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_4.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_4.setObjectName("axisactionbutton_4")
        self.y_axis_dro_layout_3.addWidget(self.axisactionbutton_4)
        self.verticalLayout_56.addLayout(self.y_axis_dro_layout_3)
        self.z_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.z_axis_dro_layout.setContentsMargins(1, 1, 1, -1)
        self.z_axis_dro_layout.setSpacing(7)
        self.z_axis_dro_layout.setObjectName("z_axis_dro_layout")
        self.zero_z_button_3 = MDIButton(self.frame_dro_zone)
        self.zero_z_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_z_button_3.sizePolicy().hasHeightForWidth())
        self.zero_z_button_3.setSizePolicy(sizePolicy)
        self.zero_z_button_3.setMinimumSize(QtCore.QSize(60, 35))
        self.zero_z_button_3.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_z_button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_z_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_z_button_3.setIcon(icon9)
        self.zero_z_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_z_button_3.setObjectName("zero_z_button_3")
        self.z_axis_dro_layout.addWidget(self.zero_z_button_3)
        self.dro_entry_main_z = DROLineEdit(self.frame_dro_zone)
        self.dro_entry_main_z.setMinimumSize(QtCore.QSize(90, 30))
        self.dro_entry_main_z.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dro_entry_main_z.setFont(font)
        self.dro_entry_main_z.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.dro_entry_main_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_entry_main_z.setProperty("axisNumber", 2)
        self.dro_entry_main_z.setObjectName("dro_entry_main_z")
        self.z_axis_dro_layout.addWidget(self.dro_entry_main_z)
        self.drolabel_21 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_21.sizePolicy().hasHeightForWidth())
        self.drolabel_21.setSizePolicy(sizePolicy)
        self.drolabel_21.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_21.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_21.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_21.setProperty("referenceType", 0)
        self.drolabel_21.setProperty("axisNumber", 2)
        self.drolabel_21.setProperty("latheMode", 0)
        self.drolabel_21.setObjectName("drolabel_21")
        self.z_axis_dro_layout.addWidget(self.drolabel_21)
        self.drolabel_22 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_22.sizePolicy().hasHeightForWidth())
        self.drolabel_22.setSizePolicy(sizePolicy)
        self.drolabel_22.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_22.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_22.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_22.setProperty("referenceType", 2)
        self.drolabel_22.setProperty("axisNumber", 2)
        self.drolabel_22.setProperty("latheMode", 0)
        self.drolabel_22.setObjectName("drolabel_22")
        self.z_axis_dro_layout.addWidget(self.drolabel_22)
        self.axisactionbutton = ActionButton(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton.sizePolicy().hasHeightForWidth())
        self.axisactionbutton.setSizePolicy(sizePolicy)
        self.axisactionbutton.setMinimumSize(QtCore.QSize(60, 35))
        self.axisactionbutton.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton.setObjectName("axisactionbutton")
        self.z_axis_dro_layout.addWidget(self.axisactionbutton)
        self.verticalLayout_56.addLayout(self.z_axis_dro_layout)
        self.a_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.a_axis_dro_layout.setContentsMargins(1, 0, 1, 0)
        self.a_axis_dro_layout.setSpacing(7)
        self.a_axis_dro_layout.setObjectName("a_axis_dro_layout")
        self.zero_a_button_3 = MDIButton(self.frame_dro_zone)
        self.zero_a_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_a_button_3.sizePolicy().hasHeightForWidth())
        self.zero_a_button_3.setSizePolicy(sizePolicy)
        self.zero_a_button_3.setMinimumSize(QtCore.QSize(60, 35))
        self.zero_a_button_3.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_a_button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_a_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_a_button_3.setIcon(icon9)
        self.zero_a_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_a_button_3.setObjectName("zero_a_button_3")
        self.a_axis_dro_layout.addWidget(self.zero_a_button_3)
        self.dro_entry_main_a = DROLineEdit(self.frame_dro_zone)
        self.dro_entry_main_a.setMinimumSize(QtCore.QSize(90, 30))
        self.dro_entry_main_a.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dro_entry_main_a.setFont(font)
        self.dro_entry_main_a.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.dro_entry_main_a.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_entry_main_a.setProperty("axisNumber", 3)
        self.dro_entry_main_a.setObjectName("dro_entry_main_a")
        self.a_axis_dro_layout.addWidget(self.dro_entry_main_a)
        self.drolabel_23 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_23.sizePolicy().hasHeightForWidth())
        self.drolabel_23.setSizePolicy(sizePolicy)
        self.drolabel_23.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_23.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_23.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_23.setProperty("referenceType", 0)
        self.drolabel_23.setProperty("axisNumber", 3)
        self.drolabel_23.setProperty("latheMode", 0)
        self.drolabel_23.setObjectName("drolabel_23")
        self.a_axis_dro_layout.addWidget(self.drolabel_23)
        self.drolabel_24 = DROLabel(self.frame_dro_zone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_24.sizePolicy().hasHeightForWidth())
        self.drolabel_24.setSizePolicy(sizePolicy)
        self.drolabel_24.setMinimumSize(QtCore.QSize(90, 30))
        self.drolabel_24.setMaximumSize(QtCore.QSize(90, 30))
        self.drolabel_24.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.drolabel_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_24.setProperty("referenceType", 2)
        self.drolabel_24.setProperty("axisNumber", 3)
        self.drolabel_24.setProperty("latheMode", 0)
        self.drolabel_24.setObjectName("drolabel_24")
        self.a_axis_dro_layout.addWidget(self.drolabel_24)
        self.button_a_goto_zero = MDIButton(self.frame_dro_zone)
        self.button_a_goto_zero.setMinimumSize(QtCore.QSize(60, 35))
        self.button_a_goto_zero.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.button_a_goto_zero.setFont(font)
        self.button_a_goto_zero.setObjectName("button_a_goto_zero")
        self.a_axis_dro_layout.addWidget(self.button_a_goto_zero)
        self.verticalLayout_56.addLayout(self.a_axis_dro_layout)
        self.stackedWidgetSpindle = VCPStackedWidget(self.page_mainScreen)
        self.stackedWidgetSpindle.setGeometry(QtCore.QRect(1015, 640, 251, 101))
        self.stackedWidgetSpindle.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetSpindle.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidgetSpindle.setObjectName("stackedWidgetSpindle")
        self.page_spindle_off = QtWidgets.QWidget()
        self.page_spindle_off.setObjectName("page_spindle_off")
        self.frame_29 = QtWidgets.QFrame(self.page_spindle_off)
        self.frame_29.setGeometry(QtCore.QRect(80, 5, 88, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_29.setMaximumSize(QtCore.QSize(16777215, 38))
        self.frame_29.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_107.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.ref_coilumn_header_5 = QtWidgets.QLabel(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_5.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_5.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_5.setMinimumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_5.setMaximumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_5.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_5.setIndent(0)
        self.ref_coilumn_header_5.setObjectName("ref_coilumn_header_5")
        self.horizontalLayout_107.addWidget(self.ref_coilumn_header_5)
        self.spindleSpeed = VCPLineEdit(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindleSpeed.sizePolicy().hasHeightForWidth())
        self.spindleSpeed.setSizePolicy(sizePolicy)
        self.spindleSpeed.setMinimumSize(QtCore.QSize(55, 30))
        self.spindleSpeed.setMaximumSize(QtCore.QSize(55, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.spindleSpeed.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spindleSpeed.setFont(font)
        self.spindleSpeed.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spindleSpeed.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spindleSpeed.setStyleSheet("font: 17pt;")
        self.spindleSpeed.setMaxLength(5)
        self.spindleSpeed.setFrame(True)
        self.spindleSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.spindleSpeed.setObjectName("spindleSpeed")
        self.horizontalLayout_107.addWidget(self.spindleSpeed)
        self.spindleFwdButton = MDIButton(self.page_spindle_off)
        self.spindleFwdButton.setGeometry(QtCore.QRect(145, 50, 96, 40))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/cw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spindleFwdButton.setIcon(icon10)
        self.spindleFwdButton.setObjectName("spindleFwdButton")
        self.spindleFwdButton_2 = MDIButton(self.page_spindle_off)
        self.spindleFwdButton_2.setGeometry(QtCore.QRect(10, 50, 96, 40))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/ccw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spindleFwdButton_2.setIcon(icon11)
        self.spindleFwdButton_2.setObjectName("spindleFwdButton_2")
        self.stackedWidgetSpindle.addWidget(self.page_spindle_off)
        self.page_spindle_on = QtWidgets.QWidget()
        self.page_spindle_on.setObjectName("page_spindle_on")
        self.spindle_stop_button = ActionButton(self.page_spindle_on)
        self.spindle_stop_button.setGeometry(QtCore.QRect(180, 50, 60, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_stop_button.sizePolicy().hasHeightForWidth())
        self.spindle_stop_button.setSizePolicy(sizePolicy)
        self.spindle_stop_button.setMinimumSize(QtCore.QSize(60, 40))
        self.spindle_stop_button.setMaximumSize(QtCore.QSize(60, 35))
        self.spindle_stop_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_stop_button.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_stop_button.setProperty("option", True)
        self.spindle_stop_button.setObjectName("spindle_stop_button")
        self.spindle_load_indicator = HalBarIndicator(self.page_spindle_on)
        self.spindle_load_indicator.setGeometry(QtCore.QRect(10, 15, 231, 20))
        self.spindle_load_indicator.setMinimumSize(QtCore.QSize(0, 20))
        self.spindle_load_indicator.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.spindle_load_indicator.setFont(font)
        self.spindle_load_indicator.setStyleSheet(".HalBarIndicator{\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.spindle_load_indicator.setProperty("value", 100.0)
        self.spindle_load_indicator.setProperty("maximum", 150.0)
        self.spindle_load_indicator.setProperty("barGradient", ['0.0, 170, 170, 236', '0.63, 85, 85, 238', '0.65, 171, 171, 158', '0.79, 227, 237, 106', '0.84, 219, 124, 55', '1.0, 209, 0, 0'])
        self.spindle_load_indicator.setObjectName("spindle_load_indicator")
        self.statuslabel_6 = StatusLabel(self.page_spindle_on)
        self.statuslabel_6.setGeometry(QtCore.QRect(105, 55, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_6.sizePolicy().hasHeightForWidth())
        self.statuslabel_6.setSizePolicy(sizePolicy)
        self.statuslabel_6.setMinimumSize(QtCore.QSize(70, 30))
        self.statuslabel_6.setMaximumSize(QtCore.QSize(70, 30))
        self.statuslabel_6.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_6.setObjectName("statuslabel_6")
        self.work_column_header_10 = QtWidgets.QLabel(self.page_spindle_on)
        self.work_column_header_10.setEnabled(False)
        self.work_column_header_10.setGeometry(QtCore.QRect(10, 60, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_10.sizePolicy().hasHeightForWidth())
        self.work_column_header_10.setSizePolicy(sizePolicy)
        self.work_column_header_10.setMinimumSize(QtCore.QSize(90, 20))
        self.work_column_header_10.setMaximumSize(QtCore.QSize(90, 20))
        self.work_column_header_10.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.work_column_header_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.work_column_header_10.setObjectName("work_column_header_10")
        self.stackedWidgetSpindle.addWidget(self.page_spindle_on)
        self.stackedWidgetTool = VCPStackedWidget(self.page_mainScreen)
        self.stackedWidgetTool.setGeometry(QtCore.QRect(1015, 440, 251, 196))
        self.stackedWidgetTool.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetTool.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidgetTool.setObjectName("stackedWidgetTool")
        self.page_loadTool = QtWidgets.QWidget()
        self.page_loadTool.setObjectName("page_loadTool")
        self.frame_28 = QtWidgets.QFrame(self.page_loadTool)
        self.frame_28.setGeometry(QtCore.QRect(95, 105, 61, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_28.setMaximumSize(QtCore.QSize(68, 38))
        self.frame_28.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_106 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_106.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout_106.setSpacing(0)
        self.horizontalLayout_106.setObjectName("horizontalLayout_106")
        self.ref_coilumn_header_4 = QtWidgets.QLabel(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_4.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_4.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_4.setMinimumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_4.setMaximumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_4.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_4.setIndent(0)
        self.ref_coilumn_header_4.setObjectName("ref_coilumn_header_4")
        self.horizontalLayout_106.addWidget(self.ref_coilumn_header_4)
        self.tool_number_entry = VCPLineEdit(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_number_entry.sizePolicy().hasHeightForWidth())
        self.tool_number_entry.setSizePolicy(sizePolicy)
        self.tool_number_entry.setMinimumSize(QtCore.QSize(35, 30))
        self.tool_number_entry.setMaximumSize(QtCore.QSize(35, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 84, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.tool_number_entry.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tool_number_entry.setFont(font)
        self.tool_number_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tool_number_entry.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tool_number_entry.setStyleSheet("VCPLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 2px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.tool_number_entry.setMaxLength(3)
        self.tool_number_entry.setFrame(True)
        self.tool_number_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_number_entry.setObjectName("tool_number_entry")
        self.horizontalLayout_106.addWidget(self.tool_number_entry)
        self.m6g43 = MDIButton(self.page_loadTool)
        self.m6g43.setGeometry(QtCore.QRect(70, 150, 106, 40))
        self.m6g43.setObjectName("m6g43")
        self.label_2 = QtWidgets.QLabel(self.page_loadTool)
        self.label_2.setGeometry(QtCore.QRect(40, -25, 166, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/spindle_tool.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.frame_28.raise_()
        self.m6g43.raise_()
        self.stackedWidgetTool.addWidget(self.page_loadTool)
        self.page_toolLoadedNotRunning = QtWidgets.QWidget()
        self.page_toolLoadedNotRunning.setObjectName("page_toolLoadedNotRunning")
        self.statuslabel_zOffset = StatusLabel(self.page_toolLoadedNotRunning)
        self.statuslabel_zOffset.setGeometry(QtCore.QRect(5, 76, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset.setMinimumSize(QtCore.QSize(80, 30))
        self.statuslabel_zOffset.setMaximumSize(QtCore.QSize(70, 25))
        self.statuslabel_zOffset.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset.setObjectName("statuslabel_zOffset")
        self.statuslabel_zOffset_2 = StatusLabel(self.page_toolLoadedNotRunning)
        self.statuslabel_zOffset_2.setGeometry(QtCore.QRect(105, 76, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_2.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_2.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_2.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_2.setMaximumSize(QtCore.QSize(51, 30))
        self.statuslabel_zOffset_2.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_2.setObjectName("statuslabel_zOffset_2")
        self.frame_4 = QtWidgets.QFrame(self.page_toolLoadedNotRunning)
        self.frame_4.setGeometry(QtCore.QRect(5, 35, 241, 35))
        self.frame_4.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 76, 17))
        self.label_4.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(180, 10, 56, 17))
        self.label_5.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 66, 17))
        self.label_6.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.statuslabel_zOffset_8 = StatusLabel(self.page_toolLoadedNotRunning)
        self.statuslabel_zOffset_8.setGeometry(QtCore.QRect(185, 76, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_8.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_8.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_8.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_8.setMaximumSize(QtCore.QSize(60, 25))
        self.statuslabel_zOffset_8.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_8.setObjectName("statuslabel_zOffset_8")
        self.statuslabel_4 = StatusLabel(self.page_toolLoadedNotRunning)
        self.statuslabel_4.setGeometry(QtCore.QRect(5, 5, 241, 26))
        self.statuslabel_4.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_4.setObjectName("statuslabel_4")
        self.line = QtWidgets.QFrame(self.page_toolLoadedNotRunning)
        self.line.setGeometry(QtCore.QRect(5, 110, 241, 16))
        self.line.setStyleSheet("color: rgb(136, 138, 133)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.btnChangeTool = QtWidgets.QPushButton(self.page_toolLoadedNotRunning)
        self.btnChangeTool.setGeometry(QtCore.QRect(70, 135, 116, 40))
        self.btnChangeTool.setObjectName("btnChangeTool")
        self.stackedWidgetTool.addWidget(self.page_toolLoadedNotRunning)
        self.page_toolLoadedAndRunning = QtWidgets.QWidget()
        self.page_toolLoadedAndRunning.setObjectName("page_toolLoadedAndRunning")
        self.statuslabel_13 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_13.setGeometry(QtCore.QRect(175, 125, 66, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_13.sizePolicy().hasHeightForWidth())
        self.statuslabel_13.setSizePolicy(sizePolicy)
        self.statuslabel_13.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statuslabel_13.setObjectName("statuslabel_13")
        self.statuslabel_14 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_14.setGeometry(QtCore.QRect(175, 160, 66, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_14.sizePolicy().hasHeightForWidth())
        self.statuslabel_14.setSizePolicy(sizePolicy)
        self.statuslabel_14.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statuslabel_14.setObjectName("statuslabel_14")
        self.frame_6 = QtWidgets.QFrame(self.page_toolLoadedAndRunning)
        self.frame_6.setGeometry(QtCore.QRect(5, 35, 241, 35))
        self.frame_6.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(90, 10, 76, 17))
        self.label_9.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(180, 10, 56, 17))
        self.label_10.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 66, 17))
        self.label_11.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.statuslabel_zOffset_5 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_zOffset_5.setGeometry(QtCore.QRect(5, 76, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_5.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_5.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_5.setMinimumSize(QtCore.QSize(80, 30))
        self.statuslabel_zOffset_5.setMaximumSize(QtCore.QSize(70, 25))
        self.statuslabel_zOffset_5.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_5.setObjectName("statuslabel_zOffset_5")
        self.statuslabel_zOffset_6 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_zOffset_6.setGeometry(QtCore.QRect(105, 76, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_6.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_6.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_6.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_6.setMaximumSize(QtCore.QSize(51, 30))
        self.statuslabel_zOffset_6.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_6.setObjectName("statuslabel_zOffset_6")
        self.label_12 = QtWidgets.QLabel(self.page_toolLoadedAndRunning)
        self.label_12.setGeometry(QtCore.QRect(5, 165, 91, 17))
        self.label_12.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_12.setObjectName("label_12")
        self.statuslabel_7 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_7.setGeometry(QtCore.QRect(5, 5, 241, 26))
        self.statuslabel_7.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_7.setObjectName("statuslabel_7")
        self.line_2 = QtWidgets.QFrame(self.page_toolLoadedAndRunning)
        self.line_2.setGeometry(QtCore.QRect(5, 110, 241, 16))
        self.line_2.setStyleSheet("color: rgb(136, 138, 133)")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.statuslabel_zOffset_11 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_zOffset_11.setGeometry(QtCore.QRect(185, 76, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_11.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_11.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_11.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_11.setMaximumSize(QtCore.QSize(60, 25))
        self.statuslabel_zOffset_11.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_11.setObjectName("statuslabel_zOffset_11")
        self.label_13 = QtWidgets.QLabel(self.page_toolLoadedAndRunning)
        self.label_13.setGeometry(QtCore.QRect(5, 130, 91, 17))
        self.label_13.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_13.setObjectName("label_13")
        self.statuslabel_zOffset_12 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_zOffset_12.setGeometry(QtCore.QRect(105, 160, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_12.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_12.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_12.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_12.setMaximumSize(QtCore.QSize(60, 25))
        self.statuslabel_zOffset_12.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_12.setObjectName("statuslabel_zOffset_12")
        self.statuslabel_zOffset_13 = StatusLabel(self.page_toolLoadedAndRunning)
        self.statuslabel_zOffset_13.setGeometry(QtCore.QRect(105, 125, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_zOffset_13.sizePolicy().hasHeightForWidth())
        self.statuslabel_zOffset_13.setSizePolicy(sizePolicy)
        self.statuslabel_zOffset_13.setMinimumSize(QtCore.QSize(60, 30))
        self.statuslabel_zOffset_13.setMaximumSize(QtCore.QSize(60, 25))
        self.statuslabel_zOffset_13.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_zOffset_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_zOffset_13.setObjectName("statuslabel_zOffset_13")
        self.stackedWidgetTool.addWidget(self.page_toolLoadedAndRunning)
        self.frame_5 = QtWidgets.QFrame(self.page_mainScreen)
        self.frame_5.setGeometry(QtCore.QRect(5, 5, 426, 41))
        self.frame_5.setStyleSheet(".QFrame {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.statuslabel_17 = StatusLabel(self.frame_5)
        self.statuslabel_17.setEnabled(True)
        self.statuslabel_17.setGeometry(QtCore.QRect(60, 2, 360, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_17.sizePolicy().hasHeightForWidth())
        self.statuslabel_17.setSizePolicy(sizePolicy)
        self.statuslabel_17.setMinimumSize(QtCore.QSize(360, 0))
        self.statuslabel_17.setMaximumSize(QtCore.QSize(40, 16777215))
        self.statuslabel_17.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font: 75 12pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statuslabel_17.setWordWrap(True)
        self.statuslabel_17.setIndent(0)
        self.statuslabel_17.setProperty("statusItem", "")
        self.statuslabel_17.setObjectName("statuslabel_17")
        self.statuslabel_18 = StatusLabel(self.frame_5)
        self.statuslabel_18.setGeometry(QtCore.QRect(60, 22, 360, 21))
        self.statuslabel_18.setMinimumSize(QtCore.QSize(360, 0))
        self.statuslabel_18.setMaximumSize(QtCore.QSize(40, 16777215))
        self.statuslabel_18.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font: 75 12pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statuslabel_18.setWordWrap(True)
        self.statuslabel_18.setIndent(0)
        self.statuslabel_18.setProperty("statusItem", "")
        self.statuslabel_18.setObjectName("statuslabel_18")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 46, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font: 75 12pt \"Bebas Kai\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.iso_view_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.iso_view_button.setGeometry(QtCore.QRect(505, 10, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iso_view_button.sizePolicy().hasHeightForWidth())
        self.iso_view_button.setSizePolicy(sizePolicy)
        self.iso_view_button.setMinimumSize(QtCore.QSize(55, 35))
        self.iso_view_button.setMaximumSize(QtCore.QSize(60, 35))
        self.iso_view_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.iso_view_button.setStyleSheet("font-size: 12pt")
        self.iso_view_button.setCheckable(False)
        self.iso_view_button.setObjectName("iso_view_button")
        self.x_view_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.x_view_button.setGeometry(QtCore.QRect(505, 55, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_view_button.sizePolicy().hasHeightForWidth())
        self.x_view_button.setSizePolicy(sizePolicy)
        self.x_view_button.setMinimumSize(QtCore.QSize(55, 35))
        self.x_view_button.setMaximumSize(QtCore.QSize(60, 35))
        self.x_view_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_view_button.setStyleSheet("font-size: 12pt")
        self.x_view_button.setCheckable(False)
        self.x_view_button.setObjectName("x_view_button")
        self.y_view_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.y_view_button.setGeometry(QtCore.QRect(505, 100, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_view_button.sizePolicy().hasHeightForWidth())
        self.y_view_button.setSizePolicy(sizePolicy)
        self.y_view_button.setMinimumSize(QtCore.QSize(55, 35))
        self.y_view_button.setMaximumSize(QtCore.QSize(55, 35))
        self.y_view_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.y_view_button.setStyleSheet("font-size: 12pt")
        self.y_view_button.setCheckable(False)
        self.y_view_button.setObjectName("y_view_button")
        self.z_view_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.z_view_button.setGeometry(QtCore.QRect(505, 145, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_view_button.sizePolicy().hasHeightForWidth())
        self.z_view_button.setSizePolicy(sizePolicy)
        self.z_view_button.setMinimumSize(QtCore.QSize(55, 35))
        self.z_view_button.setMaximumSize(QtCore.QSize(60, 35))
        self.z_view_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_view_button.setStyleSheet("font-size: 12pt")
        self.z_view_button.setCheckable(False)
        self.z_view_button.setObjectName("z_view_button")
        self.pan_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.pan_button.setGeometry(QtCore.QRect(505, 200, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pan_button.sizePolicy().hasHeightForWidth())
        self.pan_button.setSizePolicy(sizePolicy)
        self.pan_button.setMinimumSize(QtCore.QSize(55, 35))
        self.pan_button.setMaximumSize(QtCore.QSize(60, 35))
        self.pan_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pan_button.setStyleSheet("QPushButton {\n"
"    font-size: 12pt;\n"
"    color: white;\n"
"    border-color: rgb(74, 77, 81);\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"/*QPushButton[error=\"true\"] {\n"
"    border-color: red;\n"
"}*/\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")
        self.pan_button.setCheckable(True)
        self.pan_button.setObjectName("pan_button")
        self.zoom_out_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.zoom_out_button.setGeometry(QtCore.QRect(505, 300, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_out_button.sizePolicy().hasHeightForWidth())
        self.zoom_out_button.setSizePolicy(sizePolicy)
        self.zoom_out_button.setMinimumSize(QtCore.QSize(55, 35))
        self.zoom_out_button.setMaximumSize(QtCore.QSize(60, 35))
        self.zoom_out_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zoom_out_button.setStyleSheet("font-size: 12pt")
        self.zoom_out_button.setCheckable(False)
        self.zoom_out_button.setObjectName("zoom_out_button")
        self.zoom_in_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.zoom_in_button.setGeometry(QtCore.QRect(505, 255, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_in_button.sizePolicy().hasHeightForWidth())
        self.zoom_in_button.setSizePolicy(sizePolicy)
        self.zoom_in_button.setMinimumSize(QtCore.QSize(55, 35))
        self.zoom_in_button.setMaximumSize(QtCore.QSize(60, 35))
        self.zoom_in_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zoom_in_button.setStyleSheet("font-size: 12pt")
        self.zoom_in_button.setCheckable(False)
        self.zoom_in_button.setObjectName("zoom_in_button")
        self.path_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.path_button.setGeometry(QtCore.QRect(505, 350, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_button.sizePolicy().hasHeightForWidth())
        self.path_button.setSizePolicy(sizePolicy)
        self.path_button.setMinimumSize(QtCore.QSize(55, 35))
        self.path_button.setMaximumSize(QtCore.QSize(60, 35))
        self.path_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.path_button.setStyleSheet("font-size: 12pt")
        self.path_button.setCheckable(False)
        self.path_button.setObjectName("path_button")
        self.clear_button = QtWidgets.QPushButton(self.page_mainScreen)
        self.clear_button.setGeometry(QtCore.QRect(505, 395, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(55, 35))
        self.clear_button.setMaximumSize(QtCore.QSize(60, 35))
        self.clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_button.setStyleSheet("font-size: 12pt")
        self.clear_button.setCheckable(False)
        self.clear_button.setObjectName("clear_button")
        self.stackedWidgetSliders = VCPStackedWidget(self.page_mainScreen)
        self.stackedWidgetSliders.setGeometry(QtCore.QRect(300, 440, 271, 301))
        self.stackedWidgetSliders.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetSliders.setObjectName("stackedWidgetSliders")
        self.page_jog_sliders = QtWidgets.QWidget()
        self.page_jog_sliders.setObjectName("page_jog_sliders")
        self.statuslabel_33 = StatusLabel(self.page_jog_sliders)
        self.statuslabel_33.setGeometry(QtCore.QRect(10, 90, 181, 21))
        self.statuslabel_33.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_33.setObjectName("statuslabel_33")
        self.settings_slider_3 = VCPSettingsSlider(self.page_jog_sliders)
        self.settings_slider_3.setGeometry(QtCore.QRect(5, 115, 256, 30))
        self.settings_slider_3.setMinimumSize(QtCore.QSize(0, 30))
        self.settings_slider_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settings_slider_3.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.settings_slider_3.setMinimum(0)
        self.settings_slider_3.setMaximum(100)
        self.settings_slider_3.setProperty("value", 50)
        self.settings_slider_3.setSliderPosition(50)
        self.settings_slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.settings_slider_3.setObjectName("settings_slider_3")
        self.statuslabel_32 = StatusLabel(self.page_jog_sliders)
        self.statuslabel_32.setGeometry(QtCore.QRect(10, 15, 246, 21))
        self.statuslabel_32.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_32.setObjectName("statuslabel_32")
        self.settings_slider_2 = VCPSettingsSlider(self.page_jog_sliders)
        self.settings_slider_2.setGeometry(QtCore.QRect(5, 40, 256, 30))
        self.settings_slider_2.setMinimumSize(QtCore.QSize(0, 30))
        self.settings_slider_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settings_slider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.settings_slider_2.setMinimum(0)
        self.settings_slider_2.setMaximum(100)
        self.settings_slider_2.setProperty("value", 50)
        self.settings_slider_2.setSliderPosition(50)
        self.settings_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.settings_slider_2.setObjectName("settings_slider_2")
        self.actionslider_spindle_override_2 = ActionSlider(self.page_jog_sliders)
        self.actionslider_spindle_override_2.setGeometry(QtCore.QRect(5, 260, 256, 30))
        self.actionslider_spindle_override_2.setMinimumSize(QtCore.QSize(0, 30))
        self.actionslider_spindle_override_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionslider_spindle_override_2.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_spindle_override_2.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_spindle_override_2.setObjectName("actionslider_spindle_override_2")
        self.actionbutton_36 = ActionButton(self.page_jog_sliders)
        self.actionbutton_36.setGeometry(QtCore.QRect(215, 230, 45, 30))
        self.actionbutton_36.setMinimumSize(QtCore.QSize(45, 30))
        self.actionbutton_36.setMaximumSize(QtCore.QSize(40, 30))
        self.actionbutton_36.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_36.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_36.setObjectName("actionbutton_36")
        self.statuslabel_2 = StatusLabel(self.page_jog_sliders)
        self.statuslabel_2.setGeometry(QtCore.QRect(10, 235, 171, 16))
        self.statuslabel_2.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_2.setObjectName("statuslabel_2")
        self.stackedWidgetSliders.addWidget(self.page_jog_sliders)
        self.page_all_sliders = QtWidgets.QWidget()
        self.page_all_sliders.setObjectName("page_all_sliders")
        self.actionbutton_max_velocity_reset_3 = ActionButton(self.page_all_sliders)
        self.actionbutton_max_velocity_reset_3.setGeometry(QtCore.QRect(220, 10, 40, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_max_velocity_reset_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_max_velocity_reset_3.setSizePolicy(sizePolicy)
        self.actionbutton_max_velocity_reset_3.setMinimumSize(QtCore.QSize(40, 30))
        self.actionbutton_max_velocity_reset_3.setMaximumSize(QtCore.QSize(40, 30))
        self.actionbutton_max_velocity_reset_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_max_velocity_reset_3.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_max_velocity_reset_3.setObjectName("actionbutton_max_velocity_reset_3")
        self.actionslider_max_velocity_3 = ActionSlider(self.page_all_sliders)
        self.actionslider_max_velocity_3.setGeometry(QtCore.QRect(5, 40, 256, 30))
        self.actionslider_max_velocity_3.setMinimumSize(QtCore.QSize(0, 30))
        self.actionslider_max_velocity_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionslider_max_velocity_3.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_max_velocity_3.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_max_velocity_3.setObjectName("actionslider_max_velocity_3")
        self.actionbutton_rapid_override_reset_3 = ActionButton(self.page_all_sliders)
        self.actionbutton_rapid_override_reset_3.setGeometry(QtCore.QRect(220, 85, 40, 30))
        self.actionbutton_rapid_override_reset_3.setMinimumSize(QtCore.QSize(40, 30))
        self.actionbutton_rapid_override_reset_3.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.actionbutton_rapid_override_reset_3.setFont(font)
        self.actionbutton_rapid_override_reset_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_rapid_override_reset_3.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_rapid_override_reset_3.setObjectName("actionbutton_rapid_override_reset_3")
        self.statuslabel_19 = StatusLabel(self.page_all_sliders)
        self.statuslabel_19.setGeometry(QtCore.QRect(10, 15, 181, 21))
        self.statuslabel_19.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_19.setObjectName("statuslabel_19")
        self.statuslabel_16 = StatusLabel(self.page_all_sliders)
        self.statuslabel_16.setGeometry(QtCore.QRect(10, 90, 171, 21))
        self.statuslabel_16.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_16.setObjectName("statuslabel_16")
        self.actionslider_feed_override_3 = ActionSlider(self.page_all_sliders)
        self.actionslider_feed_override_3.setGeometry(QtCore.QRect(5, 190, 256, 30))
        self.actionslider_feed_override_3.setMinimumSize(QtCore.QSize(0, 30))
        self.actionslider_feed_override_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionslider_feed_override_3.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_feed_override_3.setMaximum(100)
        self.actionslider_feed_override_3.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_feed_override_3.setObjectName("actionslider_feed_override_3")
        self.statuslabel_20 = StatusLabel(self.page_all_sliders)
        self.statuslabel_20.setGeometry(QtCore.QRect(10, 165, 171, 21))
        self.statuslabel_20.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_20.setObjectName("statuslabel_20")
        self.actionbutton_feed_override_reset_3 = ActionButton(self.page_all_sliders)
        self.actionbutton_feed_override_reset_3.setGeometry(QtCore.QRect(220, 160, 40, 30))
        self.actionbutton_feed_override_reset_3.setMinimumSize(QtCore.QSize(40, 30))
        self.actionbutton_feed_override_reset_3.setMaximumSize(QtCore.QSize(40, 30))
        self.actionbutton_feed_override_reset_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_feed_override_reset_3.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_feed_override_reset_3.setObjectName("actionbutton_feed_override_reset_3")
        self.actionslider_rapid_override_3 = ActionSlider(self.page_all_sliders)
        self.actionslider_rapid_override_3.setGeometry(QtCore.QRect(5, 115, 256, 30))
        self.actionslider_rapid_override_3.setMinimumSize(QtCore.QSize(0, 30))
        self.actionslider_rapid_override_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionslider_rapid_override_3.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_rapid_override_3.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_rapid_override_3.setObjectName("actionslider_rapid_override_3")
        self.actionbutton_32 = ActionButton(self.page_all_sliders)
        self.actionbutton_32.setGeometry(QtCore.QRect(220, 230, 40, 30))
        self.actionbutton_32.setMinimumSize(QtCore.QSize(40, 30))
        self.actionbutton_32.setMaximumSize(QtCore.QSize(40, 30))
        self.actionbutton_32.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_32.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_32.setObjectName("actionbutton_32")
        self.statuslabel = StatusLabel(self.page_all_sliders)
        self.statuslabel.setGeometry(QtCore.QRect(10, 235, 171, 16))
        self.statuslabel.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel.setObjectName("statuslabel")
        self.actionslider_spindle_override = ActionSlider(self.page_all_sliders)
        self.actionslider_spindle_override.setGeometry(QtCore.QRect(5, 260, 256, 30))
        self.actionslider_spindle_override.setMinimumSize(QtCore.QSize(0, 30))
        self.actionslider_spindle_override.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionslider_spindle_override.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 20px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.actionslider_spindle_override.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_spindle_override.setObjectName("actionslider_spindle_override")
        self.stackedWidgetSliders.addWidget(self.page_all_sliders)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_mainScreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(565, 5, 701, 426))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vtkbackplot = VTKBackPlot(self.verticalLayoutWidget)
        self.vtkbackplot.setObjectName("vtkbackplot")
        self.verticalLayout_2.addWidget(self.vtkbackplot)
        self.pushStatusButton = QtWidgets.QPushButton(self.page_mainScreen)
        self.pushStatusButton.setGeometry(QtCore.QRect(435, 5, 61, 41))
        self.pushStatusButton.setCheckable(True)
        self.pushStatusButton.setObjectName("pushStatusButton")
        self.stackedWidgetMain.addWidget(self.page_mainScreen)
        self.page_selectProgram = QtWidgets.QWidget()
        self.page_selectProgram.setObjectName("page_selectProgram")
        self.frame_35 = QtWidgets.QFrame(self.page_selectProgram)
        self.frame_35.setGeometry(QtCore.QRect(0, 5, 350, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_35.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_35.setStyleSheet(".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.horizontalLayout_124 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_124.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_124.setObjectName("horizontalLayout_124")
        self.folderUp_left = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderUp_left.sizePolicy().hasHeightForWidth())
        self.folderUp_left.setSizePolicy(sizePolicy)
        self.folderUp_left.setMinimumSize(QtCore.QSize(50, 30))
        self.folderUp_left.setMaximumSize(QtCore.QSize(50, 30))
        self.folderUp_left.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderUp_left.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/folder_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folderUp_left.setIcon(icon12)
        self.folderUp_left.setIconSize(QtCore.QSize(30, 17))
        self.folderUp_left.setObjectName("folderUp_left")
        self.horizontalLayout_124.addWidget(self.folderUp_left)
        self.pathComboBox = RemovableDeviceComboBox(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathComboBox.sizePolicy().hasHeightForWidth())
        self.pathComboBox.setSizePolicy(sizePolicy)
        self.pathComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.pathComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pathComboBox.setStyleSheet("QScrollBar:horizontal {\n"
"        min-width: 240px;\n"
"        height: 13px;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        min-height: 240px;\n"
"        width: 13px;\n"
"    }\n"
"\n"
"    QScrollBar::groove {\n"
"        background: gray;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QScrollBar::handle {\n"
"        background: blue;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        width: 25px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        height: 25px;\n"
"    }")
        self.pathComboBox.setObjectName("pathComboBox")
        self.horizontalLayout_124.addWidget(self.pathComboBox)
        self.device_eject_usb_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_eject_usb_button.sizePolicy().hasHeightForWidth())
        self.device_eject_usb_button.setSizePolicy(sizePolicy)
        self.device_eject_usb_button.setMinimumSize(QtCore.QSize(100, 30))
        self.device_eject_usb_button.setMaximumSize(QtCore.QSize(100, 30))
        self.device_eject_usb_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_eject_usb_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.device_eject_usb_button.setObjectName("device_eject_usb_button")
        self.horizontalLayout_124.addWidget(self.device_eject_usb_button)
        self.verticalLayout_37.addLayout(self.horizontalLayout_124)
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.filesystemtable_left = FileSystemTable(self.frame_35)
        self.filesystemtable_left.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.filesystemtable_left.setStyleSheet("FileSystemTable {\n"
"    color: black;\n"
"       border: 4px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius:none;\n"
"    border-style: none;\n"
"    font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable_left.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filesystemtable_left.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.filesystemtable_left.setShowGrid(False)
        self.filesystemtable_left.setSortingEnabled(True)
        self.filesystemtable_left.setProperty("tableType", FileSystemTable.Remote)
        self.filesystemtable_left.setObjectName("filesystemtable_left")
        self.filesystemtable_left.horizontalHeader().setDefaultSectionSize(180)
        self.filesystemtable_left.horizontalHeader().setMinimumSectionSize(28)
        self.filesystemtable_left.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_125.addWidget(self.filesystemtable_left)
        self.verticalLayout_37.addLayout(self.horizontalLayout_125)
        self.horizontalLayout_126 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_126.setObjectName("horizontalLayout_126")
        self.device_delete_item_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_delete_item_button.sizePolicy().hasHeightForWidth())
        self.device_delete_item_button.setSizePolicy(sizePolicy)
        self.device_delete_item_button.setMinimumSize(QtCore.QSize(80, 30))
        self.device_delete_item_button.setMaximumSize(QtCore.QSize(70, 30))
        self.device_delete_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_delete_item_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_delete_item_button.setIcon(icon13)
        self.device_delete_item_button.setIconSize(QtCore.QSize(14, 14))
        self.device_delete_item_button.setObjectName("device_delete_item_button")
        self.horizontalLayout_126.addWidget(self.device_delete_item_button)
        self.device_new_file_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_new_file_button.sizePolicy().hasHeightForWidth())
        self.device_new_file_button.setSizePolicy(sizePolicy)
        self.device_new_file_button.setMinimumSize(QtCore.QSize(80, 30))
        self.device_new_file_button.setMaximumSize(QtCore.QSize(70, 30))
        self.device_new_file_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_new_file_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.device_new_file_button.setIcon(icon8)
        self.device_new_file_button.setIconSize(QtCore.QSize(12, 16))
        self.device_new_file_button.setObjectName("device_new_file_button")
        self.horizontalLayout_126.addWidget(self.device_new_file_button)
        self.device_new_folder_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_new_folder_button.sizePolicy().hasHeightForWidth())
        self.device_new_folder_button.setSizePolicy(sizePolicy)
        self.device_new_folder_button.setMinimumSize(QtCore.QSize(80, 30))
        self.device_new_folder_button.setMaximumSize(QtCore.QSize(70, 30))
        self.device_new_folder_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_new_folder_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/new_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_new_folder_button.setIcon(icon14)
        self.device_new_folder_button.setIconSize(QtCore.QSize(28, 15))
        self.device_new_folder_button.setObjectName("device_new_folder_button")
        self.horizontalLayout_126.addWidget(self.device_new_folder_button)
        self.device_rename_item_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_rename_item_button.sizePolicy().hasHeightForWidth())
        self.device_rename_item_button.setSizePolicy(sizePolicy)
        self.device_rename_item_button.setMinimumSize(QtCore.QSize(80, 30))
        self.device_rename_item_button.setMaximumSize(QtCore.QSize(70, 30))
        self.device_rename_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_rename_item_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.device_rename_item_button.setObjectName("device_rename_item_button")
        self.horizontalLayout_126.addWidget(self.device_rename_item_button)
        self.verticalLayout_37.addLayout(self.horizontalLayout_126)
        self.frame_34 = QtWidgets.QFrame(self.page_selectProgram)
        self.frame_34.setGeometry(QtCore.QRect(410, 5, 350, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_34.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_34.setStyleSheet(".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.horizontalLayout_121 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_121.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_121.setObjectName("horizontalLayout_121")
        self.folderUp_right = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderUp_right.sizePolicy().hasHeightForWidth())
        self.folderUp_right.setSizePolicy(sizePolicy)
        self.folderUp_right.setMinimumSize(QtCore.QSize(50, 30))
        self.folderUp_right.setMaximumSize(QtCore.QSize(50, 30))
        self.folderUp_right.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderUp_right.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.folderUp_right.setIcon(icon12)
        self.folderUp_right.setIconSize(QtCore.QSize(30, 17))
        self.folderUp_right.setObjectName("folderUp_right")
        self.horizontalLayout_121.addWidget(self.folderUp_right)
        self.recentfilecombobox_2 = RecentFileComboBox(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentfilecombobox_2.sizePolicy().hasHeightForWidth())
        self.recentfilecombobox_2.setSizePolicy(sizePolicy)
        self.recentfilecombobox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.recentfilecombobox_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.recentfilecombobox_2.setObjectName("recentfilecombobox_2")
        self.horizontalLayout_121.addWidget(self.recentfilecombobox_2)
        self.verticalLayout_35.addLayout(self.horizontalLayout_121)
        self.horizontalLayout_122 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_122.setObjectName("horizontalLayout_122")
        self.filesystemtable_right = FileSystemTable(self.frame_34)
        self.filesystemtable_right.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.filesystemtable_right.setStyleSheet("FileSystemTable {\n"
"    color: black;\n"
"       border: 4px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius:none;\n"
"    border-style: none;\n"
"    font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable_right.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filesystemtable_right.setShowGrid(False)
        self.filesystemtable_right.setSortingEnabled(True)
        self.filesystemtable_right.setObjectName("filesystemtable_right")
        self.filesystemtable_right.horizontalHeader().setDefaultSectionSize(180)
        self.horizontalLayout_122.addWidget(self.filesystemtable_right)
        self.verticalLayout_35.addLayout(self.horizontalLayout_122)
        self.horizontalLayout_123 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_123.setObjectName("horizontalLayout_123")
        self.main_delete_item_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_delete_item_button.sizePolicy().hasHeightForWidth())
        self.main_delete_item_button.setSizePolicy(sizePolicy)
        self.main_delete_item_button.setMinimumSize(QtCore.QSize(80, 30))
        self.main_delete_item_button.setMaximumSize(QtCore.QSize(90, 30))
        self.main_delete_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_delete_item_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.main_delete_item_button.setIcon(icon13)
        self.main_delete_item_button.setIconSize(QtCore.QSize(14, 14))
        self.main_delete_item_button.setObjectName("main_delete_item_button")
        self.horizontalLayout_123.addWidget(self.main_delete_item_button)
        self.main_new_file_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_new_file_button.sizePolicy().hasHeightForWidth())
        self.main_new_file_button.setSizePolicy(sizePolicy)
        self.main_new_file_button.setMinimumSize(QtCore.QSize(80, 30))
        self.main_new_file_button.setMaximumSize(QtCore.QSize(100, 30))
        self.main_new_file_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_new_file_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.main_new_file_button.setIcon(icon8)
        self.main_new_file_button.setIconSize(QtCore.QSize(12, 16))
        self.main_new_file_button.setObjectName("main_new_file_button")
        self.horizontalLayout_123.addWidget(self.main_new_file_button)
        self.main_new_folder_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_new_folder_button.sizePolicy().hasHeightForWidth())
        self.main_new_folder_button.setSizePolicy(sizePolicy)
        self.main_new_folder_button.setMinimumSize(QtCore.QSize(80, 30))
        self.main_new_folder_button.setMaximumSize(QtCore.QSize(125, 30))
        self.main_new_folder_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_new_folder_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.main_new_folder_button.setIcon(icon14)
        self.main_new_folder_button.setIconSize(QtCore.QSize(28, 15))
        self.main_new_folder_button.setObjectName("main_new_folder_button")
        self.horizontalLayout_123.addWidget(self.main_new_folder_button)
        self.main_rename_item_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_rename_item_button.sizePolicy().hasHeightForWidth())
        self.main_rename_item_button.setSizePolicy(sizePolicy)
        self.main_rename_item_button.setMinimumSize(QtCore.QSize(80, 30))
        self.main_rename_item_button.setMaximumSize(QtCore.QSize(90, 30))
        self.main_rename_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_rename_item_button.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.main_rename_item_button.setObjectName("main_rename_item_button")
        self.horizontalLayout_123.addWidget(self.main_rename_item_button)
        self.verticalLayout_35.addLayout(self.horizontalLayout_123)
        self.layoutWidget_4 = QtWidgets.QWidget(self.page_selectProgram)
        self.layoutWidget_4.setGeometry(QtCore.QRect(350, 9, 61, 726))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_36.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_36.setContentsMargins(3, 100, 3, 100)
        self.verticalLayout_36.setSpacing(50)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.copy_to_right = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_to_right.sizePolicy().hasHeightForWidth())
        self.copy_to_right.setSizePolicy(sizePolicy)
        self.copy_to_right.setMinimumSize(QtCore.QSize(55, 90))
        self.copy_to_right.setMaximumSize(QtCore.QSize(55, 90))
        self.copy_to_right.setFocusPolicy(QtCore.Qt.NoFocus)
        self.copy_to_right.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.copy_to_right.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"    padding-right: 4px;\n"
"}")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/tall_right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_to_right.setIcon(icon15)
        self.copy_to_right.setIconSize(QtCore.QSize(18, 60))
        self.copy_to_right.setObjectName("copy_to_right")
        self.verticalLayout_36.addWidget(self.copy_to_right)
        self.copy_to_left = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_to_left.sizePolicy().hasHeightForWidth())
        self.copy_to_left.setSizePolicy(sizePolicy)
        self.copy_to_left.setMinimumSize(QtCore.QSize(55, 90))
        self.copy_to_left.setMaximumSize(QtCore.QSize(55, 90))
        self.copy_to_left.setFocusPolicy(QtCore.Qt.NoFocus)
        self.copy_to_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.copy_to_left.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"    padding-right: 8px;\n"
"}")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/tall_left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_to_left.setIcon(icon16)
        self.copy_to_left.setIconSize(QtCore.QSize(28, 60))
        self.copy_to_left.setObjectName("copy_to_left")
        self.verticalLayout_36.addWidget(self.copy_to_left)
        self.btnLoadGCode = QtWidgets.QPushButton(self.page_selectProgram)
        self.btnLoadGCode.setGeometry(QtCore.QRect(955, 695, 150, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoadGCode.sizePolicy().hasHeightForWidth())
        self.btnLoadGCode.setSizePolicy(sizePolicy)
        self.btnLoadGCode.setMinimumSize(QtCore.QSize(150, 35))
        self.btnLoadGCode.setMaximumSize(QtCore.QSize(100, 30))
        self.btnLoadGCode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnLoadGCode.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.btnLoadGCode.setObjectName("btnLoadGCode")
        self.frame_7 = QtWidgets.QFrame(self.page_selectProgram)
        self.frame_7.setGeometry(QtCore.QRect(770, 5, 491, 676))
        self.frame_7.setStyleSheet(".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.file_absolute_path = QtWidgets.QLabel(self.frame_7)
        self.file_absolute_path.setEnabled(True)
        self.file_absolute_path.setGeometry(QtCore.QRect(15, 15, 453, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_absolute_path.sizePolicy().hasHeightForWidth())
        self.file_absolute_path.setSizePolicy(sizePolicy)
        self.file_absolute_path.setMinimumSize(QtCore.QSize(300, 25))
        self.file_absolute_path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.file_absolute_path.setFont(font)
        self.file_absolute_path.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-color: transparent;\n"
"    color: black;\n"
"      background-color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"    padding-left: 6px;\n"
"}")
        self.file_absolute_path.setText("")
        self.file_absolute_path.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.file_absolute_path.setObjectName("file_absolute_path")
        self.gcodeeditor_initial = GcodeEditor(self.frame_7)
        self.gcodeeditor_initial.setGeometry(QtCore.QRect(10, 45, 471, 571))
        self.gcodeeditor_initial.setStyleSheet("")
        self.gcodeeditor_initial.setProperty("is_editor", True)
        self.gcodeeditor_initial.setObjectName("gcodeeditor_initial")
        self.layoutWidget = QtWidgets.QWidget(self.frame_7)
        self.layoutWidget.setGeometry(QtCore.QRect(35, 630, 420, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_130 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_130.setObjectName("horizontalLayout_130")
        self.edit_gcode_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_gcode_button_2.sizePolicy().hasHeightForWidth())
        self.edit_gcode_button_2.setSizePolicy(sizePolicy)
        self.edit_gcode_button_2.setMinimumSize(QtCore.QSize(100, 30))
        self.edit_gcode_button_2.setMaximumSize(QtCore.QSize(100, 30))
        self.edit_gcode_button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.edit_gcode_button_2.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.edit_gcode_button_2.setCheckable(True)
        self.edit_gcode_button_2.setObjectName("edit_gcode_button_2")
        self.horizontalLayout_130.addWidget(self.edit_gcode_button_2)
        self.find_replace_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_replace_button_2.sizePolicy().hasHeightForWidth())
        self.find_replace_button_2.setSizePolicy(sizePolicy)
        self.find_replace_button_2.setMinimumSize(QtCore.QSize(100, 30))
        self.find_replace_button_2.setMaximumSize(QtCore.QSize(100, 30))
        self.find_replace_button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.find_replace_button_2.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.find_replace_button_2.setObjectName("find_replace_button_2")
        self.horizontalLayout_130.addWidget(self.find_replace_button_2)
        self.save_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button_2.sizePolicy().hasHeightForWidth())
        self.save_button_2.setSizePolicy(sizePolicy)
        self.save_button_2.setMinimumSize(QtCore.QSize(100, 30))
        self.save_button_2.setMaximumSize(QtCore.QSize(100, 30))
        self.save_button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_button_2.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.save_button_2.setObjectName("save_button_2")
        self.horizontalLayout_130.addWidget(self.save_button_2)
        self.save_as_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_button_2.sizePolicy().hasHeightForWidth())
        self.save_as_button_2.setSizePolicy(sizePolicy)
        self.save_as_button_2.setMinimumSize(QtCore.QSize(100, 30))
        self.save_as_button_2.setMaximumSize(QtCore.QSize(100, 30))
        self.save_as_button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_as_button_2.setStyleSheet("QPushButton {\n"
"       font: 12pt \"Bebas Kai\";\n"
"}")
        self.save_as_button_2.setObjectName("save_as_button_2")
        self.horizontalLayout_130.addWidget(self.save_as_button_2)
        self.stackedWidgetMain.addWidget(self.page_selectProgram)
        self.page_offsetsScreen = QtWidgets.QWidget()
        self.page_offsetsScreen.setObjectName("page_offsetsScreen")
        self.probewizardwidget = ProbeWizardWidget(self.page_offsetsScreen)
        self.probewizardwidget.setGeometry(QtCore.QRect(5, 5, 1116, 641))
        self.probewizardwidget.setObjectName("probewizardwidget")
        self.stackedWidgetMain.addWidget(self.page_offsetsScreen)
        self.page_Settings = QtWidgets.QWidget()
        self.page_Settings.setObjectName("page_Settings")
        self.actionbutton_20 = ActionButton(self.page_Settings)
        self.actionbutton_20.setGeometry(QtCore.QRect(115, 105, 161, 41))
        self.actionbutton_20.setCheckable(True)
        self.actionbutton_20.setObjectName("actionbutton_20")
        self.actionbutton_21 = ActionButton(self.page_Settings)
        self.actionbutton_21.setGeometry(QtCore.QRect(115, 175, 166, 41))
        self.actionbutton_21.setObjectName("actionbutton_21")
        self.actionbutton_22 = ActionButton(self.page_Settings)
        self.actionbutton_22.setGeometry(QtCore.QRect(115, 225, 166, 41))
        self.actionbutton_22.setObjectName("actionbutton_22")
        self.actionbutton_23 = ActionButton(self.page_Settings)
        self.actionbutton_23.setGeometry(QtCore.QRect(115, 275, 166, 41))
        self.actionbutton_23.setObjectName("actionbutton_23")
        self.actionbutton_24 = ActionButton(self.page_Settings)
        self.actionbutton_24.setGeometry(QtCore.QRect(115, 325, 166, 41))
        self.actionbutton_24.setObjectName("actionbutton_24")
        self.actionbutton_25 = ActionButton(self.page_Settings)
        self.actionbutton_25.setGeometry(QtCore.QRect(355, 100, 166, 41))
        self.actionbutton_25.setObjectName("actionbutton_25")
        self.actionbutton_26 = ActionButton(self.page_Settings)
        self.actionbutton_26.setGeometry(QtCore.QRect(115, 375, 166, 41))
        self.actionbutton_26.setObjectName("actionbutton_26")
        self.actionbutton_27 = ActionButton(self.page_Settings)
        self.actionbutton_27.setGeometry(QtCore.QRect(115, 430, 166, 41))
        self.actionbutton_27.setObjectName("actionbutton_27")
        self.spindleWidget = VCPStackedWidget(self.page_Settings)
        self.spindleWidget.setGeometry(QtCore.QRect(805, 90, 251, 301))
        self.spindleWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.spindleWidget.setObjectName("spindleWidget")
        self.page_probeLoaded = QtWidgets.QWidget()
        self.page_probeLoaded.setObjectName("page_probeLoaded")
        self.spindleWidget.addWidget(self.page_probeLoaded)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.spindleWidget.addWidget(self.page_2)
        self.page_noToolLoaded = QtWidgets.QWidget()
        self.page_noToolLoaded.setObjectName("page_noToolLoaded")
        self.spindleWidget.addWidget(self.page_noToolLoaded)
        self.activegcodestable = ActiveGcodesTable(self.page_Settings)
        self.activegcodestable.setGeometry(QtCore.QRect(320, 220, 431, 451))
        self.activegcodestable.setObjectName("activegcodestable")
        self.stackedWidgetMain.addWidget(self.page_Settings)
        self.verticalLayout_3.addWidget(self.stackedWidgetMain)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.gridFrame1 = QtWidgets.QFrame(self.horizontalWidget)
        self.gridFrame1.setMinimumSize(QtCore.QSize(100, 0))
        self.gridFrame1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gridFrame1.setStyleSheet("")
        self.gridFrame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gridFrame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rightButtonsContainer = QtWidgets.QWidget(self.gridFrame1)
        self.rightButtonsContainer.setObjectName("rightButtonsContainer")
        self.btnManual = ActionButton(self.rightButtonsContainer)
        self.btnManual.setGeometry(QtCore.QRect(9, 220, 80, 50))
        self.btnManual.setCheckable(True)
        self.btnManual.setObjectName("btnManual")
        self.btnMdi = ActionButton(self.rightButtonsContainer)
        self.btnMdi.setGeometry(QtCore.QRect(10, 280, 80, 50))
        self.btnMdi.setCheckable(True)
        self.btnMdi.setObjectName("btnMdi")
        self.btnProgram = ActionButton(self.rightButtonsContainer)
        self.btnProgram.setGeometry(QtCore.QRect(10, 340, 80, 50))
        self.btnProgram.setCheckable(True)
        self.btnProgram.setObjectName("btnProgram")
        self.actionbutton = ActionButton(self.rightButtonsContainer)
        self.actionbutton.setGeometry(QtCore.QRect(10, 5, 80, 60))
        self.actionbutton.setCheckable(True)
        self.actionbutton.setObjectName("actionbutton")
        self.actionbutton_2 = ActionButton(self.rightButtonsContainer)
        self.actionbutton_2.setGeometry(QtCore.QRect(10, 70, 80, 60))
        self.actionbutton_2.setCheckable(True)
        self.actionbutton_2.setObjectName("actionbutton_2")
        self.actionbutton_4 = ActionButton(self.rightButtonsContainer)
        self.actionbutton_4.setGeometry(QtCore.QRect(10, 135, 80, 60))
        self.actionbutton_4.setObjectName("actionbutton_4")
        self.btnOffsets = ActionButton(self.rightButtonsContainer)
        self.btnOffsets.setGeometry(QtCore.QRect(10, 435, 80, 30))
        self.btnOffsets.setCheckable(True)
        self.btnOffsets.setObjectName("btnOffsets")
        self.btnTools = ActionButton(self.rightButtonsContainer)
        self.btnTools.setGeometry(QtCore.QRect(10, 480, 80, 30))
        self.btnTools.setCheckable(True)
        self.btnTools.setObjectName("btnTools")
        self.btnConversational = ActionButton(self.rightButtonsContainer)
        self.btnConversational.setGeometry(QtCore.QRect(10, 525, 80, 30))
        self.btnConversational.setObjectName("btnConversational")
        self.btnExit = ActionButton(self.rightButtonsContainer)
        self.btnExit.setGeometry(QtCore.QRect(10, 685, 80, 50))
        self.btnExit.setObjectName("btnExit")
        self.btnSettings = ActionButton(self.rightButtonsContainer)
        self.btnSettings.setGeometry(QtCore.QRect(10, 610, 80, 30))
        self.btnSettings.setCheckable(True)
        self.btnSettings.setObjectName("btnSettings")
        self.gridLayout_2.addWidget(self.rightButtonsContainer, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame1)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionFullscreen = QtWidgets.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName("actionFullscreen")

        self.retranslateUi(MainWindow)
        self.stackedWidgetMain.setCurrentIndex(1)
        self.stackedWidgetLeftTop.setCurrentIndex(3)
        self.stackedWidgetLeftBottom.setCurrentIndex(0)
        self.stackedWidgetSpindle.setCurrentIndex(0)
        self.stackedWidgetTool.setCurrentIndex(1)
        self.stackedWidgetSliders.setCurrentIndex(0)
        self.pathComboBox.setCurrentIndex(2)
        self.spindleWidget.setCurrentIndex(1)
        self.pathComboBox.currentDeviceEjectable['bool'].connect(self.device_eject_usb_button.setEnabled)
        self.pathComboBox.usbPresent['bool'].connect(self.device_eject_usb_button.setEnabled)
        self.pathComboBox.currentPathChanged['QString'].connect(self.filesystemtable_left.setRootPath)
        self.filesystemtable_left.transferFileRequest['QString'].connect(self.filesystemtable_right.transferFile)
        self.copy_to_right.clicked.connect(self.filesystemtable_left.doFileTransfer)
        self.filesystemtable_right.transferFileRequest['QString'].connect(self.filesystemtable_left.transferFile)
        self.copy_to_left.clicked.connect(self.filesystemtable_right.doFileTransfer)
        self.folderUp_left.clicked['bool'].connect(self.filesystemtable_left.viewParentDirectory)
        self.folderUp_right.clicked.connect(self.filesystemtable_right.viewParentDirectory)
        self.filesystemtable_left.rootChanged['QString'].connect(self.pathComboBox.setCurrentText)
        self.btnLoadGCode.clicked.connect(self.filesystemtable_right.loadSelectedFile)
        self.runMdiCommand.clicked.connect(self.mdiEntry.submit)
        self.filesystemtable_right.filePreviewText['QString'].connect(self.gcodeeditor_initial.setText)
        self.iso_view_button.clicked.connect(self.vtkbackplot.setViewP)
        self.x_view_button.clicked.connect(self.vtkbackplot.setViewX)
        self.y_view_button.clicked.connect(self.vtkbackplot.setViewY)
        self.z_view_button.clicked.connect(self.vtkbackplot.setViewZ)
        self.zoom_in_button.clicked.connect(self.vtkbackplot.zoomIn)
        self.zoom_out_button.clicked.connect(self.vtkbackplot.zoomOut)
        self.pan_button.toggled['bool'].connect(self.vtkbackplot.enable_panning)
        self.path_button.clicked.connect(self.vtkbackplot.setViewPath)
        self.clear_button.clicked.connect(self.vtkbackplot.clearLivePlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stackedWidgetMain.setProperty("rules", _translate("MainWindow", "[]"))
        self.tableWidget_2.setProperty("displayColumns", _translate("MainWindow", "TPZDR"))
        self.tool_table_delete_button.setText(_translate("MainWindow", "DELETE"))
        self.tool_table_add_tool_button.setText(_translate("MainWindow", "ADD TOOL"))
        self.tool_table_import_tool_button.setText(_translate("MainWindow", "IMPORT TOOL"))
        self.tool_table_export_tool_button.setText(_translate("MainWindow", "EXPORT TOOL"))
        self.tool_table_save_button.setText(_translate("MainWindow", "SAVE TABLE"))
        self.tool_table_reload_button.setText(_translate("MainWindow", "RELOAD TABLE"))
        self.label_50.setText(_translate("MainWindow", "TOOL LENGTH"))
        self.tool_length_6.setText(_translate("MainWindow", "0.0000"))
        self.tool_length_6.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length_6.setProperty("format", _translate("MainWindow", "{:.3f}"))
        self.label_51.setText(_translate("MainWindow", "DIAMETER"))
        self.tool_diameter_3.setText(_translate("MainWindow", "0.00"))
        self.tool_diameter_3.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.2f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]"))
        self.tool_diameter_3.setProperty("format", _translate("MainWindow", "{:.3f}"))
        self.tool_length_7.setText(_translate("MainWindow", "T0"))
        self.tool_length_7.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'T\' + ch[0]\", \"name\": \"current tool\"}]"))
        self.tool_length_7.setProperty("format", _translate("MainWindow", "{:.3f}"))
        self.tool_touch_off_button.setText(_translate("MainWindow", "TOUCH OFF CURRENT TOOL"))
        self.tool_touch_off_button.setProperty("filename", _translate("MainWindow", "tool_touch_off.ngc"))
        self.label_52.setText(_translate("MainWindow", "Touched"))
        self.stackedWidgetLeftTop.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}], \"property\": \"currentIndex\", \"expression\": \"0 if(ch[0] == 1) else (1 if(ch[0] == 3) else 2)\", \"name\": \"Selected Page\"}]"))
        self.y_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:y,pos"))
        self.z_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:z,pos"))
        self.x_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:x,neg"))
        self.y_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:y,neg"))
        self.x_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:x,pos"))
        self.a_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:a,neg"))
        self.a_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:a,pos"))
        self.z_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:z,neg"))
        self.pushButton_23.setText(_translate("MainWindow", "-"))
        self.pushButton_22.setText(_translate("MainWindow", "+"))
        self.pushButton_28.setText(_translate("MainWindow", "J"))
        self.pushButton_27.setText(_translate("MainWindow", "I"))
        self.pushButton_9.setText(_translate("MainWindow", "S"))
        self.pushButton_7.setText(_translate("MainWindow", "G"))
        self.pushButton_26.setText(_translate("MainWindow", "K"))
        self.pushButton_8.setText(_translate("MainWindow", "M"))
        self.pushButton_24.setText(_translate("MainWindow", "T"))
        self.pushButton_25.setText(_translate("MainWindow", "P"))
        self.runMdiCommand.setText(_translate("MainWindow", "Run"))
        self.mdiEntry.setPlaceholderText(_translate("MainWindow", "MDI Command"))
        self.runMdiCommand_2.setText(_translate("MainWindow", "<- Back"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_6.setText(_translate("MainWindow", "A"))
        self.pushButton_4.setText(_translate("MainWindow", "Y"))
        self.pushButton_5.setText(_translate("MainWindow", "Z"))
        self.pushButton_11.setText(_translate("MainWindow", "2"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_15.setText(_translate("MainWindow", "6"))
        self.pushButton_18.setText(_translate("MainWindow", "9"))
        self.pushButton_17.setText(_translate("MainWindow", "8"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_12.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_16.setText(_translate("MainWindow", "7"))
        self.pushButton_20.setText(_translate("MainWindow", "."))
        self.pushButton_19.setText(_translate("MainWindow", "0"))
        self.pushButton_29.setText(_translate("MainWindow", "q"))
        self.pushButton_30.setText(_translate("MainWindow", "H"))
        self.pushButton_31.setText(_translate("MainWindow", "L"))
        self.pushButton_32.setText(_translate("MainWindow", "D"))
        self.gcodeeditor_final.setProperty("backgroundcolor", _translate("MainWindow", "#d9dadb"))
        self.gcodeeditor_final.setProperty("marginbackgroundcolor", _translate("MainWindow", "#d9dadb"))
        self.change_program_button.setText(_translate("MainWindow", "Change"))
        self.reload_program_button.setText(_translate("MainWindow", "Reload"))
        self.stackedWidgetLeftBottom.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}, {\"url\": \"status:interp_state\", \"trigger\": true}], \"property\": \"currentIndex\", \"expression\": \"0 if(ch[0] == 1) else (1 if(ch[0] == 3) else (2 if(ch[1] == 1) else 3))\", \"name\": \"Selected Page\"}]"))
        self.actionbutton_9.setText(_translate("MainWindow", "Flood"))
        self.actionbutton_9.setProperty("actionName", _translate("MainWindow", "coolant.flood.toggle"))
        self.actionbutton_8.setText(_translate("MainWindow", "Mist"))
        self.actionbutton_8.setProperty("actionName", _translate("MainWindow", "coolant.mist.toggle"))
        self.actionbutton_6.setText(_translate("MainWindow", "STOP"))
        self.actionbutton_6.setProperty("actionName", _translate("MainWindow", "program.abort"))
        self.actionbutton_10.setText(_translate("MainWindow", "FEED HOLD"))
        self.actionbutton_10.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_10.setProperty("actionName", _translate("MainWindow", "program.pause"))
        self.actionbutton_11.setText(_translate("MainWindow", "Mist"))
        self.actionbutton_11.setProperty("actionName", _translate("MainWindow", "coolant.mist.toggle"))
        self.actionbutton_12.setText(_translate("MainWindow", "Flood"))
        self.actionbutton_12.setProperty("actionName", _translate("MainWindow", "coolant.flood.toggle"))
        self.actionbutton_18.setText(_translate("MainWindow", "Resume"))
        self.actionbutton_18.setProperty("actionName", _translate("MainWindow", "program.resume"))
        self.actionbutton_3.setText(_translate("MainWindow", "CYCLE START"))
        self.actionbutton_3.setProperty("actionName", _translate("MainWindow", "program.run"))
        self.actionbutton_13.setText(_translate("MainWindow", "Flood"))
        self.actionbutton_13.setProperty("actionName", _translate("MainWindow", "coolant.flood.toggle"))
        self.actionbutton_7.setText(_translate("MainWindow", "STOP"))
        self.actionbutton_7.setProperty("actionName", _translate("MainWindow", "program.abort"))
        self.actionbutton_14.setText(_translate("MainWindow", "Mist"))
        self.actionbutton_14.setProperty("actionName", _translate("MainWindow", "coolant.mist.toggle"))
        self.actionbutton_15.setText(_translate("MainWindow", "Pause"))
        self.actionbutton_15.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_15.setProperty("actionName", _translate("MainWindow", "program.pause"))
        self.actionbutton_16.setText(_translate("MainWindow", "Single Block"))
        self.actionbutton_16.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_16.setProperty("actionName", _translate("MainWindow", "program.step"))
        self.actionbutton_19.setText(_translate("MainWindow", "RUN FM HERE"))
        self.actionbutton_19.setProperty("actionName", _translate("MainWindow", "program.run-from-line"))
        self.actionbutton_17.setText(_translate("MainWindow", "Resume"))
        self.actionbutton_17.setProperty("actionName", _translate("MainWindow", "program.resume"))
        self.actionbutton_5.setText(_translate("MainWindow", "M01 BREAK"))
        self.actionbutton_5.setProperty("actionName", _translate("MainWindow", "program.optional-stop.toggle"))
        self.statuslabel_23.setText(_translate("MainWindow", "AXIS"))
        self.statuslabel_23.setProperty("rules", _translate("MainWindow", "[]"))
        self.statuslabel_24.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \' POS\'\\n\", \"name\": \"WCS Header\"}]"))
        self.work_column_header_9.setText(_translate("MainWindow", "MACHINE"))
        self.dtg_column_header_4.setText(_translate("MainWindow", "DTG"))
        self.statuslabel_25.setText(_translate("MainWindow", "REF"))
        self.statuslabel_25.setProperty("rules", _translate("MainWindow", "[]"))
        self.zero_x_button_3.setText(_translate("MainWindow", "X"))
        self.zero_x_button_3.setProperty("rules", _translate("MainWindow", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_x_button_3.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} X0.0"))
        self.dro_entry_main_x.setText(_translate("MainWindow", "-0000.000"))
        self.drolabel_15.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_15.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_15.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_15.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_16.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_16.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_16.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_16.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_6.setText(_translate("MainWindow", "REF X"))
        self.axisactionbutton_6.setProperty("actionName", _translate("MainWindow", "machine.home.axis:x"))
        self.zero_y_button_5.setText(_translate("MainWindow", "Y"))
        self.zero_y_button_5.setProperty("rules", _translate("MainWindow", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_y_button_5.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} Y0.0"))
        self.dro_entry_main_y_2.setText(_translate("MainWindow", "   0.0000"))
        self.drolabel_19.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_19.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_19.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_19.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_20.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_20.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_20.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_20.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_4.setText(_translate("MainWindow", "REF Y"))
        self.axisactionbutton_4.setProperty("actionName", _translate("MainWindow", "machine.home.axis:y"))
        self.zero_z_button_3.setText(_translate("MainWindow", "Z"))
        self.zero_z_button_3.setProperty("rules", _translate("MainWindow", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_z_button_3.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} Z0.0"))
        self.dro_entry_main_z.setText(_translate("MainWindow", "   0.0000"))
        self.drolabel_21.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_21.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_21.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_21.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_22.setText(_translate("MainWindow", "     0.000"))
        self.drolabel_22.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_22.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_22.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton.setText(_translate("MainWindow", "REF Z"))
        self.axisactionbutton.setProperty("actionName", _translate("MainWindow", "machine.home.axis:z"))
        self.zero_a_button_3.setText(_translate("MainWindow", "A"))
        self.zero_a_button_3.setProperty("rules", _translate("MainWindow", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_a_button_3.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} A0.0"))
        self.dro_entry_main_a.setText(_translate("MainWindow", "      0.00"))
        self.drolabel_23.setText(_translate("MainWindow", "      0.00"))
        self.drolabel_23.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_23.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_23.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_24.setText(_translate("MainWindow", "      0.00"))
        self.drolabel_24.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_24.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_24.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.button_a_goto_zero.setText(_translate("MainWindow", "GO TO 0"))
        self.button_a_goto_zero.setProperty("MDICommand", _translate("MainWindow", "G0 A0.0"))
        self.stackedWidgetSpindle.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:spindle.0.speed\", \"trigger\": true}], \"property\": \"currentIndex\", \"expression\": \"0 if ch[0] == 0 else 1\", \"name\": \"Spindle Status\"}]"))
        self.ref_coilumn_header_5.setText(_translate("MainWindow", "S"))
        self.spindleSpeed.setText(_translate("MainWindow", "0"))
        self.spindleSpeed.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:settings?speed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(int(ch[0]))\", \"name\": \"Default spindle speed\"}]"))
        self.spindleFwdButton.setText(_translate("MainWindow", "FWD"))
        self.spindleFwdButton.setProperty("MDICommand", _translate("MainWindow", "S#<spindleSpeed>M3"))
        self.spindleFwdButton_2.setText(_translate("MainWindow", "REV"))
        self.spindleFwdButton_2.setProperty("MDICommand", _translate("MainWindow", "S#<spindleSpeed>M4"))
        self.spindle_stop_button.setText(_translate("MainWindow", "STOP"))
        self.spindle_stop_button.setProperty("actionName", _translate("MainWindow", "spindle.off"))
        self.spindle_load_indicator.setProperty("format", _translate("MainWindow", "Spindle Load: {p}%"))
        self.statuslabel_6.setText(_translate("MainWindow", "0"))
        self.statuslabel_6.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:spindle.0.speed\", \"trigger\": true}, {\"url\": \"status:spindle.0.override\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.0f}\\\".format(ch[0] * ch[1])\", \"name\": \"Speed\"}]"))
        self.statuslabel_6.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.work_column_header_10.setText(_translate("MainWindow", "Spindle RPM"))
        self.stackedWidgetTool.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}, {\"url\": \"status:spindle.0.speed\", \"trigger\": true}], \"property\": \"currentIndex\", \"expression\": \"0 if ch[0] == 0 else (1 if ch[1]  == 0 else 2)\", \"name\": \"Selected Index\"}]"))
        self.ref_coilumn_header_4.setText(_translate("MainWindow", "T"))
        self.tool_number_entry.setText(_translate("MainWindow", "0"))
        self.tool_number_entry.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == \'On\' and ch[1] == \'Idle\'\", \"name\": \"enable/disable\"}]"))
        self.m6g43.setText(_translate("MainWindow", "M6 G43"))
        self.m6g43.setProperty("MDICommand", _translate("MainWindow", "M6 T#<tool_number_entry> G43"))
        self.statuslabel_zOffset.setText(_translate("MainWindow", "0.000"))
        self.statuslabel_zOffset.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0])\", \"name\": \"Z Offset\"}]"))
        self.statuslabel_zOffset.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.statuslabel_zOffset_2.setText(_translate("MainWindow", "0.00"))
        self.statuslabel_zOffset_2.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.2f}\\\".format(ch[0])\", \"name\": \"Diameter\"}]"))
        self.statuslabel_zOffset_2.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.label_4.setText(_translate("MainWindow", "Diameter"))
        self.label_5.setText(_translate("MainWindow", "Flutes"))
        self.label_6.setText(_translate("MainWindow", "Z Offset"))
        self.statuslabel_zOffset_8.setText(_translate("MainWindow", "0"))
        self.statuslabel_zOffset_8.setProperty("rules", _translate("MainWindow", "[]"))
        self.statuslabel_zOffset_8.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.statuslabel_4.setText(_translate("MainWindow", "T 0 : No Tool Loaded"))
        self.statuslabel_4.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}, {\"url\": \"tooltable:current_tool?remark\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\'T \' + (str(ch[0])) + \\\" : \\\" + ch[1]\", \"name\": \"Tool Number & comment\"}]"))
        self.btnChangeTool.setText(_translate("MainWindow", "Change Tool"))
        self.statuslabel_13.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:linear_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \\\"/min\\\"\", \"name\": \"Units\"}]"))
        self.statuslabel_14.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:linear_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \\\"/flute\\\"\", \"name\": \"Units\"}]"))
        self.label_9.setText(_translate("MainWindow", "Diameter"))
        self.label_10.setText(_translate("MainWindow", "Flutes"))
        self.label_11.setText(_translate("MainWindow", "Z Offset"))
        self.statuslabel_zOffset_5.setText(_translate("MainWindow", "0.000"))
        self.statuslabel_zOffset_5.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0])\", \"name\": \"Z Offset\"}]"))
        self.statuslabel_zOffset_5.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.statuslabel_zOffset_6.setText(_translate("MainWindow", "0.00"))
        self.statuslabel_zOffset_6.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.2f}\\\".format(ch[0])\", \"name\": \"Diameter\"}]"))
        self.statuslabel_zOffset_6.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.label_12.setText(_translate("MainWindow", "Chip Load"))
        self.statuslabel_7.setText(_translate("MainWindow", "T 0 : No Tool Loaded"))
        self.statuslabel_7.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}, {\"url\": \"tooltable:current_tool?remark\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\'T \' + (str(ch[0])) + \\\" : \\\" + ch[1]\", \"name\": \"Tool Number & comment\"}]"))
        self.statuslabel_zOffset_11.setText(_translate("MainWindow", "0"))
        self.statuslabel_zOffset_11.setProperty("rules", _translate("MainWindow", "[]"))
        self.statuslabel_zOffset_11.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.label_13.setText(_translate("MainWindow", "Feed Rate"))
        self.statuslabel_zOffset_12.setText(_translate("MainWindow", "0.00"))
        self.statuslabel_zOffset_12.setProperty("rules", _translate("MainWindow", "[]"))
        self.statuslabel_zOffset_12.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.statuslabel_zOffset_13.setText(_translate("MainWindow", "0.0"))
        self.statuslabel_zOffset_13.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:current_vel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'%.1f\' % (ch[0] * 60)\", \"name\": \"Current Feedrate\"}]"))
        self.statuslabel_zOffset_13.setProperty("format", _translate("MainWindow", "{:.0f}"))
        self.statuslabel_17.setText(_translate("MainWindow", "G0   G0   G0"))
        self.statuslabel_17.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:gcodes\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'   \'.join(map(str, ch[0]))\", \"name\": \"Active Codes\"}]"))
        self.statuslabel_18.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:mcodes\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'   \'.join(map(str, ch[0]))\", \"name\": \"Active Mcodes\"}]"))
        self.label_3.setText(_translate("MainWindow", "Active\n"
"Codes"))
        self.iso_view_button.setText(_translate("MainWindow", "ISO VIEW"))
        self.x_view_button.setText(_translate("MainWindow", "X View"))
        self.y_view_button.setText(_translate("MainWindow", "Y View"))
        self.z_view_button.setText(_translate("MainWindow", "Z View"))
        self.pan_button.setText(_translate("MainWindow", "PAN"))
        self.zoom_out_button.setText(_translate("MainWindow", "ZOOM -"))
        self.zoom_in_button.setText(_translate("MainWindow", "ZOOM +"))
        self.path_button.setText(_translate("MainWindow", "Path"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.stackedWidgetSliders.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}], \"property\": \"currentIndex\", \"expression\": \"0 if ch[0] == 1 else 1\", \"name\": \"Selected Page\"}]"))
        self.statuslabel_33.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"settings:machine.jog.angular-speed\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\'Angular Jog Speed: {:.0f}\'.format(ch[0])\", \"name\": \"Angular Jog Speed\"}]"))
        self.settings_slider_3.setProperty("settingName", _translate("MainWindow", "machine.jog.angular-speed-percentage"))
        self.statuslabel_32.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"settings:machine.jog.linear-speed\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\'Linear Jog Speed: {:.0f}\'.format(ch[0]) +\\\" \\\"+ ch[1] + \'/min\'\", \"name\": \"Linear Jog Speed\"}]"))
        self.settings_slider_2.setProperty("settingName", _translate("MainWindow", "machine.jog.linear-speed-percentage"))
        self.actionslider_spindle_override_2.setProperty("actionName", _translate("MainWindow", "spindle.override"))
        self.actionbutton_36.setText(_translate("MainWindow", "Reset"))
        self.actionbutton_36.setProperty("actionName", _translate("MainWindow", "spindle.override.reset"))
        self.statuslabel_2.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:spindle.0.override\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'Spindle Override: {:.0%}\'.format(ch[0])\", \"name\": \"Spindle Override Text\"}]"))
        self.actionbutton_max_velocity_reset_3.setText(_translate("MainWindow", "reset"))
        self.actionbutton_max_velocity_reset_3.setProperty("actionName", _translate("MainWindow", "machine.max-velocity.reset"))
        self.actionslider_max_velocity_3.setProperty("actionName", _translate("MainWindow", "machine.max-velocity.set"))
        self.actionbutton_rapid_override_reset_3.setText(_translate("MainWindow", "Reset"))
        self.actionbutton_rapid_override_reset_3.setProperty("actionName", _translate("MainWindow", "machine.rapid-override.reset"))
        self.statuslabel_19.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:max_velocity\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\'Max Velocity: {:.0f}\'.format(ch[0] * 60)\", \"name\": \"Max Velocity Text\"}]"))
        self.statuslabel_16.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:rapidrate\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'Rapid Override: {:.0%}\'.format(ch[0])\", \"name\": \"Rapid Override Text\"}]"))
        self.actionslider_feed_override_3.setProperty("actionName", _translate("MainWindow", "machine.feed-override.set"))
        self.statuslabel_20.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:feedrate\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'Feed Override: {:.0%}\'.format(ch[0])\", \"name\": \"Feed Override Text\"}]"))
        self.actionbutton_feed_override_reset_3.setText(_translate("MainWindow", "reset"))
        self.actionbutton_feed_override_reset_3.setProperty("actionName", _translate("MainWindow", "machine.feed-override.reset"))
        self.actionslider_rapid_override_3.setProperty("actionName", _translate("MainWindow", "machine.rapid-override.set"))
        self.actionbutton_32.setText(_translate("MainWindow", "Reset"))
        self.actionbutton_32.setProperty("actionName", _translate("MainWindow", "spindle.override.reset"))
        self.statuslabel.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:spindle.0.override\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'Spindle Override: {:.0%}\'.format(ch[0])\", \"name\": \"Spindle Override Text\"}]"))
        self.actionslider_spindle_override.setProperty("actionName", _translate("MainWindow", "spindle.override"))
        self.pushStatusButton.setText(_translate("MainWindow", "Status"))
        self.folderUp_left.setText(_translate("MainWindow", " UP"))
        self.device_eject_usb_button.setText(_translate("MainWindow", "EJECT USB"))
        self.filesystemtable_left.setProperty("hiddenColumns", _translate("MainWindow", "1,2"))
        self.device_delete_item_button.setText(_translate("MainWindow", " DELETE"))
        self.device_new_file_button.setText(_translate("MainWindow", " +FILE"))
        self.device_new_folder_button.setText(_translate("MainWindow", " + FOLDER"))
        self.device_rename_item_button.setText(_translate("MainWindow", "RENAME"))
        self.folderUp_right.setText(_translate("MainWindow", " UP"))
        self.filesystemtable_right.setProperty("hiddenColumns", _translate("MainWindow", "1,2"))
        self.main_delete_item_button.setText(_translate("MainWindow", " DELETE"))
        self.main_new_file_button.setText(_translate("MainWindow", " NEW FILE"))
        self.main_new_folder_button.setText(_translate("MainWindow", " NEW FOLDER"))
        self.main_rename_item_button.setText(_translate("MainWindow", "RENAME"))
        self.copy_to_right.setText(_translate("MainWindow", "COPY\n"
"TO\n"
"RIGHT"))
        self.copy_to_left.setText(_translate("MainWindow", "COPY\n"
"TO\n"
"LEFT"))
        self.btnLoadGCode.setText(_translate("MainWindow", "LOAD G-CODE"))
        self.gcodeeditor_initial.setProperty("backgroundcolor", _translate("MainWindow", "#d9dadb"))
        self.gcodeeditor_initial.setProperty("marginbackgroundcolor", _translate("MainWindow", "#d9dadb"))
        self.edit_gcode_button_2.setText(_translate("MainWindow", "EDIT G-CODE"))
        self.find_replace_button_2.setText(_translate("MainWindow", "FIND/REPLACE"))
        self.save_button_2.setText(_translate("MainWindow", "SAVE"))
        self.save_as_button_2.setText(_translate("MainWindow", "SAVE AS"))
        self.actionbutton_20.setText(_translate("MainWindow", "Virtual Keyboard"))
        self.actionbutton_20.setProperty("actionName", _translate("MainWindow", "settings.virtual-input.enable"))
        self.actionbutton_21.setText(_translate("MainWindow", "Hal Show"))
        self.actionbutton_21.setProperty("actionName", _translate("MainWindow", "tool.halshow"))
        self.actionbutton_22.setText(_translate("MainWindow", "Hal Meter"))
        self.actionbutton_22.setProperty("actionName", _translate("MainWindow", "tool.halmeter"))
        self.actionbutton_23.setText(_translate("MainWindow", "Hal Scope"))
        self.actionbutton_23.setProperty("actionName", _translate("MainWindow", "tool.halscope"))
        self.actionbutton_24.setText(_translate("MainWindow", "Classic Ladder"))
        self.actionbutton_24.setProperty("actionName", _translate("MainWindow", "tool.classicladder"))
        self.actionbutton_25.setText(_translate("MainWindow", "Simulated Probe"))
        self.actionbutton_25.setProperty("actionName", _translate("MainWindow", "tool.simulate_probe"))
        self.actionbutton_26.setText(_translate("MainWindow", "LCNC Status"))
        self.actionbutton_26.setProperty("actionName", _translate("MainWindow", "tool.status"))
        self.actionbutton_27.setText(_translate("MainWindow", "Calibration"))
        self.actionbutton_27.setProperty("actionName", _translate("MainWindow", "tool.calibration"))
        self.btnManual.setText(_translate("MainWindow", "Manual"))
        self.btnManual.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 1\", \"name\": \"Manual Mode ON\"}]"))
        self.btnManual.setProperty("actionName", _translate("MainWindow", "machine.mode.manual"))
        self.btnMdi.setText(_translate("MainWindow", "MDI"))
        self.btnMdi.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 3\", \"name\": \"Mode MDI On\"}]"))
        self.btnMdi.setProperty("actionName", _translate("MainWindow", "machine.mode.mdi"))
        self.btnProgram.setText(_translate("MainWindow", "Program"))
        self.btnProgram.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 2\", \"name\": \"Auto Mode ON\"}]"))
        self.btnProgram.setProperty("actionName", _translate("MainWindow", "machine.mode.auto"))
        self.actionbutton.setText(_translate("MainWindow", "E-Stop"))
        self.actionbutton.setProperty("actionName", _translate("MainWindow", "machine.estop.toggle"))
        self.actionbutton_2.setText(_translate("MainWindow", "Power\n"
"ON"))
        self.actionbutton_2.setProperty("actionName", _translate("MainWindow", "machine.power.toggle"))
        self.actionbutton_4.setText(_translate("MainWindow", "Home\n"
"All"))
        self.actionbutton_4.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'Homed\' if ch[0] else \'Home\\\\nAll\'\", \"name\": \"Button text\"}, {\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Style Sheet\", \"expression\": \"\'background-color:rgb(138, 226, 52)\' if ch[0]else \'\'\", \"name\": \"New Rule\"}]"))
        self.actionbutton_4.setProperty("actionName", _translate("MainWindow", "machine.home.all"))
        self.btnOffsets.setText(_translate("MainWindow", "Offsets"))
        self.btnTools.setText(_translate("MainWindow", "Tools"))
        self.btnConversational.setText(_translate("MainWindow", "Convers"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionOPEN.setText(_translate("MainWindow", "oPEN"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "F11"))

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.containers.stack import VCPStackedWidget
from qtpyvcp.widgets.display_widgets.active_gcodes_table import ActiveGcodesTable
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.notification_widget import NotificationWidget
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.display_widgets.vtk_backplot.vtk_backplot import VTKBackPlot
from qtpyvcp.widgets.hal_widgets.hal_bar_indicator import HalBarIndicator
from qtpyvcp.widgets.hal_widgets.hal_led import HalLedIndicator
from qtpyvcp.widgets.input_widgets.action_slider import ActionSlider
from qtpyvcp.widgets.input_widgets.dro_line_edit import DROLineEdit
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable, RemovableDeviceComboBox
from qtpyvcp.widgets.input_widgets.gcode_editor import GcodeEditor
from qtpyvcp.widgets.input_widgets.jog_increment import JogIncrementWidget
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.recent_file_combobox import RecentFileComboBox
from qtpyvcp.widgets.input_widgets.setting_slider import VCPSettingsSlider
from qtpyvcp.widgets.input_widgets.tool_table import ToolTable
from widgets.probe_wizard_widget import ProbeWizardWidget
import resources_rc
