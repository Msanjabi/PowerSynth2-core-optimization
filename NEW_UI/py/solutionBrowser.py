# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEW_UI/ui/solutionBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CornerStitch_Dialog(object):
    def setupUi(self, CornerStitch_Dialog):
        CornerStitch_Dialog.setObjectName("CornerStitch_Dialog")
        CornerStitch_Dialog.resize(1400, 920)
        self.gridLayout_7 = QtWidgets.QGridLayout(CornerStitch_Dialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.grbox_view = QtWidgets.QGroupBox(CornerStitch_Dialog)
        self.grbox_view.setMinimumSize(QtCore.QSize(600, 600))
        self.grbox_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grbox_view.setObjectName("grbox_view")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.grbox_view)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.grbox_view)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.grbox_view)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.gridLayout_8.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.grbox_view, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(CornerStitch_Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 0, 1, 1)
        self.grview_sols_browser = QtWidgets.QGraphicsView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grview_sols_browser.sizePolicy().hasHeightForWidth())
        self.grview_sols_browser.setSizePolicy(sizePolicy)
        self.grview_sols_browser.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.grview_sols_browser.setObjectName("grview_sols_browser")
        self.gridLayout_4.addWidget(self.grview_sols_browser, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 1, 1, 2)

        self.retranslateUi(CornerStitch_Dialog)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(CornerStitch_Dialog)

    def retranslateUi(self, CornerStitch_Dialog):
        _translate = QtCore.QCoreApplication.translate
        CornerStitch_Dialog.setWindowTitle(_translate("CornerStitch_Dialog", "Solution Browser "))
        self.grbox_view.setTitle(_translate("CornerStitch_Dialog", "Layout Visualization"))
        self.groupBox_4.setTitle(_translate("CornerStitch_Dialog", "Generated Layout"))
        self.groupBox_5.setTitle(_translate("CornerStitch_Dialog", "Input (initial) Layout"))
        self.groupBox_2.setTitle(_translate("CornerStitch_Dialog", "Layout Selection"))
        self.pushButton.setText(_translate("CornerStitch_Dialog", "Export Solution"))
        self.label.setText(_translate("CornerStitch_Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Click on the points above to view the respective layout.  Click on export solution below to export the selected layout.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CornerStitch_Dialog = QtWidgets.QDialog()
    ui = Ui_CornerStitch_Dialog()
    ui.setupUi(CornerStitch_Dialog)
    CornerStitch_Dialog.show()
    sys.exit(app.exec_())

