# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEW_UI/ui/optimizationSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layout_generation_setup_frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.layout_generation_setup_frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.floor_plan_x = QtWidgets.QSpinBox(self.layout_generation_setup_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_plan_x.sizePolicy().hasHeightForWidth())
        self.floor_plan_x.setSizePolicy(sizePolicy)
        self.floor_plan_x.setMaximumSize(QtCore.QSize(50, 16777215))
        self.floor_plan_x.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.floor_plan_x.setMinimum(50)
        self.floor_plan_x.setMaximum(999)
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
        self.floor_plan_y = QtWidgets.QSpinBox(self.layout_generation_setup_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floor_plan_y.sizePolicy().hasHeightForWidth())
        self.floor_plan_y.setSizePolicy(sizePolicy)
        self.floor_plan_y.setMaximumSize(QtCore.QSize(50, 16777215))
        self.floor_plan_y.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.floor_plan_y.setMinimum(50)
        self.floor_plan_y.setMaximum(999)
        self.floor_plan_y.setObjectName("floor_plan_y")
        self.horizontalLayout_8.addWidget(self.floor_plan_y)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.verticalLayout.addWidget(self.layout_generation_setup_frame_2)
        self.layout_generation_setup_frame = QtWidgets.QFrame(Dialog)
        self.layout_generation_setup_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layout_generation_setup_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layout_generation_setup_frame.setObjectName("layout_generation_setup_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layout_generation_setup_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.num_layouts = QtWidgets.QSpinBox(self.layout_generation_setup_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_layouts.sizePolicy().hasHeightForWidth())
        self.num_layouts.setSizePolicy(sizePolicy)
        self.num_layouts.setMinimumSize(QtCore.QSize(15, 0))
        self.num_layouts.setMaximumSize(QtCore.QSize(50, 16777215))
        self.num_layouts.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.num_layouts.setMaximum(9999)
        self.num_layouts.setObjectName("num_layouts")
        self.horizontalLayout_9.addWidget(self.num_layouts)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.seed = QtWidgets.QSpinBox(self.layout_generation_setup_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seed.sizePolicy().hasHeightForWidth())
        self.seed.setSizePolicy(sizePolicy)
        self.seed.setMinimumSize(QtCore.QSize(15, 0))
        self.seed.setMaximumSize(QtCore.QSize(50, 16777215))
        self.seed.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.seed.setMaximum(999)
        self.seed.setObjectName("seed")
        self.horizontalLayout_10.addWidget(self.seed)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
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
        self.horizontalLayout_11.addWidget(self.combo_optimization_algorithm)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QtWidgets.QLabel(self.layout_generation_setup_frame)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_13.addWidget(self.label_19)
        self.num_generations = QtWidgets.QSpinBox(self.layout_generation_setup_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_generations.sizePolicy().hasHeightForWidth())
        self.num_generations.setSizePolicy(sizePolicy)
        self.num_generations.setMinimumSize(QtCore.QSize(15, 0))
        self.num_generations.setMaximumSize(QtCore.QSize(50, 16777215))
        self.num_generations.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.num_generations.setMaximum(999)
        self.num_generations.setProperty("value", 100)
        self.num_generations.setDisplayIntegerBase(10)
        self.num_generations.setObjectName("num_generations")
        self.horizontalLayout_13.addWidget(self.num_generations)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addWidget(self.layout_generation_setup_frame)
        self.electrical_thermal_frame = QtWidgets.QFrame(Dialog)
        self.electrical_thermal_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.electrical_thermal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.electrical_thermal_frame.setObjectName("electrical_thermal_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.electrical_thermal_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_electrical_setup = QtWidgets.QPushButton(self.electrical_thermal_frame)
        self.btn_electrical_setup.setObjectName("btn_electrical_setup")
        self.horizontalLayout.addWidget(self.btn_electrical_setup)
        self.btn_thermal_setup = QtWidgets.QPushButton(self.electrical_thermal_frame)
        self.btn_thermal_setup.setObjectName("btn_thermal_setup")
        self.horizontalLayout.addWidget(self.btn_thermal_setup)
        self.verticalLayout.addWidget(self.electrical_thermal_frame)
        self.btn_run_powersynth = QtWidgets.QPushButton(Dialog)
        self.btn_run_powersynth.setDefault(True)
        self.btn_run_powersynth.setObjectName("btn_run_powersynth")
        self.verticalLayout.addWidget(self.btn_run_powersynth)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Optimization Setup"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Macro Script Setup:</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "Floor Plan:"))
        self.label_13.setText(_translate("Dialog", "by"))
        self.label_24.setText(_translate("Dialog", "Plot Solution:"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Layout Generation Setup:</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "Layout_Mode:"))
        self.combo_layout_mode.setItemText(0, _translate("Dialog", "minimum-sized solutions"))
        self.combo_layout_mode.setItemText(1, _translate("Dialog", "variable-sized solutions"))
        self.combo_layout_mode.setItemText(2, _translate("Dialog", "fixed-sized solutions"))
        self.label_14.setText(_translate("Dialog", "Number of layouts:"))
        self.num_layouts.setSpecialValueText(_translate("Dialog", "25"))
        self.label_15.setText(_translate("Dialog", "Seed:"))
        self.seed.setSpecialValueText(_translate("Dialog", "10"))
        self.label_16.setText(_translate("Dialog", "Optimization Algorithm:"))
        self.combo_optimization_algorithm.setItemText(0, _translate("Dialog", "NG-RANDOM"))
        self.label_19.setText(_translate("Dialog", "Number of Generations:"))
        self.num_generations.setSpecialValueText(_translate("Dialog", "10"))
        self.btn_electrical_setup.setText(_translate("Dialog", "Open Electrical Setup"))
        self.btn_thermal_setup.setText(_translate("Dialog", "Open Thermal Setup"))
        self.btn_run_powersynth.setText(_translate("Dialog", "Run Powersynth"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

