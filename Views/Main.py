# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTime = QtWidgets.QLabel(self.centralwidget)
        self.lblTime.setGeometry(QtCore.QRect(0, 0, 471, 181))
        font = QtGui.QFont()
        font.setPointSize(107)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.lblDate = QtWidgets.QLabel(self.centralwidget)
        self.lblDate.setGeometry(QtCore.QRect(0, 180, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(66)
        self.lblDate.setFont(font)
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTime.setText(_translate("MainWindow", "TIME"))
        self.lblDate.setText(_translate("MainWindow", "DATE"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())