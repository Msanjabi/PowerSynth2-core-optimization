# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/thermalSetup.ui',
# licensing of 'ui/thermalSetup.ui' applies.
#
# Created: Thu Oct 21 14:10:54 2021
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 370)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thermal_setup_2 = QtWidgets.QFrame(Dialog)
        self.thermal_setup_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thermal_setup_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thermal_setup_2.setObjectName("thermal_setup_2")
        self.gridLayout = QtWidgets.QGridLayout(self.thermal_setup_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.thermal_setup_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_25 = QtWidgets.QLabel(self.thermal_setup_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_17.addWidget(self.label_25)
        self.combo_model_select = QtWidgets.QComboBox(self.thermal_setup_2)
        self.combo_model_select.setObjectName("combo_model_select")
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.setItemText(3, "")
        self.horizontalLayout_17.addWidget(self.combo_model_select)
        self.gridLayout.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_26 = QtWidgets.QLabel(self.thermal_setup_2)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_18.addWidget(self.label_26)
        self.lineedit_measure_name = QtWidgets.QLineEdit(self.thermal_setup_2)
        self.lineedit_measure_name.setObjectName("lineedit_measure_name")
        self.horizontalLayout_18.addWidget(self.lineedit_measure_name)
        self.gridLayout.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.thermal_setup_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_add_device = QtWidgets.QPushButton(self.thermal_setup_2)
        self.btn_add_device.setObjectName("btn_add_device")
        self.verticalLayout.addWidget(self.btn_add_device)
        self.btn_remove_device = QtWidgets.QPushButton(self.thermal_setup_2)
        self.btn_remove_device.setObjectName("btn_remove_device")
        self.verticalLayout.addWidget(self.btn_remove_device)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.thermal_setup_2)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_19.addWidget(self.label_27)
        self.heat_convection = QtWidgets.QLineEdit(self.thermal_setup_2)
        self.heat_convection.setObjectName("heat_convection")
        self.horizontalLayout_19.addWidget(self.heat_convection)
        self.gridLayout.addLayout(self.horizontalLayout_19, 4, 0, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_28 = QtWidgets.QLabel(self.thermal_setup_2)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_20.addWidget(self.label_28)
        self.ambient_temperature = QtWidgets.QSpinBox(self.thermal_setup_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ambient_temperature.sizePolicy().hasHeightForWidth())
        self.ambient_temperature.setSizePolicy(sizePolicy)
        self.ambient_temperature.setMinimumSize(QtCore.QSize(15, 0))
        self.ambient_temperature.setMaximumSize(QtCore.QSize(70, 16777215))
        self.ambient_temperature.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ambient_temperature.setMaximum(100000)
        self.ambient_temperature.setObjectName("ambient_temperature")
        self.horizontalLayout_20.addWidget(self.ambient_temperature)
        self.gridLayout.addLayout(self.horizontalLayout_20, 5, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.thermal_setup_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_continue = QtWidgets.QPushButton(Dialog)
        self.btn_continue.setDefault(True)
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Thermal Setup", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Thermal Setup</span></p></body></html>", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Dialog", "Model Select:", None, -1))
        self.combo_model_select.setItemText(0, QtWidgets.QApplication.translate("Dialog", "ParaPower", None, -1))
        self.combo_model_select.setItemText(1, QtWidgets.QApplication.translate("Dialog", "TSFM", None, -1))
        self.combo_model_select.setItemText(2, QtWidgets.QApplication.translate("Dialog", "Analytical", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Dialog", "Measure Name:", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "Device", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "Power", None, -1))
        self.btn_add_device.setText(QtWidgets.QApplication.translate("Dialog", "Add Device", None, -1))
        self.btn_remove_device.setText(QtWidgets.QApplication.translate("Dialog", "Remove Device", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("Dialog", "Heat Convection:", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Dialog", "Ambient Temperature:", None, -1))
        self.ambient_temperature.setSpecialValueText(QtWidgets.QApplication.translate("Dialog", "300", None, -1))
        self.btn_continue.setText(QtWidgets.QApplication.translate("Dialog", "Continue", None, -1))
