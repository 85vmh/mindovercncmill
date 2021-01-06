# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'probe_wizard_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1123, 618)
        self.stackedWidget = VCPStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 5, 1071, 606))
        self.stackedWidget.setStyleSheet("background: rgb(136, 138, 133)")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_loadProbeTool = QtWidgets.QWidget()
        self.page_loadProbeTool.setObjectName("page_loadProbeTool")
        self.label = QtWidgets.QLabel(self.page_loadProbeTool)
        self.label.setGeometry(QtCore.QRect(225, 95, 326, 61))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_loadProbeTool)
        self.page_tripProbeTip = QtWidgets.QWidget()
        self.page_tripProbeTip.setObjectName("page_tripProbeTip")
        self.label_2 = QtWidgets.QLabel(self.page_tripProbeTip)
        self.label_2.setGeometry(QtCore.QRect(210, 170, 321, 56))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.page_tripProbeTip)
        self.label_7.setGeometry(QtCore.QRect(320, 220, 101, 66))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/probe_icons/touch.png"))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_tripProbeTip)
        self.page_selectProbeOperation = QtWidgets.QWidget()
        self.page_selectProbeOperation.setObjectName("page_selectProbeOperation")
        self.probe_group_select = QtWidgets.QWidget(self.page_selectProbeOperation)
        self.probe_group_select.setGeometry(QtCore.QRect(15, 0, 801, 46))
        self.probe_group_select.setStyleSheet("QWidget {\n"
"    font: 13pt \"bebas kai\";\n"
"}")
        self.probe_group_select.setObjectName("probe_group_select")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.probe_group_select)
        self.horizontalLayout_30.setContentsMargins(10, 3, 10, 6)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.outside_corners = QtWidgets.QPushButton(self.probe_group_select)
        self.outside_corners.setFocusPolicy(QtCore.Qt.NoFocus)
        self.outside_corners.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 2px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.outside_corners.setCheckable(True)
        self.outside_corners.setChecked(True)
        self.outside_corners.setAutoExclusive(True)
        self.outside_corners.setProperty("page", 0)
        self.outside_corners.setObjectName("outside_corners")
        self.probeTabsGroup = QtWidgets.QButtonGroup(Form)
        self.probeTabsGroup.setObjectName("probeTabsGroup")
        self.probeTabsGroup.addButton(self.outside_corners)
        self.horizontalLayout_30.addWidget(self.outside_corners)
        self.inside_corners = QtWidgets.QPushButton(self.probe_group_select)
        self.inside_corners.setFocusPolicy(QtCore.Qt.NoFocus)
        self.inside_corners.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.inside_corners.setCheckable(True)
        self.inside_corners.setAutoExclusive(True)
        self.inside_corners.setProperty("page", 1)
        self.inside_corners.setObjectName("inside_corners")
        self.probeTabsGroup.addButton(self.inside_corners)
        self.horizontalLayout_30.addWidget(self.inside_corners)
        self.boss_and_pocket = QtWidgets.QPushButton(self.probe_group_select)
        self.boss_and_pocket.setFocusPolicy(QtCore.Qt.NoFocus)
        self.boss_and_pocket.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.boss_and_pocket.setCheckable(True)
        self.boss_and_pocket.setAutoExclusive(True)
        self.boss_and_pocket.setProperty("page", 2)
        self.boss_and_pocket.setObjectName("boss_and_pocket")
        self.probeTabsGroup.addButton(self.boss_and_pocket)
        self.horizontalLayout_30.addWidget(self.boss_and_pocket)
        self.ridge_and_valley = QtWidgets.QPushButton(self.probe_group_select)
        self.ridge_and_valley.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ridge_and_valley.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.ridge_and_valley.setCheckable(True)
        self.ridge_and_valley.setAutoExclusive(True)
        self.ridge_and_valley.setProperty("page", 3)
        self.ridge_and_valley.setObjectName("ridge_and_valley")
        self.probeTabsGroup.addButton(self.ridge_and_valley)
        self.horizontalLayout_30.addWidget(self.ridge_and_valley)
        self.rotation_angle = QtWidgets.QPushButton(self.probe_group_select)
        self.rotation_angle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rotation_angle.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.rotation_angle.setCheckable(True)
        self.rotation_angle.setAutoExclusive(True)
        self.rotation_angle.setProperty("page", 4)
        self.rotation_angle.setObjectName("rotation_angle")
        self.probeTabsGroup.addButton(self.rotation_angle)
        self.horizontalLayout_30.addWidget(self.rotation_angle)
        self.rotary_axis = QtWidgets.QPushButton(self.probe_group_select)
        self.rotary_axis.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rotary_axis.setStyleSheet("QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 2px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.rotary_axis.setCheckable(True)
        self.rotary_axis.setAutoExclusive(True)
        self.rotary_axis.setProperty("page", 5)
        self.rotary_axis.setObjectName("rotary_axis")
        self.probeTabsGroup.addButton(self.rotary_axis)
        self.horizontalLayout_30.addWidget(self.rotary_axis)
        self.probingCyclesStackedWidget = QtWidgets.QStackedWidget(self.page_selectProbeOperation)
        self.probingCyclesStackedWidget.setGeometry(QtCore.QRect(15, 55, 396, 351))
        self.probingCyclesStackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.probingCyclesStackedWidget.setObjectName("probingCyclesStackedWidget")
        self.outsideCornersPage = QtWidgets.QWidget()
        self.outsideCornersPage.setObjectName("outsideCornersPage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.outsideCornersPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 276))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.probepushbutton = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton.sizePolicy().hasHeightForWidth())
        self.probepushbutton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/probe_icons/X+Y-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton.setIcon(icon)
        self.probepushbutton.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton.setObjectName("probepushbutton")
        self.probeButtonGroup = QtWidgets.QButtonGroup(Form)
        self.probeButtonGroup.setObjectName("probeButtonGroup")
        self.probeButtonGroup.addButton(self.probepushbutton)
        self.gridLayout_3.addWidget(self.probepushbutton, 0, 0, 1, 1)
        self.probepushbutton_4 = ProbePushButton(self.gridLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/probe_icons/X+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_4.setIcon(icon1)
        self.probepushbutton_4.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_4.setObjectName("probepushbutton_4")
        self.probeButtonGroup.addButton(self.probepushbutton_4)
        self.gridLayout_3.addWidget(self.probepushbutton_4, 1, 0, 1, 1)
        self.probepushbutton_2 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_2.sizePolicy().hasHeightForWidth())
        self.probepushbutton_2.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/probe_icons/inY-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_2.setIcon(icon2)
        self.probepushbutton_2.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_2.setObjectName("probepushbutton_2")
        self.probeButtonGroup.addButton(self.probepushbutton_2)
        self.gridLayout_3.addWidget(self.probepushbutton_2, 0, 1, 1, 1)
        self.probepushbutton_3 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_3.sizePolicy().hasHeightForWidth())
        self.probepushbutton_3.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/probe_icons/X-Y-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_3.setIcon(icon3)
        self.probepushbutton_3.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_3.setObjectName("probepushbutton_3")
        self.probeButtonGroup.addButton(self.probepushbutton_3)
        self.gridLayout_3.addWidget(self.probepushbutton_3, 0, 2, 1, 1)
        self.probepushbutton_5 = ProbePushButton(self.gridLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/probe_icons/X+Y+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_5.setIcon(icon4)
        self.probepushbutton_5.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_5.setObjectName("probepushbutton_5")
        self.probeButtonGroup.addButton(self.probepushbutton_5)
        self.gridLayout_3.addWidget(self.probepushbutton_5, 2, 0, 1, 1)
        self.probepushbutton_6 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_6.sizePolicy().hasHeightForWidth())
        self.probepushbutton_6.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/probe_icons/Y+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_6.setIcon(icon5)
        self.probepushbutton_6.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_6.setObjectName("probepushbutton_6")
        self.probeButtonGroup.addButton(self.probepushbutton_6)
        self.gridLayout_3.addWidget(self.probepushbutton_6, 2, 1, 1, 1)
        self.probepushbutton_7 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_7.sizePolicy().hasHeightForWidth())
        self.probepushbutton_7.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/probe_icons/X-Y+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_7.setIcon(icon6)
        self.probepushbutton_7.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_7.setObjectName("probepushbutton_7")
        self.probeButtonGroup.addButton(self.probepushbutton_7)
        self.gridLayout_3.addWidget(self.probepushbutton_7, 2, 2, 1, 1)
        self.probepushbutton_8 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_8.sizePolicy().hasHeightForWidth())
        self.probepushbutton_8.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/probe_icons/X-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_8.setIcon(icon7)
        self.probepushbutton_8.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_8.setObjectName("probepushbutton_8")
        self.probeButtonGroup.addButton(self.probepushbutton_8)
        self.gridLayout_3.addWidget(self.probepushbutton_8, 1, 2, 1, 1)
        self.probepushbutton_17 = ProbePushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_17.sizePolicy().hasHeightForWidth())
        self.probepushbutton_17.setSizePolicy(sizePolicy)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/probe_icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_17.setIcon(icon8)
        self.probepushbutton_17.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_17.setObjectName("probepushbutton_17")
        self.probeButtonGroup.addButton(self.probepushbutton_17)
        self.gridLayout_3.addWidget(self.probepushbutton_17, 1, 1, 1, 1)
        self.probingCyclesStackedWidget.addWidget(self.outsideCornersPage)
        self.insideCornersPage = QtWidgets.QWidget()
        self.insideCornersPage.setObjectName("insideCornersPage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.insideCornersPage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 291, 276))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.probepushbutton_9 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_9.sizePolicy().hasHeightForWidth())
        self.probepushbutton_9.setSizePolicy(sizePolicy)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/probe_icons/inX-Y+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_9.setIcon(icon9)
        self.probepushbutton_9.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_9.setObjectName("probepushbutton_9")
        self.gridLayout_5.addWidget(self.probepushbutton_9, 0, 0, 1, 1)
        self.probepushbutton_10 = ProbePushButton(self.gridLayoutWidget_2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/probe_icons/inX-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_10.setIcon(icon10)
        self.probepushbutton_10.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_10.setObjectName("probepushbutton_10")
        self.gridLayout_5.addWidget(self.probepushbutton_10, 1, 0, 1, 1)
        self.probepushbutton_11 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_11.sizePolicy().hasHeightForWidth())
        self.probepushbutton_11.setSizePolicy(sizePolicy)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/probe_icons/inY+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_11.setIcon(icon11)
        self.probepushbutton_11.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_11.setObjectName("probepushbutton_11")
        self.gridLayout_5.addWidget(self.probepushbutton_11, 0, 1, 1, 1)
        self.probepushbutton_12 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_12.sizePolicy().hasHeightForWidth())
        self.probepushbutton_12.setSizePolicy(sizePolicy)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/probe_icons/inX+Y+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_12.setIcon(icon12)
        self.probepushbutton_12.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_12.setObjectName("probepushbutton_12")
        self.gridLayout_5.addWidget(self.probepushbutton_12, 0, 2, 1, 1)
        self.probepushbutton_13 = ProbePushButton(self.gridLayoutWidget_2)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/probe_icons/inX-Y-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_13.setIcon(icon13)
        self.probepushbutton_13.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_13.setObjectName("probepushbutton_13")
        self.gridLayout_5.addWidget(self.probepushbutton_13, 2, 0, 1, 1)
        self.probepushbutton_14 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_14.sizePolicy().hasHeightForWidth())
        self.probepushbutton_14.setSizePolicy(sizePolicy)
        self.probepushbutton_14.setIcon(icon2)
        self.probepushbutton_14.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_14.setObjectName("probepushbutton_14")
        self.gridLayout_5.addWidget(self.probepushbutton_14, 2, 1, 1, 1)
        self.probepushbutton_15 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_15.sizePolicy().hasHeightForWidth())
        self.probepushbutton_15.setSizePolicy(sizePolicy)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/probe_icons/inX+Y-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_15.setIcon(icon14)
        self.probepushbutton_15.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_15.setObjectName("probepushbutton_15")
        self.gridLayout_5.addWidget(self.probepushbutton_15, 2, 2, 1, 1)
        self.probepushbutton_16 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_16.sizePolicy().hasHeightForWidth())
        self.probepushbutton_16.setSizePolicy(sizePolicy)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/probe_icons/inX+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_16.setIcon(icon15)
        self.probepushbutton_16.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_16.setObjectName("probepushbutton_16")
        self.gridLayout_5.addWidget(self.probepushbutton_16, 1, 2, 1, 1)
        self.probepushbutton_18 = ProbePushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_18.sizePolicy().hasHeightForWidth())
        self.probepushbutton_18.setSizePolicy(sizePolicy)
        self.probepushbutton_18.setIcon(icon8)
        self.probepushbutton_18.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_18.setObjectName("probepushbutton_18")
        self.gridLayout_5.addWidget(self.probepushbutton_18, 1, 1, 1, 1)
        self.probingCyclesStackedWidget.addWidget(self.insideCornersPage)
        self.bossPocketPage = QtWidgets.QWidget()
        self.bossPocketPage.setObjectName("bossPocketPage")
        self.probepushbutton_19 = ProbePushButton(self.bossPocketPage)
        self.probepushbutton_19.setGeometry(QtCore.QRect(30, 15, 83, 79))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_19.sizePolicy().hasHeightForWidth())
        self.probepushbutton_19.setSizePolicy(sizePolicy)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/probe_icons/inHole.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_19.setIcon(icon16)
        self.probepushbutton_19.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_19.setObjectName("probepushbutton_19")
        self.probepushbutton_20 = ProbePushButton(self.bossPocketPage)
        self.probepushbutton_20.setGeometry(QtCore.QRect(155, 15, 83, 79))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_20.sizePolicy().hasHeightForWidth())
        self.probepushbutton_20.setSizePolicy(sizePolicy)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/probe_icons/xy_center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_20.setIcon(icon17)
        self.probepushbutton_20.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_20.setObjectName("probepushbutton_20")
        self.probingCyclesStackedWidget.addWidget(self.bossPocketPage)
        self.ridgeValleyPage = QtWidgets.QWidget()
        self.ridgeValleyPage.setObjectName("ridgeValleyPage")
        self.probepushbutton_21 = ProbePushButton(self.ridgeValleyPage)
        self.probepushbutton_21.setGeometry(QtCore.QRect(30, 30, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_21.sizePolicy().hasHeightForWidth())
        self.probepushbutton_21.setSizePolicy(sizePolicy)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/probe_icons/Lx_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_21.setIcon(icon18)
        self.probepushbutton_21.setIconSize(QtCore.QSize(200, 200))
        self.probepushbutton_21.setObjectName("probepushbutton_21")
        self.probepushbutton_22 = ProbePushButton(self.ridgeValleyPage)
        self.probepushbutton_22.setGeometry(QtCore.QRect(155, 30, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_22.sizePolicy().hasHeightForWidth())
        self.probepushbutton_22.setSizePolicy(sizePolicy)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/probe_icons/Lx_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_22.setIcon(icon19)
        self.probepushbutton_22.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_22.setObjectName("probepushbutton_22")
        self.probepushbutton_23 = ProbePushButton(self.ridgeValleyPage)
        self.probepushbutton_23.setGeometry(QtCore.QRect(30, 150, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_23.sizePolicy().hasHeightForWidth())
        self.probepushbutton_23.setSizePolicy(sizePolicy)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/probe_icons/Ly_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_23.setIcon(icon20)
        self.probepushbutton_23.setIconSize(QtCore.QSize(200, 200))
        self.probepushbutton_23.setObjectName("probepushbutton_23")
        self.probepushbutton_24 = ProbePushButton(self.ridgeValleyPage)
        self.probepushbutton_24.setGeometry(QtCore.QRect(155, 150, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_24.sizePolicy().hasHeightForWidth())
        self.probepushbutton_24.setSizePolicy(sizePolicy)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/probe_icons/Ly_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_24.setIcon(icon21)
        self.probepushbutton_24.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_24.setObjectName("probepushbutton_24")
        self.probingCyclesStackedWidget.addWidget(self.ridgeValleyPage)
        self.edgeAnglePage = QtWidgets.QWidget()
        self.edgeAnglePage.setObjectName("edgeAnglePage")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.edgeAnglePage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(105, 70, 174, 166))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.probepushbutton_28 = ProbePushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_28.sizePolicy().hasHeightForWidth())
        self.probepushbutton_28.setSizePolicy(sizePolicy)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/probe_icons/angleX+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_28.setIcon(icon22)
        self.probepushbutton_28.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_28.setObjectName("probepushbutton_28")
        self.gridLayout_7.addWidget(self.probepushbutton_28, 0, 0, 1, 1)
        self.probepushbutton_29 = ProbePushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_29.sizePolicy().hasHeightForWidth())
        self.probepushbutton_29.setSizePolicy(sizePolicy)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/probe_icons/angleY+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_29.setIcon(icon23)
        self.probepushbutton_29.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_29.setObjectName("probepushbutton_29")
        self.gridLayout_7.addWidget(self.probepushbutton_29, 1, 0, 1, 1)
        self.probepushbutton_30 = ProbePushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_30.sizePolicy().hasHeightForWidth())
        self.probepushbutton_30.setSizePolicy(sizePolicy)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/probe_icons/angleY-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_30.setIcon(icon24)
        self.probepushbutton_30.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_30.setObjectName("probepushbutton_30")
        self.gridLayout_7.addWidget(self.probepushbutton_30, 0, 1, 1, 1)
        self.probepushbutton_31 = ProbePushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probepushbutton_31.sizePolicy().hasHeightForWidth())
        self.probepushbutton_31.setSizePolicy(sizePolicy)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/probe_icons/angleX-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probepushbutton_31.setIcon(icon25)
        self.probepushbutton_31.setIconSize(QtCore.QSize(75, 75))
        self.probepushbutton_31.setObjectName("probepushbutton_31")
        self.gridLayout_7.addWidget(self.probepushbutton_31, 1, 1, 1, 1)
        self.probingCyclesStackedWidget.addWidget(self.edgeAnglePage)
        self.rotaryAxisPage = QtWidgets.QWidget()
        self.rotaryAxisPage.setObjectName("rotaryAxisPage")
        self.probingCyclesStackedWidget.addWidget(self.rotaryAxisPage)
        self.stackedWidget.addWidget(self.page_selectProbeOperation)
        self.page_enterParameters = QtWidgets.QWidget()
        self.page_enterParameters.setObjectName("page_enterParameters")
        self.buttonChangeRoutine = QtWidgets.QPushButton(self.page_enterParameters)
        self.buttonChangeRoutine.setGeometry(QtCore.QRect(390, 5, 131, 36))
        self.buttonChangeRoutine.setObjectName("buttonChangeRoutine")
        self.labelSelectedRoutine = QtWidgets.QLabel(self.page_enterParameters)
        self.labelSelectedRoutine.setGeometry(QtCore.QRect(15, 10, 316, 26))
        self.labelSelectedRoutine.setObjectName("labelSelectedRoutine")
        self.buttonGenerateCode = QtWidgets.QPushButton(self.page_enterParameters)
        self.buttonGenerateCode.setGeometry(QtCore.QRect(660, 475, 196, 46))
        self.buttonGenerateCode.setObjectName("buttonGenerateCode")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_enterParameters)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(585, 55, 386, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qmlprobe = QmlProbe(self.page_enterParameters)
        self.qmlprobe.setGeometry(QtCore.QRect(15, 195, 521, 401))
        self.qmlprobe.setObjectName("qmlprobe")
        self.spinBox = QtWidgets.QSpinBox(self.page_enterParameters)
        self.spinBox.setGeometry(QtCore.QRect(565, 470, 49, 26))
        self.spinBox.setObjectName("spinBox")
        self.settings_lineedit = VCPSettingsLineEdit(self.page_enterParameters)
        self.settings_lineedit.setGeometry(QtCore.QRect(105, 60, 216, 25))
        self.settings_lineedit.setObjectName("settings_lineedit")
        self.stackedWidget.addWidget(self.page_enterParameters)
        self.page_displayResults = QtWidgets.QWidget()
        self.page_displayResults.setObjectName("page_displayResults")
        self.label_108 = QtWidgets.QLabel(self.page_displayResults)
        self.label_108.setGeometry(QtCore.QRect(125, 95, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)
        self.label_108.setMinimumSize(QtCore.QSize(0, 31))
        self.label_108.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_108.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_108.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_108.setLineWidth(0)
        self.label_108.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_108.setIndent(0)
        self.label_108.setObjectName("label_108")
        self.label_98 = QtWidgets.QLabel(self.page_displayResults)
        self.label_98.setGeometry(QtCore.QRect(130, 175, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy)
        self.label_98.setMinimumSize(QtCore.QSize(80, 31))
        self.label_98.setMaximumSize(QtCore.QSize(80, 30))
        self.label_98.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_98.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_98.setLineWidth(0)
        self.label_98.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_98.setIndent(0)
        self.label_98.setObjectName("label_98")
        self.buttonChangeParams = QtWidgets.QPushButton(self.page_displayResults)
        self.buttonChangeParams.setGeometry(QtCore.QRect(20, 15, 166, 36))
        self.buttonChangeParams.setObjectName("buttonChangeParams")
        self.x_plus_probed_position = StatusLabel(self.page_displayResults)
        self.x_plus_probed_position.setGeometry(QtCore.QRect(215, 175, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_plus_probed_position.sizePolicy().hasHeightForWidth())
        self.x_plus_probed_position.setSizePolicy(sizePolicy)
        self.x_plus_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.x_plus_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.x_plus_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.x_plus_probed_position.setText("")
        self.x_plus_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_plus_probed_position.setObjectName("x_plus_probed_position")
        self.x_minus_probed_position = StatusLabel(self.page_displayResults)
        self.x_minus_probed_position.setGeometry(QtCore.QRect(215, 95, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.x_minus_probed_position.setSizePolicy(sizePolicy)
        self.x_minus_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.x_minus_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.x_minus_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.x_minus_probed_position.setText("")
        self.x_minus_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_minus_probed_position.setObjectName("x_minus_probed_position")
        self.label_97 = QtWidgets.QLabel(self.page_displayResults)
        self.label_97.setGeometry(QtCore.QRect(125, 215, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy)
        self.label_97.setMinimumSize(QtCore.QSize(80, 31))
        self.label_97.setMaximumSize(QtCore.QSize(80, 30))
        self.label_97.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_97.setLineWidth(0)
        self.label_97.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_97.setIndent(0)
        self.label_97.setObjectName("label_97")
        self.label_113 = QtWidgets.QLabel(self.page_displayResults)
        self.label_113.setGeometry(QtCore.QRect(125, 135, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy)
        self.label_113.setMinimumSize(QtCore.QSize(80, 31))
        self.label_113.setMaximumSize(QtCore.QSize(80, 30))
        self.label_113.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_113.setLineWidth(0)
        self.label_113.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_113.setIndent(0)
        self.label_113.setObjectName("label_113")
        self.x_center_probed_position = StatusLabel(self.page_displayResults)
        self.x_center_probed_position.setGeometry(QtCore.QRect(215, 135, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_center_probed_position.sizePolicy().hasHeightForWidth())
        self.x_center_probed_position.setSizePolicy(sizePolicy)
        self.x_center_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.x_center_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.x_center_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.x_center_probed_position.setText("")
        self.x_center_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_center_probed_position.setObjectName("x_center_probed_position")
        self.x_probed_width = StatusLabel(self.page_displayResults)
        self.x_probed_width.setGeometry(QtCore.QRect(215, 215, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_probed_width.sizePolicy().hasHeightForWidth())
        self.x_probed_width.setSizePolicy(sizePolicy)
        self.x_probed_width.setMinimumSize(QtCore.QSize(80, 31))
        self.x_probed_width.setMaximumSize(QtCore.QSize(80, 31))
        self.x_probed_width.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.x_probed_width.setText("")
        self.x_probed_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_probed_width.setObjectName("x_probed_width")
        self.y_center_probed_position = StatusLabel(self.page_displayResults)
        self.y_center_probed_position.setGeometry(QtCore.QRect(435, 135, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_center_probed_position.sizePolicy().hasHeightForWidth())
        self.y_center_probed_position.setSizePolicy(sizePolicy)
        self.y_center_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.y_center_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.y_center_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.y_center_probed_position.setText("")
        self.y_center_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_center_probed_position.setObjectName("y_center_probed_position")
        self.label_109 = QtWidgets.QLabel(self.page_displayResults)
        self.label_109.setGeometry(QtCore.QRect(345, 95, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy)
        self.label_109.setMinimumSize(QtCore.QSize(0, 31))
        self.label_109.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_109.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_109.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_109.setLineWidth(0)
        self.label_109.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_109.setIndent(0)
        self.label_109.setObjectName("label_109")
        self.label_114 = QtWidgets.QLabel(self.page_displayResults)
        self.label_114.setGeometry(QtCore.QRect(345, 135, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setMinimumSize(QtCore.QSize(80, 31))
        self.label_114.setMaximumSize(QtCore.QSize(80, 30))
        self.label_114.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_114.setLineWidth(0)
        self.label_114.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_114.setIndent(0)
        self.label_114.setObjectName("label_114")
        self.y_probed_width = StatusLabel(self.page_displayResults)
        self.y_probed_width.setGeometry(QtCore.QRect(435, 215, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_probed_width.sizePolicy().hasHeightForWidth())
        self.y_probed_width.setSizePolicy(sizePolicy)
        self.y_probed_width.setMinimumSize(QtCore.QSize(80, 31))
        self.y_probed_width.setMaximumSize(QtCore.QSize(80, 31))
        self.y_probed_width.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.y_probed_width.setText("")
        self.y_probed_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_probed_width.setObjectName("y_probed_width")
        self.y_plus_probed_position = StatusLabel(self.page_displayResults)
        self.y_plus_probed_position.setGeometry(QtCore.QRect(435, 175, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_plus_probed_position.sizePolicy().hasHeightForWidth())
        self.y_plus_probed_position.setSizePolicy(sizePolicy)
        self.y_plus_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.y_plus_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.y_plus_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.y_plus_probed_position.setText("")
        self.y_plus_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_plus_probed_position.setObjectName("y_plus_probed_position")
        self.label_99 = QtWidgets.QLabel(self.page_displayResults)
        self.label_99.setGeometry(QtCore.QRect(350, 175, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy)
        self.label_99.setMinimumSize(QtCore.QSize(80, 31))
        self.label_99.setMaximumSize(QtCore.QSize(80, 30))
        self.label_99.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_99.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_99.setLineWidth(0)
        self.label_99.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_99.setIndent(0)
        self.label_99.setObjectName("label_99")
        self.label_100 = QtWidgets.QLabel(self.page_displayResults)
        self.label_100.setGeometry(QtCore.QRect(345, 215, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setMinimumSize(QtCore.QSize(80, 31))
        self.label_100.setMaximumSize(QtCore.QSize(80, 30))
        self.label_100.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_100.setLineWidth(0)
        self.label_100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_100.setIndent(0)
        self.label_100.setObjectName("label_100")
        self.y_minus_probed_position = StatusLabel(self.page_displayResults)
        self.y_minus_probed_position.setGeometry(QtCore.QRect(435, 95, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.y_minus_probed_position.setSizePolicy(sizePolicy)
        self.y_minus_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.y_minus_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.y_minus_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.y_minus_probed_position.setText("")
        self.y_minus_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_minus_probed_position.setObjectName("y_minus_probed_position")
        self.label_110 = QtWidgets.QLabel(self.page_displayResults)
        self.label_110.setGeometry(QtCore.QRect(565, 95, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy)
        self.label_110.setMinimumSize(QtCore.QSize(0, 31))
        self.label_110.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_110.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_110.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_110.setLineWidth(0)
        self.label_110.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_110.setIndent(0)
        self.label_110.setObjectName("label_110")
        self.z_minus_probed_position = StatusLabel(self.page_displayResults)
        self.z_minus_probed_position.setGeometry(QtCore.QRect(655, 95, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.z_minus_probed_position.setSizePolicy(sizePolicy)
        self.z_minus_probed_position.setMinimumSize(QtCore.QSize(80, 31))
        self.z_minus_probed_position.setMaximumSize(QtCore.QSize(80, 31))
        self.z_minus_probed_position.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.z_minus_probed_position.setText("")
        self.z_minus_probed_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.z_minus_probed_position.setObjectName("z_minus_probed_position")
        self.label_111 = QtWidgets.QLabel(self.page_displayResults)
        self.label_111.setGeometry(QtCore.QRect(565, 135, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy)
        self.label_111.setMinimumSize(QtCore.QSize(0, 31))
        self.label_111.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_111.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_111.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_111.setLineWidth(0)
        self.label_111.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_111.setIndent(0)
        self.label_111.setObjectName("label_111")
        self.probed_diameter = StatusLabel(self.page_displayResults)
        self.probed_diameter.setGeometry(QtCore.QRect(655, 135, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probed_diameter.sizePolicy().hasHeightForWidth())
        self.probed_diameter.setSizePolicy(sizePolicy)
        self.probed_diameter.setMinimumSize(QtCore.QSize(80, 31))
        self.probed_diameter.setMaximumSize(QtCore.QSize(80, 31))
        self.probed_diameter.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.probed_diameter.setText("")
        self.probed_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probed_diameter.setObjectName("probed_diameter")
        self.label_112 = QtWidgets.QLabel(self.page_displayResults)
        self.label_112.setGeometry(QtCore.QRect(565, 175, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy)
        self.label_112.setMinimumSize(QtCore.QSize(0, 31))
        self.label_112.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_112.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_112.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_112.setLineWidth(0)
        self.label_112.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_112.setIndent(0)
        self.label_112.setObjectName("label_112")
        self.edge_delta = StatusLabel(self.page_displayResults)
        self.edge_delta.setGeometry(QtCore.QRect(655, 175, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_delta.sizePolicy().hasHeightForWidth())
        self.edge_delta.setSizePolicy(sizePolicy)
        self.edge_delta.setMinimumSize(QtCore.QSize(80, 31))
        self.edge_delta.setMaximumSize(QtCore.QSize(80, 31))
        self.edge_delta.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.edge_delta.setText("")
        self.edge_delta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edge_delta.setObjectName("edge_delta")
        self.label_115 = QtWidgets.QLabel(self.page_displayResults)
        self.label_115.setGeometry(QtCore.QRect(565, 215, 83, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)
        self.label_115.setMinimumSize(QtCore.QSize(0, 31))
        self.label_115.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_115.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_115.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_115.setLineWidth(0)
        self.label_115.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_115.setIndent(0)
        self.label_115.setObjectName("label_115")
        self.edge_angle = StatusLabel(self.page_displayResults)
        self.edge_angle.setGeometry(QtCore.QRect(655, 215, 80, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_angle.sizePolicy().hasHeightForWidth())
        self.edge_angle.setSizePolicy(sizePolicy)
        self.edge_angle.setMinimumSize(QtCore.QSize(80, 31))
        self.edge_angle.setMaximumSize(QtCore.QSize(80, 31))
        self.edge_angle.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.edge_angle.setText("")
        self.edge_angle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edge_angle.setObjectName("edge_angle")
        self.stackedWidget.addWidget(self.page_displayResults)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        self.probingCyclesStackedWidget.setCurrentIndex(0)
        self.spinBox.valueChanged['int'].connect(self.qmlprobe.set_z_retract)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Load the probe tool into the spindle\n"
"and plug the cable"))
        self.label_2.setText(_translate("Form", "Touch the tip of the probe to ensure its working"))
        self.outside_corners.setText(_translate("Form", "OUTSIDE CORNERS"))
        self.inside_corners.setText(_translate("Form", "INSIDE CORNERS"))
        self.boss_and_pocket.setText(_translate("Form", "BOSS/POCKET"))
        self.ridge_and_valley.setText(_translate("Form", "RIDGE/VALLEY"))
        self.rotation_angle.setText(_translate("Form", "EDGE ANGLE"))
        self.rotary_axis.setText(_translate("Form", "ROTARY AXIS"))
        self.probepushbutton.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_4.setProperty("filename", _translate("Form", "probe_x_plus.ngc"))
        self.probepushbutton_2.setProperty("filename", _translate("Form", "probe_y_minus.ngc"))
        self.probepushbutton_5.setProperty("filename", _translate("Form", "probe_x_write_values.ngc"))
        self.probepushbutton_17.setProperty("filename", _translate("Form", "probe_z_minus.ngc"))
        self.probepushbutton_19.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_20.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_21.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_22.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_23.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.probepushbutton_24.setProperty("filename", _translate("Form", "probe_back_left_corner.ngc"))
        self.buttonChangeRoutine.setText(_translate("Form", "Change Routine"))
        self.labelSelectedRoutine.setText(_translate("Form", "Selected Routine Name"))
        self.buttonGenerateCode.setText(_translate("Form", "Generate Probing Code"))
        self.settings_lineedit.setProperty("settingName", _translate("Form", "probewizard.setting_name"))
        self.label_108.setText(_translate("Form", "X- PROBED:"))
        self.label_98.setText(_translate("Form", "X+ PROBED:"))
        self.buttonChangeParams.setText(_translate("Form", "Change Parameters"))
        self.x_plus_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.x_plus_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.x_minus_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.x_minus_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_97.setText(_translate("Form", "X WIDTH:"))
        self.label_113.setText(_translate("Form", "X CENTER:"))
        self.x_center_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.x_center_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.x_probed_width.setProperty("rules", _translate("Form", "[]"))
        self.x_probed_width.setProperty("format", _translate("Form", "{:6.4f}"))
        self.y_center_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.y_center_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_109.setText(_translate("Form", "Y- PROBED:"))
        self.label_114.setText(_translate("Form", "Y CENTER:"))
        self.y_probed_width.setProperty("rules", _translate("Form", "[]"))
        self.y_probed_width.setProperty("format", _translate("Form", "{:6.4f}"))
        self.y_plus_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.y_plus_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_99.setText(_translate("Form", "Y+ PROBED:"))
        self.label_100.setText(_translate("Form", "Y WIDTH:"))
        self.y_minus_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.y_minus_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_110.setText(_translate("Form", "Z- PROBED:"))
        self.z_minus_probed_position.setProperty("rules", _translate("Form", "[]"))
        self.z_minus_probed_position.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_111.setText(_translate("Form", "Diameter:"))
        self.probed_diameter.setProperty("rules", _translate("Form", "[]"))
        self.probed_diameter.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_112.setText(_translate("Form", "Edge Delta:"))
        self.edge_delta.setProperty("rules", _translate("Form", "[]"))
        self.edge_delta.setProperty("format", _translate("Form", "{:6.4f}"))
        self.label_115.setText(_translate("Form", "Edge Angle:"))
        self.edge_angle.setProperty("rules", _translate("Form", "[]"))
        self.edge_angle.setProperty("format", _translate("Form", "{:6.4f}"))

from qtpyvcp.widgets.containers.stack import VCPStackedWidget
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.setting_slider import VCPSettingsLineEdit
from widgets.probe_push_button import ProbePushButton
from widgets.qml_probe.qml_probe import QmlProbe
import resources_rc
