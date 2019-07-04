# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
import sys

class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lstEmployees = QtWidgets.QListView(self.centralwidget)
        self.lstEmployees.setGeometry(QtCore.QRect(0, 40, 471, 221))
        self.lstEmployees.setObjectName("lstEmployees")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(0, 262, 471, 31))
        self.btnCancel.setObjectName("btnCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Employee to Register:"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
