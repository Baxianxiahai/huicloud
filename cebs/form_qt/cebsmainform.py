# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cebsMainform.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cebsMainWindow(object):
    def setupUi(self, cebsMainWindow):
        cebsMainWindow.setObjectName("cebsMainWindow")
        cebsMainWindow.resize(1197, 637)
        self.centralwidget = QtWidgets.QWidget(cebsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cebs_textEdit_runProgress = QtWidgets.QTextEdit(self.centralwidget)
        self.cebs_textEdit_runProgress.setGeometry(QtCore.QRect(220, 80, 641, 241))
        self.cebs_textEdit_runProgress.setObjectName("cebs_textEdit_runProgress")
        self.cebs_pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.cebs_pushButton_start.setGeometry(QtCore.QRect(60, 60, 111, 111))
        self.cebs_pushButton_start.setObjectName("cebs_pushButton_start")
        self.cebs_label_runProgress = QtWidgets.QLabel(self.centralwidget)
        self.cebs_label_runProgress.setGeometry(QtCore.QRect(220, 60, 261, 16))
        self.cebs_label_runProgress.setObjectName("cebs_label_runProgress")
        self.cebs_pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.cebs_pushButton_stop.setGeometry(QtCore.QRect(60, 210, 111, 111))
        self.cebs_pushButton_stop.setObjectName("cebs_pushButton_stop")
        cebsMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cebsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        cebsMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cebsMainWindow)
        self.statusbar.setObjectName("statusbar")
        cebsMainWindow.setStatusBar(self.statusbar)
        self.actionSTART = QtWidgets.QAction(cebsMainWindow)
        self.actionSTART.setObjectName("actionSTART")
        self.actionSTOP = QtWidgets.QAction(cebsMainWindow)
        self.actionSTOP.setObjectName("actionSTOP")
        self.actionEXIT = QtWidgets.QAction(cebsMainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.actionABOUT = QtWidgets.QAction(cebsMainWindow)
        self.actionABOUT.setObjectName("actionABOUT")
        self.menu.addAction(self.actionSTART)
        self.menu.addAction(self.actionSTOP)
        self.menu_2.addAction(self.actionEXIT)
        self.menu_2.addAction(self.actionABOUT)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(cebsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(cebsMainWindow)

    def retranslateUi(self, cebsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        cebsMainWindow.setWindowTitle(_translate("cebsMainWindow", "CEBS SYSTEM"))
        self.cebs_textEdit_runProgress.setHtml(_translate("cebsMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; 2018/5/2 15:30:99 系统启动</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; 2018/5/2 15:40:55 启动执行命令 </p></body></html>"))
        self.cebs_pushButton_start.setText(_translate("cebsMainWindow", "启动"))
        self.cebs_label_runProgress.setText(_translate("cebsMainWindow", "运行进展"))
        self.cebs_pushButton_stop.setText(_translate("cebsMainWindow", "停止"))
        self.menu.setTitle(_translate("cebsMainWindow", "控制命令"))
        self.menu_2.setTitle(_translate("cebsMainWindow", "系统设置"))
        self.actionSTART.setText(_translate("cebsMainWindow", "START"))
        self.actionSTOP.setText(_translate("cebsMainWindow", "STOP"))
        self.actionEXIT.setText(_translate("cebsMainWindow", "EXIT"))
        self.actionABOUT.setText(_translate("cebsMainWindow", "ABOUT"))

