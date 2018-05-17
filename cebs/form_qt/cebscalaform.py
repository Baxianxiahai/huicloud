# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cebsCalaForm.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cebsCalaForm(object):
    def setupUi(self, cebsCalaForm):
        cebsCalaForm.setObjectName("cebsCalaForm")
        cebsCalaForm.resize(999, 596)
        self.pushButton_cala_test1 = QtWidgets.QPushButton(cebsCalaForm)
        self.pushButton_cala_test1.setGeometry(QtCore.QRect(50, 60, 161, 71))
        self.pushButton_cala_test1.setObjectName("pushButton_cala_test1")
        self.pushButton_cala_close = QtWidgets.QPushButton(cebsCalaForm)
        self.pushButton_cala_close.setGeometry(QtCore.QRect(250, 60, 161, 71))
        self.pushButton_cala_close.setObjectName("pushButton_cala_close")

        self.retranslateUi(cebsCalaForm)
        self.pushButton_cala_close.clicked.connect(cebsCalaForm.slot_cala_close)
        QtCore.QMetaObject.connectSlotsByName(cebsCalaForm)

    def retranslateUi(self, cebsCalaForm):
        _translate = QtCore.QCoreApplication.translate
        cebsCalaForm.setWindowTitle(_translate("cebsCalaForm", "CALIBRATION"))
        self.pushButton_cala_test1.setText(_translate("cebsCalaForm", "测试1"))
        self.pushButton_cala_close.setText(_translate("cebsCalaForm", "完成"))

