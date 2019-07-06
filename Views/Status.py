# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.resize(480, 320)
        self.lblStatus = QtWidgets.QLabel(StatusDialog)
        self.lblStatus.setGeometry(QtCore.QRect(0, 30, 471, 281))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblStatus.setObjectName("lblStatus")

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("StatusDialog", "StatusDialog"))
        self.lblStatus.setText(_translate("StatusDialog", "<Status Code>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatusDialog = QtWidgets.QDialog()
    ui = Ui_StatusDialog()
    ui.setupUi(StatusDialog)
    StatusDialog.show()
    sys.exit(app.exec_())
