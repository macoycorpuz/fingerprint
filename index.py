import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Admin import Ui_AdminWindow
from Views.Main import Ui_MainWindow
from Views.Timed import Ui_TimedWindow
from Views.Status import Ui_StatusDialog
from fingerprint import fingerprint
from database import database
from threading import Thread

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
AdminWindow = QtWidgets.QMainWindow()
TimedWindow = QtWidgets.QMainWindow()
StatusDialog = QtWidgets.QDialog()

ui_main = Ui_MainWindow()
ui_admin = Ui_AdminWindow()
ui_timed = Ui_TimedWindow()
ui_status = Ui_StatusDialog()

ui_main.setupUi(MainWindow)
ui_admin.setupUi(AdminWindow)
ui_timed.setupUi(TimedWindow)
ui_status.setupUi(StatusDialog)

f = fingerprint()
db = database()
isFingerprintRunning = True
isShowStatusDialog = False
isShowTimedWindow = False

def update_time():
    now=datetime.now()
    currentTime=now.strftime("%I:%M:%S %p")
    currentDate=now.strftime("%b, %d %Y")
    ui_main.lblTime.setText(currentTime)
    ui_main.lblDate.setText(currentDate)

def btnCancel_clicked():
    AdminWindow.close()
    isFingerprintRunning = True

def close_status_dialog():
    StatusDialog.close()
    isFingerprintRunning = True

def close_timed_dialog():
    TimedWindow.close()
    isFingerprintRunning = True

def statusMessage(message, color='green'):
    StatusDialog.show()
    ui_status.lblStatus.setText(message)
    ui_status.lblStatus.setStyleSheet('color: ' + color)
    isFingerprintRunning = False
    QtCore.QTimer.singleShot(5000, close_status_dialog)

def timedMessage(name, status):
    TimedWindow.show()
    ui_timed.lblName.setText(name)
    ui_timed.lblStatus.setText("Time %s:"  % status)
    ui_timed.lblTime.setText(datetime.now().strftime("%I:%M:%S %p"))
    isFingerprintRunning = False
    QtCore.QTimer.singleShot(5000, close_timed_dialog)

def register_employee():
    print("Wow Admin ka")
    AdminWindow.show()
    isFingerprintRunning = False

# def check_fingerprint():
#     while isFingerprintRunning:
#         try:
#             error, fingerId = f.searchFingerprint()
#             if db.isAdmin(fingerId):
#                 register_employee()
#             elif fingerId > 0:
#                 name, status = db.saveTime(fingerId)
#                 timedMessage(name, status)
#             elif error: raise Exception(error)
#         except Exception as e:
#             if "Communication" in str(e): continue
#             print("Error Message: %s"  % e)
#             statusMessage(error, 'red')

# Initialize Events
ui_admin.btnCancel.clicked.connect(btnCancel_clicked)

if __name__ == "__main__":
    MainWindow.show()

    timer = QtCore.QTimer()
    timer.timeout.connect(update_time)
    timer.start(1)

    statusMessage('error', 'red')
    # FingerprintThread = Thread(target=check_fingerprint)
    # FingerprintThread.start()

    sys.exit(app.exec_())
     