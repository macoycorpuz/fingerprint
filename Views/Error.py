# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(480, 320)
        self.lblError = QtWidgets.QLabel(errorDialog)
        self.lblError.setGeometry(QtCore.QRect(0, 30, 471, 281))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblError.setFont(font)
        self.lblError.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblError.setObjectName("lblError")

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("errorDialog", "errorDialog"))
        self.lblError.setText(_translate("errorDialog", "<Error Code>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorDialog = QtWidgets.QDialog()
    ui = Ui_errorDialog()
    ui.setupUi(errorDialog)
    errorDialog.show()
    sys.exit(app.exec_())
