# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timed_in.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimedWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(0, 0, 471, 131))
        font = QtGui.QFont()
        font.setPointSize(63)
        font.setBold(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(0, 120, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.lblTime = QtWidgets.QLabel(self.centralwidget)
        self.lblTime.setGeometry(QtCore.QRect(0, 190, 471, 101))
        font = QtGui.QFont()
        font.setPointSize(54)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblName.setText(_translate("MainWindow", "<name>"))
        self.lblStatus.setText(_translate("MainWindow", "<status>:"))
        self.lblTime.setText(_translate("MainWindow", "<time>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TimedWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
