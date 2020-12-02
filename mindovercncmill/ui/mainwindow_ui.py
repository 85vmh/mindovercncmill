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
        self.horizontalLayout.setContentsMargins(1, 2, 1, 0)
        self.horizontalLayout.setSpacing(2)
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
        self.stackedWidgetMain.setObjectName("stackedWidgetMain")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.frame_2 = QtWidgets.QFrame(self.page_1)
        self.frame_2.setGeometry(QtCore.QRect(400, 390, 501, 331))
        self.frame_2.setStyleSheet(".QFrame {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.widget_52 = QtWidgets.QWidget(self.frame_2)
        self.widget_52.setGeometry(QtCore.QRect(10, 0, 481, 320))
        self.widget_52.setObjectName("widget_52")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.widget_52)
        self.verticalLayout_56.setContentsMargins(0, 6, 0, 2)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_77.setSpacing(8)
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.frame_43 = QtWidgets.QFrame(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_43.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.horizontalLayout_144.setContentsMargins(15, -1, 20, -1)
        self.horizontalLayout_144.setSpacing(8)
        self.horizontalLayout_144.setObjectName("horizontalLayout_144")
        self.statuslabel_23 = StatusLabel(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_23.sizePolicy().hasHeightForWidth())
        self.statuslabel_23.setSizePolicy(sizePolicy)
        self.statuslabel_23.setMinimumSize(QtCore.QSize(60, 17))
        self.statuslabel_23.setMaximumSize(QtCore.QSize(60, 17))
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
        self.statuslabel_24.setMinimumSize(QtCore.QSize(100, 17))
        self.statuslabel_24.setMaximumSize(QtCore.QSize(100, 17))
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
        self.dtg_column_header_4.setMinimumSize(QtCore.QSize(100, 17))
        self.dtg_column_header_4.setMaximumSize(QtCore.QSize(100, 17))
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
        self.x_axis_dro_layout_2 = QtWidgets.QHBoxLayout()
        self.x_axis_dro_layout_2.setContentsMargins(1, 1, 1, 1)
        self.x_axis_dro_layout_2.setSpacing(7)
        self.x_axis_dro_layout_2.setObjectName("x_axis_dro_layout_2")
        self.zero_x_button_4 = MDIButton(self.widget_52)
        self.zero_x_button_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_x_button_4.sizePolicy().hasHeightForWidth())
        self.zero_x_button_4.setSizePolicy(sizePolicy)
        self.zero_x_button_4.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_x_button_4.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_x_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_x_button_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zero_x_button_4.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zero_x_button_4.setIcon(icon)
        self.zero_x_button_4.setIconSize(QtCore.QSize(20, 20))
        self.zero_x_button_4.setObjectName("zero_x_button_4")
        self.x_axis_dro_layout_2.addWidget(self.zero_x_button_4)
        self.drowidget_4 = DROWidget(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drowidget_4.sizePolicy().hasHeightForWidth())
        self.drowidget_4.setSizePolicy(sizePolicy)
        self.drowidget_4.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_4.setMaximumSize(QtCore.QSize(100, 35))
        self.drowidget_4.setStyleSheet("QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_4.setProperty("referenceType", DROWidget.Relative)
        self.drowidget_4.setObjectName("drowidget_4")
        self.x_axis_dro_layout_2.addWidget(self.drowidget_4)
        self.drolabel_7 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_7.sizePolicy().hasHeightForWidth())
        self.drolabel_7.setSizePolicy(sizePolicy)
        self.drolabel_7.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_7.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_7.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_7.setProperty("referenceType", 0)
        self.drolabel_7.setProperty("axisNumber", 0)
        self.drolabel_7.setProperty("latheMode", 0)
        self.drolabel_7.setObjectName("drolabel_7")
        self.x_axis_dro_layout_2.addWidget(self.drolabel_7)
        self.drolabel_8 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_8.sizePolicy().hasHeightForWidth())
        self.drolabel_8.setSizePolicy(sizePolicy)
        self.drolabel_8.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_8.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_8.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_8.setProperty("referenceType", 2)
        self.drolabel_8.setProperty("axisNumber", 0)
        self.drolabel_8.setProperty("latheMode", 0)
        self.drolabel_8.setObjectName("drolabel_8")
        self.x_axis_dro_layout_2.addWidget(self.drolabel_8)
        self.axisactionbutton_9 = ActionButton(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_9.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_9.setSizePolicy(sizePolicy)
        self.axisactionbutton_9.setMinimumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_9.setMaximumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_9.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_9.setObjectName("axisactionbutton_9")
        self.x_axis_dro_layout_2.addWidget(self.axisactionbutton_9)
        self.verticalLayout_56.addLayout(self.x_axis_dro_layout_2)
        self.y_axis_dro_layout_2 = QtWidgets.QHBoxLayout()
        self.y_axis_dro_layout_2.setContentsMargins(1, 1, 1, 1)
        self.y_axis_dro_layout_2.setSpacing(7)
        self.y_axis_dro_layout_2.setObjectName("y_axis_dro_layout_2")
        self.zero_y_button_4 = MDIButton(self.widget_52)
        self.zero_y_button_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_y_button_4.sizePolicy().hasHeightForWidth())
        self.zero_y_button_4.setSizePolicy(sizePolicy)
        self.zero_y_button_4.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_y_button_4.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_y_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_y_button_4.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_y_button_4.setIcon(icon)
        self.zero_y_button_4.setIconSize(QtCore.QSize(20, 20))
        self.zero_y_button_4.setObjectName("zero_y_button_4")
        self.y_axis_dro_layout_2.addWidget(self.zero_y_button_4)
        self.drowidget_5 = DROWidget(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drowidget_5.sizePolicy().hasHeightForWidth())
        self.drowidget_5.setSizePolicy(sizePolicy)
        self.drowidget_5.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_5.setMaximumSize(QtCore.QSize(100, 35))
        self.drowidget_5.setStyleSheet("QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_5.setProperty("referenceType", DROWidget.Relative)
        self.drowidget_5.setProperty("axis", DROWidget.Y)
        self.drowidget_5.setObjectName("drowidget_5")
        self.y_axis_dro_layout_2.addWidget(self.drowidget_5)
        self.drolabel_9 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_9.sizePolicy().hasHeightForWidth())
        self.drolabel_9.setSizePolicy(sizePolicy)
        self.drolabel_9.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_9.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_9.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_9.setProperty("referenceType", 0)
        self.drolabel_9.setProperty("axisNumber", 1)
        self.drolabel_9.setProperty("latheMode", 0)
        self.drolabel_9.setObjectName("drolabel_9")
        self.y_axis_dro_layout_2.addWidget(self.drolabel_9)
        self.drolabel_10 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_10.sizePolicy().hasHeightForWidth())
        self.drolabel_10.setSizePolicy(sizePolicy)
        self.drolabel_10.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_10.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_10.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_10.setProperty("referenceType", 2)
        self.drolabel_10.setProperty("axisNumber", 1)
        self.drolabel_10.setProperty("latheMode", 0)
        self.drolabel_10.setObjectName("drolabel_10")
        self.y_axis_dro_layout_2.addWidget(self.drolabel_10)
        self.axisactionbutton_5 = ActionButton(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_5.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_5.setSizePolicy(sizePolicy)
        self.axisactionbutton_5.setMinimumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_5.setMaximumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_5.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_5.setObjectName("axisactionbutton_5")
        self.y_axis_dro_layout_2.addWidget(self.axisactionbutton_5)
        self.verticalLayout_56.addLayout(self.y_axis_dro_layout_2)
        self.z_axis_dro_layout_2 = QtWidgets.QHBoxLayout()
        self.z_axis_dro_layout_2.setContentsMargins(1, 1, 1, 1)
        self.z_axis_dro_layout_2.setSpacing(7)
        self.z_axis_dro_layout_2.setObjectName("z_axis_dro_layout_2")
        self.zero_z_button_4 = MDIButton(self.widget_52)
        self.zero_z_button_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_z_button_4.sizePolicy().hasHeightForWidth())
        self.zero_z_button_4.setSizePolicy(sizePolicy)
        self.zero_z_button_4.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_z_button_4.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_z_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_z_button_4.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_z_button_4.setIcon(icon)
        self.zero_z_button_4.setIconSize(QtCore.QSize(20, 20))
        self.zero_z_button_4.setObjectName("zero_z_button_4")
        self.z_axis_dro_layout_2.addWidget(self.zero_z_button_4)
        self.drowidget_6 = DROWidget(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drowidget_6.sizePolicy().hasHeightForWidth())
        self.drowidget_6.setSizePolicy(sizePolicy)
        self.drowidget_6.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_6.setMaximumSize(QtCore.QSize(100, 35))
        self.drowidget_6.setStyleSheet("QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_6.setProperty("referenceType", DROWidget.Relative)
        self.drowidget_6.setProperty("axis", DROWidget.Z)
        self.drowidget_6.setObjectName("drowidget_6")
        self.z_axis_dro_layout_2.addWidget(self.drowidget_6)
        self.drolabel_11 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_11.sizePolicy().hasHeightForWidth())
        self.drolabel_11.setSizePolicy(sizePolicy)
        self.drolabel_11.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_11.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_11.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_11.setProperty("referenceType", 0)
        self.drolabel_11.setProperty("axisNumber", 2)
        self.drolabel_11.setProperty("latheMode", 0)
        self.drolabel_11.setObjectName("drolabel_11")
        self.z_axis_dro_layout_2.addWidget(self.drolabel_11)
        self.drolabel_12 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_12.sizePolicy().hasHeightForWidth())
        self.drolabel_12.setSizePolicy(sizePolicy)
        self.drolabel_12.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_12.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_12.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_12.setProperty("referenceType", 2)
        self.drolabel_12.setProperty("axisNumber", 2)
        self.drolabel_12.setProperty("latheMode", 0)
        self.drolabel_12.setObjectName("drolabel_12")
        self.z_axis_dro_layout_2.addWidget(self.drolabel_12)
        self.axisactionbutton_7 = ActionButton(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_7.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_7.setSizePolicy(sizePolicy)
        self.axisactionbutton_7.setMinimumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_7.setMaximumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_7.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_7.setObjectName("axisactionbutton_7")
        self.z_axis_dro_layout_2.addWidget(self.axisactionbutton_7)
        self.verticalLayout_56.addLayout(self.z_axis_dro_layout_2)
        self.a_axis_dro_layout_2 = QtWidgets.QHBoxLayout()
        self.a_axis_dro_layout_2.setContentsMargins(1, 1, 1, 1)
        self.a_axis_dro_layout_2.setSpacing(7)
        self.a_axis_dro_layout_2.setObjectName("a_axis_dro_layout_2")
        self.zero_a_button_4 = MDIButton(self.widget_52)
        self.zero_a_button_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_a_button_4.sizePolicy().hasHeightForWidth())
        self.zero_a_button_4.setSizePolicy(sizePolicy)
        self.zero_a_button_4.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_a_button_4.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_a_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_a_button_4.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_a_button_4.setIcon(icon)
        self.zero_a_button_4.setIconSize(QtCore.QSize(20, 20))
        self.zero_a_button_4.setObjectName("zero_a_button_4")
        self.a_axis_dro_layout_2.addWidget(self.zero_a_button_4)
        self.drowidget_7 = DROWidget(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drowidget_7.sizePolicy().hasHeightForWidth())
        self.drowidget_7.setSizePolicy(sizePolicy)
        self.drowidget_7.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_7.setMaximumSize(QtCore.QSize(100, 35))
        self.drowidget_7.setStyleSheet("QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_7.setProperty("referenceType", DROWidget.Relative)
        self.drowidget_7.setProperty("axis", DROWidget.A)
        self.drowidget_7.setObjectName("drowidget_7")
        self.a_axis_dro_layout_2.addWidget(self.drowidget_7)
        self.drolabel_13 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_13.sizePolicy().hasHeightForWidth())
        self.drolabel_13.setSizePolicy(sizePolicy)
        self.drolabel_13.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_13.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_13.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_13.setProperty("referenceType", 0)
        self.drolabel_13.setProperty("axisNumber", 3)
        self.drolabel_13.setProperty("latheMode", 0)
        self.drolabel_13.setObjectName("drolabel_13")
        self.a_axis_dro_layout_2.addWidget(self.drolabel_13)
        self.drolabel_14 = DROLabel(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_14.sizePolicy().hasHeightForWidth())
        self.drolabel_14.setSizePolicy(sizePolicy)
        self.drolabel_14.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_14.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_14.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_14.setProperty("referenceType", 2)
        self.drolabel_14.setProperty("axisNumber", 3)
        self.drolabel_14.setProperty("latheMode", 0)
        self.drolabel_14.setObjectName("drolabel_14")
        self.a_axis_dro_layout_2.addWidget(self.drolabel_14)
        self.axisactionbutton_8 = ActionButton(self.widget_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_8.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_8.setSizePolicy(sizePolicy)
        self.axisactionbutton_8.setMinimumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_8.setMaximumSize(QtCore.QSize(62, 40))
        self.axisactionbutton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.axisactionbutton_8.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_8.setObjectName("axisactionbutton_8")
        self.a_axis_dro_layout_2.addWidget(self.axisactionbutton_8)
        self.verticalLayout_56.addLayout(self.a_axis_dro_layout_2)
        self.stackedWidgetJogMdi = VCPStackedWidget(self.page_1)
        self.stackedWidgetJogMdi.setGeometry(QtCore.QRect(0, 0, 551, 381))
        self.stackedWidgetJogMdi.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetJogMdi.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidgetJogMdi.setObjectName("stackedWidgetJogMdi")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(410, 10, 131, 361))
        self.groupBox.setObjectName("groupBox")
        self.jogincrement = JogIncrementWidget(self.groupBox)
        self.jogincrement.setGeometry(QtCore.QRect(10, 40, 115, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jogincrement.sizePolicy().hasHeightForWidth())
        self.jogincrement.setSizePolicy(sizePolicy)
        self.jogincrement.setMinimumSize(QtCore.QSize(115, 300))
        self.jogincrement.setMaximumSize(QtCore.QSize(115, 400))
        self.jogincrement.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"\n"
"}\n"
"\n"
"")
        self.jogincrement.setProperty("diameter", 0)
        self.jogincrement.setOrientation(QtCore.Qt.Vertical)
        self.jogincrement.setLayoutSpacing(10)
        self.jogincrement.setObjectName("jogincrement")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 381, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 361, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.settings_slider = VCPSettingsSlider(self.layoutWidget)
        self.settings_slider.setMinimumSize(QtCore.QSize(0, 50))
        self.settings_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settings_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
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
        self.settings_slider.setMinimum(0)
        self.settings_slider.setMaximum(100)
        self.settings_slider.setProperty("value", 50)
        self.settings_slider.setSliderPosition(50)
        self.settings_slider.setOrientation(QtCore.Qt.Horizontal)
        self.settings_slider.setObjectName("settings_slider")
        self.horizontalLayout_84.addWidget(self.settings_slider)
        self.fr_override_dro_2 = StatusLabel(self.layoutWidget)
        self.fr_override_dro_2.setMinimumSize(QtCore.QSize(48, 38))
        self.fr_override_dro_2.setMaximumSize(QtCore.QSize(48, 38))
        self.fr_override_dro_2.setStyleSheet("StatusLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.fr_override_dro_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_override_dro_2.setObjectName("fr_override_dro_2")
        self.horizontalLayout_84.addWidget(self.fr_override_dro_2)
        self.gridWidget_2 = QtWidgets.QWidget(self.page_3)
        self.gridWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 271))
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.y_plus_jogbutton = ActionButton(self.gridWidget_2)
        self.y_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.y_plus_jogbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/y_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_plus_jogbutton.setIcon(icon1)
        self.y_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_plus_jogbutton.setObjectName("y_plus_jogbutton")
        self.gridLayout_4.addWidget(self.y_plus_jogbutton, 0, 2, 1, 1)
        self.z_plus_jogbutton = ActionButton(self.gridWidget_2)
        self.z_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_plus_jogbutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/z_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_plus_jogbutton.setIcon(icon2)
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
        self.x_minus_jogbutton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/x_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_minus_jogbutton.setIcon(icon3)
        self.x_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_minus_jogbutton.setObjectName("x_minus_jogbutton")
        self.gridLayout_4.addWidget(self.x_minus_jogbutton, 1, 1, 1, 1)
        
        
        self.x_plus_jogbutton = ActionButton(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_plus_jogbutton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/x_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_plus_jogbutton.setIcon(icon4)
        self.x_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_plus_jogbutton.setObjectName("x_plus_jogbutton")
        self.gridLayout_4.addWidget(self.x_plus_jogbutton, 1, 3, 1, 1)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/y_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_minus_jogbutton.setIcon(icon5)
        self.y_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_minus_jogbutton.setObjectName("y_minus_jogbutton")
        self.gridLayout_4.addWidget(self.y_minus_jogbutton, 3, 2, 1, 1)
        self.z_minus_jogbutton = ActionButton(self.gridWidget_2)
        self.z_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_minus_jogbutton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/z_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_minus_jogbutton.setIcon(icon6)
        self.z_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.z_minus_jogbutton.setObjectName("z_minus_jogbutton")
        self.gridLayout_4.addWidget(self.z_minus_jogbutton, 3, 0, 1, 1)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/a_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_plus_jogbutton.setIcon(icon7)
        self.a_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_plus_jogbutton.setObjectName("a_plus_jogbutton")
        self.gridLayout_4.addWidget(self.a_plus_jogbutton, 0, 4, 1, 1)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/a_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_minus_jogbutton.setIcon(icon8)
        self.a_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_minus_jogbutton.setObjectName("a_minus_jogbutton")
        self.gridLayout_4.addWidget(self.a_minus_jogbutton, 3, 4, 1, 1)
        self.stackedWidgetJogMdi.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridFrame1 = QtWidgets.QFrame(self.page_4)
        self.gridFrame1.setGeometry(QtCore.QRect(10, 10, 531, 361))
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_19 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 7, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_3.addWidget(self.pushButton_13, 5, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 4, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_3.addWidget(self.pushButton_15, 5, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 4, 5, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_3.addWidget(self.pushButton_14, 5, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 0, 5, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 6, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 7, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 7, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_3.addWidget(self.pushButton_16, 6, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_3.addWidget(self.pushButton_17, 6, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_3.addWidget(self.pushButton_23, 7, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 1, 5, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_3.addWidget(self.pushButton_18, 6, 2, 1, 1)
        self.mdientry = MDIEntry(self.gridFrame1)
        self.mdientry.setObjectName("mdientry")
        self.gridLayout_3.addWidget(self.mdientry, 0, 1, 1, 4)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 1, 6, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_3.addWidget(self.pushButton_24, 4, 6, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_3.addWidget(self.pushButton_25, 5, 5, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_3.addWidget(self.pushButton_26, 5, 6, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_3.addWidget(self.pushButton_27, 6, 5, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridFrame1)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_3.addWidget(self.pushButton_28, 6, 6, 1, 1)
        self.stackedWidgetJogMdi.addWidget(self.page_4)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidgetJogMdi.addWidget(self.page_8)
        self.frame_3 = QtWidgets.QFrame(self.page_1)
        self.frame_3.setGeometry(QtCore.QRect(560, 0, 701, 381))
        self.frame_3.setStyleSheet(".QFrame {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.vtkbackplot = VTKBackPlot(self.frame_3)
        self.vtkbackplot.setGeometry(QtCore.QRect(3, 3, 694, 374))
        self.vtkbackplot.setStyleSheet(".VTKBackPlot {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"}")
        self.vtkbackplot.setObjectName("vtkbackplot")
        self.stackedWidgetLeftActions = VCPStackedWidget(self.page_1)
        self.stackedWidgetLeftActions.setGeometry(QtCore.QRect(0, 390, 391, 331))
        self.stackedWidgetLeftActions.setStyleSheet(".VCPStackedWidget {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}")
        self.stackedWidgetLeftActions.setObjectName("stackedWidgetLeftActions")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.actionbutton_9 = ActionButton(self.page_5)
        self.actionbutton_9.setGeometry(QtCore.QRect(210, 20, 130, 42))
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
        self.actionbutton_8.setGeometry(QtCore.QRect(40, 20, 130, 42))
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
        self.stackedWidgetLeftActions.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.actionbutton_6 = ActionButton(self.page_6)
        self.actionbutton_6.setGeometry(QtCore.QRect(200, 90, 130, 42))
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
        self.actionbutton_10.setGeometry(QtCore.QRect(30, 90, 130, 42))
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
        self.actionbutton_11.setGeometry(QtCore.QRect(30, 20, 130, 42))
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
        self.actionbutton_12.setGeometry(QtCore.QRect(200, 20, 130, 42))
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
        self.stackedWidgetLeftActions.addWidget(self.page_6)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.actionbutton_3 = ActionButton(self.page)
        self.actionbutton_3.setGeometry(QtCore.QRect(40, 60, 308, 52))
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
        self.stackedWidgetLeftActions.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.actionbutton_13 = ActionButton(self.page_7)
        self.actionbutton_13.setGeometry(QtCore.QRect(210, 20, 130, 42))
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
        self.actionbutton_7.setGeometry(QtCore.QRect(210, 80, 130, 42))
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
        self.actionbutton_14.setGeometry(QtCore.QRect(30, 20, 130, 42))
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
        self.actionbutton_15.setGeometry(QtCore.QRect(30, 80, 130, 42))
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
        self.actionbutton_16.setGeometry(QtCore.QRect(30, 140, 130, 42))
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
        self.actionbutton_17 = ActionButton(self.page_7)
        self.actionbutton_17.setGeometry(QtCore.QRect(90, 200, 200, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_17.sizePolicy().hasHeightForWidth())
        self.actionbutton_17.setSizePolicy(sizePolicy)
        self.actionbutton_17.setMinimumSize(QtCore.QSize(200, 42))
        self.actionbutton_17.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_17.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_17.setCheckable(True)
        self.actionbutton_17.setObjectName("actionbutton_17")
        self.actionbutton_18 = ActionButton(self.page_7)
        self.actionbutton_18.setGeometry(QtCore.QRect(90, 260, 200, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_18.sizePolicy().hasHeightForWidth())
        self.actionbutton_18.setSizePolicy(sizePolicy)
        self.actionbutton_18.setMinimumSize(QtCore.QSize(200, 42))
        self.actionbutton_18.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.actionbutton_18.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_18.setCheckable(True)
        self.actionbutton_18.setObjectName("actionbutton_18")
        self.actionbutton_19 = ActionButton(self.page_7)
        self.actionbutton_19.setGeometry(QtCore.QRect(210, 140, 130, 42))
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
        self.stackedWidgetLeftActions.addWidget(self.page_7)
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setGeometry(QtCore.QRect(910, 390, 341, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 211, 42))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_97 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_97.setSpacing(9)
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.frame_28 = QtWidgets.QFrame(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 38))
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
        self.tool_number_entry_main_panel_2 = VCPLineEdit(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_number_entry_main_panel_2.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_main_panel_2.setSizePolicy(sizePolicy)
        self.tool_number_entry_main_panel_2.setMinimumSize(QtCore.QSize(55, 0))
        self.tool_number_entry_main_panel_2.setMaximumSize(QtCore.QSize(55, 16777215))
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
        self.tool_number_entry_main_panel_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tool_number_entry_main_panel_2.setFont(font)
        self.tool_number_entry_main_panel_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tool_number_entry_main_panel_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tool_number_entry_main_panel_2.setStyleSheet("font: 17pt;")
        self.tool_number_entry_main_panel_2.setFrame(True)
        self.tool_number_entry_main_panel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_number_entry_main_panel_2.setObjectName("tool_number_entry_main_panel_2")
        self.horizontalLayout_106.addWidget(self.tool_number_entry_main_panel_2)
        self.horizontalLayout_97.addWidget(self.frame_28)
        self.m6_tool_call_button_main_panel_2 = SubCallButton(self.layoutWidget_3)
        self.m6_tool_call_button_main_panel_2.setMinimumSize(QtCore.QSize(70, 40))
        self.m6_tool_call_button_main_panel_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.m6_tool_call_button_main_panel_2.setStyleSheet("QPushButton {\n"
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
        self.m6_tool_call_button_main_panel_2.setObjectName("m6_tool_call_button_main_panel_2")
        self.horizontalLayout_97.addWidget(self.m6_tool_call_button_main_panel_2)
        self.statuslabel = StatusLabel(self.frame)
        self.statuslabel.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.statuslabel.setObjectName("statuslabel")
        self.statuslabel_3 = StatusLabel(self.frame)
        self.statuslabel_3.setGeometry(QtCore.QRect(10, 110, 321, 17))
        self.statuslabel_3.setObjectName("statuslabel_3")
        self.statuslabel_2 = StatusLabel(self.frame)
        self.statuslabel_2.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.statuslabel_2.setObjectName("statuslabel_2")
        self.frame_4 = QtWidgets.QFrame(self.page_1)
        self.frame_4.setGeometry(QtCore.QRect(910, 560, 341, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 100, 292, 48))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_86.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.spindle_rev_button = ActionButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_rev_button.sizePolicy().hasHeightForWidth())
        self.spindle_rev_button.setSizePolicy(sizePolicy)
        self.spindle_rev_button.setMinimumSize(QtCore.QSize(100, 42))
        self.spindle_rev_button.setMaximumSize(QtCore.QSize(100, 42))
        self.spindle_rev_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_rev_button.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/ccw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spindle_rev_button.setIcon(icon9)
        self.spindle_rev_button.setIconSize(QtCore.QSize(18, 18))
        self.spindle_rev_button.setProperty("option", True)
        self.spindle_rev_button.setObjectName("spindle_rev_button")
        self.horizontalLayout_86.addWidget(self.spindle_rev_button)
        self.spindle_stop_button = ActionButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_stop_button.sizePolicy().hasHeightForWidth())
        self.spindle_stop_button.setSizePolicy(sizePolicy)
        self.spindle_stop_button.setMinimumSize(QtCore.QSize(90, 42))
        self.spindle_stop_button.setMaximumSize(QtCore.QSize(90, 42))
        self.spindle_stop_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_stop_button.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_stop_button.setProperty("option", True)
        self.spindle_stop_button.setObjectName("spindle_stop_button")
        self.horizontalLayout_86.addWidget(self.spindle_stop_button)
        self.spindle_fwd_button = ActionButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_fwd_button.sizePolicy().hasHeightForWidth())
        self.spindle_fwd_button.setSizePolicy(sizePolicy)
        self.spindle_fwd_button.setMinimumSize(QtCore.QSize(100, 42))
        self.spindle_fwd_button.setMaximumSize(QtCore.QSize(100, 42))
        self.spindle_fwd_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_fwd_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spindle_fwd_button.setStyleSheet("QPushButton {\n"
"    text-align: right;\n"
"    padding-right: 22px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/cw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spindle_fwd_button.setIcon(icon10)
        self.spindle_fwd_button.setIconSize(QtCore.QSize(18, 18))
        self.spindle_fwd_button.setProperty("option", True)
        self.spindle_fwd_button.setObjectName("spindle_fwd_button")
        self.horizontalLayout_86.addWidget(self.spindle_fwd_button)
        self.frame_29 = QtWidgets.QFrame(self.frame_4)
        self.frame_29.setGeometry(QtCore.QRect(20, 30, 121, 38))
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
        self.tool_number_entry_main_panel_3 = VCPLineEdit(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_number_entry_main_panel_3.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_main_panel_3.setSizePolicy(sizePolicy)
        self.tool_number_entry_main_panel_3.setMinimumSize(QtCore.QSize(70, 0))
        self.tool_number_entry_main_panel_3.setMaximumSize(QtCore.QSize(55, 16777215))
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
        self.tool_number_entry_main_panel_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tool_number_entry_main_panel_3.setFont(font)
        self.tool_number_entry_main_panel_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tool_number_entry_main_panel_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tool_number_entry_main_panel_3.setStyleSheet("font: 17pt;")
        self.tool_number_entry_main_panel_3.setFrame(True)
        self.tool_number_entry_main_panel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_number_entry_main_panel_3.setObjectName("tool_number_entry_main_panel_3")
        self.horizontalLayout_107.addWidget(self.tool_number_entry_main_panel_3)
        self.stackedWidgetMain.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_35 = QtWidgets.QFrame(self.page_2)
        self.frame_35.setGeometry(QtCore.QRect(0, 0, 500, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_35.setMaximumSize(QtCore.QSize(500, 16777215))
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
        self.device_folder_up_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_folder_up_button.sizePolicy().hasHeightForWidth())
        self.device_folder_up_button.setSizePolicy(sizePolicy)
        self.device_folder_up_button.setMinimumSize(QtCore.QSize(110, 30))
        self.device_folder_up_button.setMaximumSize(QtCore.QSize(110, 30))
        self.device_folder_up_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_folder_up_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/folder_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_folder_up_button.setIcon(icon11)
        self.device_folder_up_button.setIconSize(QtCore.QSize(30, 17))
        self.device_folder_up_button.setObjectName("device_folder_up_button")
        self.horizontalLayout_124.addWidget(self.device_folder_up_button)
        self.removabledevicecombobox = RemovableDeviceComboBox(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removabledevicecombobox.sizePolicy().hasHeightForWidth())
        self.removabledevicecombobox.setSizePolicy(sizePolicy)
        self.removabledevicecombobox.setMinimumSize(QtCore.QSize(0, 30))
        self.removabledevicecombobox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.removabledevicecombobox.setObjectName("removabledevicecombobox")
        self.horizontalLayout_124.addWidget(self.removabledevicecombobox)
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
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.device_eject_usb_button.setObjectName("device_eject_usb_button")
        self.horizontalLayout_124.addWidget(self.device_eject_usb_button)
        self.verticalLayout_37.addLayout(self.horizontalLayout_124)
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.filesystemtable_2 = FileSystemTable(self.frame_35)
        self.filesystemtable_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.filesystemtable_2.setStyleSheet("FileSystemTable {\n"
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
        self.filesystemtable_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filesystemtable_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.filesystemtable_2.setShowGrid(False)
        self.filesystemtable_2.setObjectName("filesystemtable_2")
        self.horizontalLayout_125.addWidget(self.filesystemtable_2)
        self.verticalLayout_37.addLayout(self.horizontalLayout_125)
        self.horizontalLayout_126 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_126.setObjectName("horizontalLayout_126")
        self.device_delete_item_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_delete_item_button.sizePolicy().hasHeightForWidth())
        self.device_delete_item_button.setSizePolicy(sizePolicy)
        self.device_delete_item_button.setMinimumSize(QtCore.QSize(90, 30))
        self.device_delete_item_button.setMaximumSize(QtCore.QSize(90, 30))
        self.device_delete_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_delete_item_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_delete_item_button.setIcon(icon12)
        self.device_delete_item_button.setIconSize(QtCore.QSize(14, 14))
        self.device_delete_item_button.setObjectName("device_delete_item_button")
        self.horizontalLayout_126.addWidget(self.device_delete_item_button)
        self.device_new_file_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_new_file_button.sizePolicy().hasHeightForWidth())
        self.device_new_file_button.setSizePolicy(sizePolicy)
        self.device_new_file_button.setMinimumSize(QtCore.QSize(100, 30))
        self.device_new_file_button.setMaximumSize(QtCore.QSize(100, 30))
        self.device_new_file_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_new_file_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/new_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_new_file_button.setIcon(icon13)
        self.device_new_file_button.setIconSize(QtCore.QSize(12, 16))
        self.device_new_file_button.setObjectName("device_new_file_button")
        self.horizontalLayout_126.addWidget(self.device_new_file_button)
        self.device_new_folder_button = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_new_folder_button.sizePolicy().hasHeightForWidth())
        self.device_new_folder_button.setSizePolicy(sizePolicy)
        self.device_new_folder_button.setMinimumSize(QtCore.QSize(125, 30))
        self.device_new_folder_button.setMaximumSize(QtCore.QSize(125, 30))
        self.device_new_folder_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_new_folder_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
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
        self.device_rename_item_button.setMinimumSize(QtCore.QSize(90, 30))
        self.device_rename_item_button.setMaximumSize(QtCore.QSize(90, 30))
        self.device_rename_item_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.device_rename_item_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.device_rename_item_button.setObjectName("device_rename_item_button")
        self.horizontalLayout_126.addWidget(self.device_rename_item_button)
        self.verticalLayout_37.addLayout(self.horizontalLayout_126)
        self.frame_36 = QtWidgets.QFrame(self.page_2)
        self.frame_36.setGeometry(QtCore.QRect(510, 0, 501, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setStyleSheet(".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_38.setContentsMargins(9, -1, 9, 9)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.file_viewer_widget = QtWidgets.QStackedWidget(self.frame_36)
        self.file_viewer_widget.setMinimumSize(QtCore.QSize(457, 0))
        self.file_viewer_widget.setStyleSheet("QStackedWidget{\n"
"    background-color: transparent;\n"
"}")
        self.file_viewer_widget.setObjectName("file_viewer_widget")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.file_absolute_path = QtWidgets.QLabel(self.page_9)
        self.file_absolute_path.setEnabled(True)
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
        self.verticalLayout_50.addWidget(self.file_absolute_path)
        self.gcodeeditor_2 = GcodeEditor(self.page_9)
        self.gcodeeditor_2.setStyleSheet("")
        self.gcodeeditor_2.setProperty("is_editor", True)
        self.gcodeeditor_2.setProperty("marginbackgroundcolor", "")
        self.gcodeeditor_2.setObjectName("gcodeeditor_2")
        self.verticalLayout_50.addWidget(self.gcodeeditor_2)
        self.horizontalLayout_129 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.edit_gcode_button = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_gcode_button.sizePolicy().hasHeightForWidth())
        self.edit_gcode_button.setSizePolicy(sizePolicy)
        self.edit_gcode_button.setMinimumSize(QtCore.QSize(100, 30))
        self.edit_gcode_button.setMaximumSize(QtCore.QSize(100, 30))
        self.edit_gcode_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.edit_gcode_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.edit_gcode_button.setCheckable(True)
        self.edit_gcode_button.setObjectName("edit_gcode_button")
        self.horizontalLayout_129.addWidget(self.edit_gcode_button)
        self.find_replace_button = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_replace_button.sizePolicy().hasHeightForWidth())
        self.find_replace_button.setSizePolicy(sizePolicy)
        self.find_replace_button.setMinimumSize(QtCore.QSize(100, 30))
        self.find_replace_button.setMaximumSize(QtCore.QSize(100, 30))
        self.find_replace_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.find_replace_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.find_replace_button.setObjectName("find_replace_button")
        self.horizontalLayout_129.addWidget(self.find_replace_button)
        self.save_button = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(100, 30))
        self.save_button.setMaximumSize(QtCore.QSize(100, 30))
        self.save_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_129.addWidget(self.save_button)
        self.save_as_button = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_button.sizePolicy().hasHeightForWidth())
        self.save_as_button.setSizePolicy(sizePolicy)
        self.save_as_button.setMinimumSize(QtCore.QSize(100, 30))
        self.save_as_button.setMaximumSize(QtCore.QSize(100, 30))
        self.save_as_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_as_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.save_as_button.setObjectName("save_as_button")
        self.horizontalLayout_129.addWidget(self.save_as_button)
        self.verticalLayout_50.addLayout(self.horizontalLayout_129)
        self.file_viewer_widget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.webView = QtWebKitWidgets.QWebView(self.page_10)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout_52.addWidget(self.webView)
        self.file_viewer_widget.addWidget(self.page_10)
        self.verticalLayout_38.addWidget(self.file_viewer_widget)
        self.btnViewHomeDir = QtWidgets.QPushButton(self.page_2)
        self.btnViewHomeDir.setGeometry(QtCore.QRect(80, 540, 181, 25))
        self.btnViewHomeDir.setObjectName("btnViewHomeDir")
        self.btnViewPresetDir = QtWidgets.QPushButton(self.page_2)
        self.btnViewPresetDir.setGeometry(QtCore.QRect(80, 590, 181, 25))
        self.btnViewPresetDir.setObjectName("btnViewPresetDir")
        self.btnViewNcDir = QtWidgets.QPushButton(self.page_2)
        self.btnViewNcDir.setGeometry(QtCore.QRect(90, 640, 181, 25))
        self.btnViewNcDir.setObjectName("btnViewNcDir")
        self.stackedWidgetMain.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidgetMain)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.gridFrame2 = QtWidgets.QFrame(self.horizontalWidget)
        self.gridFrame2.setMinimumSize(QtCore.QSize(100, 0))
        self.gridFrame2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gridFrame2.setStyleSheet(".QFrame {\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"}   \n"
"\n"
"\n"
" ")
        self.gridFrame2.setFrameShape(QtWidgets.QFrame.Box)
        self.gridFrame2.setObjectName("gridFrame2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnMdi = ActionButton(self.gridFrame2)
        self.btnMdi.setObjectName("btnMdi")
        self.gridLayout_2.addWidget(self.btnMdi, 2, 0, 1, 1)
        self.btnManual = ActionButton(self.gridFrame2)
        self.btnManual.setObjectName("btnManual")
        self.gridLayout_2.addWidget(self.btnManual, 1, 0, 1, 1)
        self.btnProgram = ActionButton(self.gridFrame2)
        self.btnProgram.setObjectName("btnProgram")
        self.gridLayout_2.addWidget(self.btnProgram, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame2)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.stackedWidgetMain.setCurrentIndex(0)
        self.stackedWidgetJogMdi.setCurrentIndex(2)
        self.stackedWidgetLeftActions.setCurrentIndex(2)
        self.file_viewer_widget.setCurrentIndex(0)
        self.btnViewHomeDir.clicked.connect(self.filesystemtable_2.viewHomeDirectory)
        self.btnViewPresetDir.clicked.connect(self.filesystemtable_2.viewPresetDirectory)
        self.btnViewNcDir.clicked.connect(self.filesystemtable_2.viewNCFilesDirectory)
        self.removabledevicecombobox.currentPathChanged['QString'].connect(self.filesystemtable_2.setRootPath)
        self.removabledevicecombobox.usbPresent['bool'].connect(self.device_eject_usb_button.setEnabled)
        self.removabledevicecombobox.currentDeviceEjectable['bool'].connect(self.device_eject_usb_button.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statuslabel_23.setText(_translate("MainWindow", "AXIS"))
        self.statuslabel_23.setProperty("rules", _translate("MainWindow", "[]"))
        self.statuslabel_24.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \' POS\'\\n\", \"name\": \"WCS Header\"}]"))
        self.work_column_header_9.setText(_translate("MainWindow", "MACHINE"))
        self.dtg_column_header_4.setText(_translate("MainWindow", "DTG"))
        self.statuslabel_25.setText(_translate("MainWindow", "REF"))
        self.statuslabel_25.setProperty("rules", _translate("MainWindow", "[]"))
        self.zero_x_button_4.setText(_translate("MainWindow", "X"))
        self.zero_x_button_4.setProperty("rules", _translate("MainWindow", "[\n"
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
        self.zero_x_button_4.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} X0.0"))
        self.drolabel_7.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_7.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_7.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_8.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_8.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_8.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_9.setText(_translate("MainWindow", "REF X"))
        self.axisactionbutton_9.setProperty("actionName", _translate("MainWindow", "machine.home.axis:x"))
        self.zero_y_button_4.setText(_translate("MainWindow", "Y"))
        self.zero_y_button_4.setProperty("rules", _translate("MainWindow", "[\n"
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
        self.zero_y_button_4.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} Y0.0"))
        self.drolabel_9.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_9.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_9.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_10.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_10.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_10.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_5.setText(_translate("MainWindow", "REF Y"))
        self.axisactionbutton_5.setProperty("actionName", _translate("MainWindow", "machine.home.axis:y"))
        self.zero_z_button_4.setText(_translate("MainWindow", "Z"))
        self.zero_z_button_4.setProperty("rules", _translate("MainWindow", "[\n"
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
        self.zero_z_button_4.setProperty("MDICommand", _translate("MainWindow", "G10 L20 P{ch[0]} Z0.0"))
        self.drolabel_11.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_11.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_11.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_12.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_12.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_12.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_7.setText(_translate("MainWindow", "REF Z"))
        self.axisactionbutton_7.setProperty("actionName", _translate("MainWindow", "machine.home.axis:z"))
        self.zero_a_button_4.setText(_translate("MainWindow", "A"))
        self.zero_a_button_4.setProperty("rules", _translate("MainWindow", "[\n"
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
        self.zero_a_button_4.setProperty("MDICommand", _translate("MainWindow", "G10 L2 P{ch[0]} A0.0"))
        self.drowidget_7.setProperty("metricTemplate", _translate("MainWindow", "%10.2f"))
        self.drolabel_13.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_13.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_13.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.drolabel_14.setProperty("inchFormat", _translate("MainWindow", "%9.4f"))
        self.drolabel_14.setProperty("millimeterFormat", _translate("MainWindow", "%10.3f"))
        self.drolabel_14.setProperty("degreeFormat", _translate("MainWindow", "%10.2f"))
        self.axisactionbutton_8.setText(_translate("MainWindow", "REF A"))
        self.axisactionbutton_8.setProperty("actionName", _translate("MainWindow", "machine.home.axis:a"))
        self.groupBox.setTitle(_translate("MainWindow", "Jog Increment"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Jog Speed"))
        self.settings_slider.setProperty("settingName", _translate("MainWindow", "machine.jog.linear-speed-percentage"))
        self.fr_override_dro_2.setText(_translate("MainWindow", "30%"))
        self.fr_override_dro_2.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"settings:machine.jog.linear-speed-percentage\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"%s%%\\\" % ch[0]\", \"name\": \"New Rule\"}]"))
        self.y_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:y,pos"))
        self.z_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:z,pos"))
        self.x_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:x,neg"))
        self.x_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:x,pos"))
        self.y_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:y,neg"))
        self.z_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:z,neg"))
        self.a_plus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:a,pos"))
        self.a_minus_jogbutton.setProperty("actionName", _translate("MainWindow", "machine.jog.axis:a,neg"))
        self.pushButton_19.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "2"))
        self.pushButton_15.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "S"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "Run"))
        self.pushButton_12.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_22.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "A"))
        self.pushButton_21.setText(_translate("MainWindow", " "))
        self.pushButton_4.setText(_translate("MainWindow", "Y"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton_20.setText(_translate("MainWindow", "."))
        self.pushButton_16.setText(_translate("MainWindow", "7"))
        self.pushButton_17.setText(_translate("MainWindow", "8"))
        self.pushButton_5.setText(_translate("MainWindow", "Z"))
        self.pushButton_23.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "G"))
        self.pushButton_18.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "M"))
        self.pushButton_24.setText(_translate("MainWindow", "T"))
        self.pushButton_25.setText(_translate("MainWindow", "P"))
        self.pushButton_26.setText(_translate("MainWindow", "K"))
        self.pushButton_27.setText(_translate("MainWindow", "I"))
        self.pushButton_28.setText(_translate("MainWindow", "J"))
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
        self.actionbutton_3.setText(_translate("MainWindow", "CYCLE START"))
        self.actionbutton_3.setProperty("actionName", _translate("MainWindow", "program.run"))
        self.actionbutton_13.setText(_translate("MainWindow", "Flood"))
        self.actionbutton_13.setProperty("actionName", _translate("MainWindow", "coolant.flood.toggle"))
        self.actionbutton_7.setText(_translate("MainWindow", "STOP"))
        self.actionbutton_7.setProperty("actionName", _translate("MainWindow", "program.abort"))
        self.actionbutton_14.setText(_translate("MainWindow", "Mist"))
        self.actionbutton_14.setProperty("actionName", _translate("MainWindow", "coolant.mist.toggle"))
        self.actionbutton_15.setText(_translate("MainWindow", "FEED HOLD"))
        self.actionbutton_15.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_15.setProperty("actionName", _translate("MainWindow", "program.pause"))
        self.actionbutton_16.setText(_translate("MainWindow", "Single Block"))
        self.actionbutton_16.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_16.setProperty("actionName", _translate("MainWindow", "program.step"))
        self.actionbutton_17.setText(_translate("MainWindow", "Stop and remember Line"))
        self.actionbutton_17.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_17.setProperty("actionName", _translate("MainWindow", "program.pause"))
        self.actionbutton_18.setText(_translate("MainWindow", "Pause and Inspect"))
        self.actionbutton_18.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_18.setProperty("actionName", _translate("MainWindow", "program.pause"))
        self.actionbutton_19.setText(_translate("MainWindow", "RUN FM HERE"))
        self.actionbutton_19.setProperty("actionName", _translate("MainWindow", "program.run-from-line"))
        self.ref_coilumn_header_4.setText(_translate("MainWindow", "  T"))
        self.tool_number_entry_main_panel_2.setText(_translate("MainWindow", "0"))
        self.tool_number_entry_main_panel_2.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == \'On\' and ch[1] == \'Idle\'\", \"name\": \"enable/disable\"}]"))
        self.m6_tool_call_button_main_panel_2.setText(_translate("MainWindow", "M6 G43"))
        self.m6_tool_call_button_main_panel_2.setProperty("filename", _translate("MainWindow", "m6_tool_call_main_panel.ngc"))
        self.statuslabel.setText(_translate("MainWindow", "Diameter: 8mm"))
        self.statuslabel_3.setText(_translate("MainWindow", "Chip Load @2000RPM & F200 : 0.02mm/min"))
        self.statuslabel_2.setText(_translate("MainWindow", "Z Offset: 123"))
        self.spindle_rev_button.setText(_translate("MainWindow", "REV"))
        self.spindle_rev_button.setProperty("actionName", _translate("MainWindow", "spindle.reverse"))
        self.spindle_stop_button.setText(_translate("MainWindow", "STOP"))
        self.spindle_stop_button.setProperty("actionName", _translate("MainWindow", "spindle.off"))
        self.spindle_fwd_button.setText(_translate("MainWindow", "FWD"))
        self.spindle_fwd_button.setProperty("actionName", _translate("MainWindow", "spindle.forward"))
        self.ref_coilumn_header_5.setText(_translate("MainWindow", "  S"))
        self.tool_number_entry_main_panel_3.setText(_translate("MainWindow", "0"))
        self.tool_number_entry_main_panel_3.setProperty("rules", _translate("MainWindow", "[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == \'On\' and ch[1] == \'Idle\'\", \"name\": \"enable/disable\"}]"))
        self.device_folder_up_button.setText(_translate("MainWindow", "  FOLDER UP"))
        self.device_eject_usb_button.setText(_translate("MainWindow", "EJECT USB"))
        self.device_delete_item_button.setText(_translate("MainWindow", " DELETE"))
        self.device_new_file_button.setText(_translate("MainWindow", " NEW FILE"))
        self.device_new_folder_button.setText(_translate("MainWindow", " NEW FOLDER"))
        self.device_rename_item_button.setText(_translate("MainWindow", "RENAME"))
        self.gcodeeditor_2.setProperty("backgroundcolor", _translate("MainWindow", "#ffffff"))
        self.edit_gcode_button.setText(_translate("MainWindow", "EDIT G-CODE"))
        self.find_replace_button.setText(_translate("MainWindow", "FIND/REPLACE"))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.save_as_button.setText(_translate("MainWindow", "SAVE AS"))
        self.btnViewHomeDir.setText(_translate("MainWindow", "View Home Dir"))
        self.btnViewPresetDir.setText(_translate("MainWindow", "View Preset Dir"))
        self.btnViewNcDir.setText(_translate("MainWindow", "View NC Dir"))
        self.btnMdi.setText(_translate("MainWindow", "MDI"))
        self.btnManual.setText(_translate("MainWindow", "Manual"))
        self.btnProgram.setText(_translate("MainWindow", "Program"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionOPEN.setText(_translate("MainWindow", "oPEN"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "F11"))

from PyQt5 import QtWebKitWidgets
from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.containers.stack import VCPStackedWidget
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.dro_widget import DROWidget
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.display_widgets.vtk_backplot.vtk_backplot import VTKBackPlot
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable, RemovableDeviceComboBox
from qtpyvcp.widgets.input_widgets.gcode_editor import GcodeEditor
from qtpyvcp.widgets.input_widgets.jog_increment import JogIncrementWidget
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.setting_slider import VCPSettingsSlider
import probe_basic_rc
import resources_rc
