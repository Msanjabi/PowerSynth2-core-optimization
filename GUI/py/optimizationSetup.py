# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/optimizationSetup.ui',
# licensing of 'ui/optimizationSetup.ui' applies.
#
# Created: Sun Oct 10 16:29:28 2021
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_generation_setup_frame_2 = QtWidgets.QFrame(Dialog)
        self.layout_generation_setup_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layout_generation_setup_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layout_generation_setup_frame_2.setObjectName("layout_generation_setup_frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layout_generation_setup_frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.floor_plan_x = QtWidgets.QLineEdit(self.layout_generation_setup_frame_2)
        self.floor_plan_x.setObjectName("floor_plan_x")
        self.horizontalLayout_8.addWidget(self.floor_plan_x)
        self.label_13 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(10, 0))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.floor_plan_y = QtWidgets.QLineEdit(self.layout_generation_setup_frame_2)
        self.floor_plan_y.setObjectName("floor_plan_y")
        self.gridLayout.addWidget(self.floor_plan_y, 1, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_24 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_17.addWidget(self.label_24)
        self.checkbox_plot_solutions = QtWidgets.QCheckBox(self.layout_generation_setup_frame_2)
        self.checkbox_plot_solutions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkbox_plot_solutions.setText("")
        self.checkbox_plot_solutions.setChecked(True)
        self.checkbox_plot_solutions.setObjectName("checkbox_plot_solutions")
        self.horizontalLayout_17.addWidget(self.checkbox_plot_solutions)
        self.gridLayout.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.layout_generation_setup_frame_2)
        self.layout_generation_setup_frame = QtWidgets.QFrame(Dialog)
        self.layout_generation_setup_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layout_generation_setup_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layout_generation_setup_frame.setObjectName("layout_generation_setup_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layout_generation_setup_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.combo_layout_mode = QtWidgets.QComboBox(self.layout_generation_setup_frame)
        self.combo_layout_mode.setObjectName("combo_layout_mode")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.horizontalLayout_7.addWidget(self.combo_layout_mode)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 2, 0, 1, 2)
        self.num_layouts = QtWidgets.QLineEdit(self.layout_generation_setup_frame)
        self.num_layouts.setObjectName("num_layouts")
        self.gridLayout_3.addWidget(self.num_layouts, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 3, 1, 1, 1)
        self.seed = QtWidgets.QLineEdit(self.layout_generation_setup_frame)
        self.seed.setObjectName("seed")
        self.gridLayout_3.addWidget(self.seed, 3, 2, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.combo_optimization_algorithm = QtWidgets.QComboBox(self.layout_generation_setup_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_optimization_algorithm.sizePolicy().hasHeightForWidth())
        self.combo_optimization_algorithm.setSizePolicy(sizePolicy)
        self.combo_optimization_algorithm.setMaximumSize(QtCore.QSize(110, 16777215))
        self.combo_optimization_algorithm.setObjectName("combo_optimization_algorithm")
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.addItem("")
        self.horizontalLayout_11.addWidget(self.combo_optimization_algorithm)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 5, 0, 1, 3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.layout_generation_setup_frame)
        self.electrical_thermal_frame = QtWidgets.QFrame(Dialog)
        self.electrical_thermal_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.electrical_thermal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.electrical_thermal_frame.setObjectName("electrical_thermal_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.electrical_thermal_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_electrical_setup = QtWidgets.QPushButton(self.electrical_thermal_frame)
        self.btn_electrical_setup.setObjectName("btn_electrical_setup")
        self.gridLayout_2.addWidget(self.btn_electrical_setup, 0, 0, 1, 1)
        self.btn_thermal_setup = QtWidgets.QPushButton(self.electrical_thermal_frame)
        self.btn_thermal_setup.setObjectName("btn_thermal_setup")
        self.gridLayout_2.addWidget(self.btn_thermal_setup, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.electrical_thermal_frame)
        self.btn_run_powersynth = QtWidgets.QPushButton(Dialog)
        self.btn_run_powersynth.setDefault(True)
        self.btn_run_powersynth.setObjectName("btn_run_powersynth")
        self.verticalLayout.addWidget(self.btn_run_powersynth)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Optimization Setup", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Macro Script Setup:</span></p></body></html>", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Dialog", "Floor Plan:", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Dialog", "X", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Dialog", "Plot Solution:", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Layout Generation Setup:</span></p></body></html>", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Dialog", "Layout_Mode:", None, -1))
        self.combo_layout_mode.setItemText(0, QtWidgets.QApplication.translate("Dialog", "minimum-sized solutions", None, -1))
        self.combo_layout_mode.setItemText(1, QtWidgets.QApplication.translate("Dialog", "variable-sized solutions", None, -1))
        self.combo_layout_mode.setItemText(2, QtWidgets.QApplication.translate("Dialog", "fixed-sized solutions", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Dialog", "Number of layouts/generation:", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Dialog", "Seed:", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Dialog", "Optimization Algorithm:", None, -1))
        self.combo_optimization_algorithm.setItemText(0, QtWidgets.QApplication.translate("Dialog", "NG-RANDOM", None, -1))
        self.combo_optimization_algorithm.setItemText(1, QtWidgets.QApplication.translate("Dialog", "NSGAII", None, -1))
        self.btn_electrical_setup.setText(QtWidgets.QApplication.translate("Dialog", "Open Electrical Setup", None, -1))
        self.btn_thermal_setup.setText(QtWidgets.QApplication.translate("Dialog", "Open Thermal Setup", None, -1))
        self.btn_run_powersynth.setText(QtWidgets.QApplication.translate("Dialog", "Run Powersynth", None, -1))

