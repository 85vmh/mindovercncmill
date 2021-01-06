# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cnc/mindovercncmill/mindovercncmill/widgets/probe_param_input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 44)
        Form.setMinimumSize(QtCore.QSize(350, 40))
        Form.setStyleSheet("background: rgb(136, 138, 133)")
        self.param_label = QtWidgets.QLabel(Form)
        self.param_label.setGeometry(QtCore.QRect(10, 5, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.param_label.sizePolicy().hasHeightForWidth())
        self.param_label.setSizePolicy(sizePolicy)
        self.param_label.setMinimumSize(QtCore.QSize(0, 30))
        self.param_label.setMaximumSize(QtCore.QSize(280, 30))
        self.param_label.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.param_label.setLineWidth(0)
        self.param_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.param_label.setIndent(0)
        self.param_label.setObjectName("param_label")
        self.input_unit = StatusLabel(Form)
        self.input_unit.setGeometry(QtCore.QRect(390, 10, 50, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_unit.sizePolicy().hasHeightForWidth())
        self.input_unit.setSizePolicy(sizePolicy)
        self.input_unit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.input_unit.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.input_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_unit.setObjectName("input_unit")
        self.param_input = QtWidgets.QLineEdit(Form)
        self.param_input.setGeometry(QtCore.QRect(300, 5, 80, 30))
        self.param_input.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.param_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.param_input.setObjectName("param_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.param_label.setText(_translate("Form", "Param Label:"))
        self.input_unit.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:linear_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Units\"}]"))

from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
