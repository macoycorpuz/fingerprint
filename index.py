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

# Initialize Libraries
f = fingerprint()
db = database()

# Update Time
def update_time():
    now=datetime.now()
    currentTime=now.strftime("%I:%M:%S %p")
    currentDate=now.strftime("%b, %d %Y")
    ui_main.lblTime.setText(currentTime)
    ui_main.lblDate.setText(currentDate)

# Cancel Button
def btnCancel_clicked():
    AdminWindow.close()

# PyQt Sleep
def timesleep(t):
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(t, loop.quit)
    loop.exec_()

def statusMessage(message, color='green', t=3000):
    StatusDialog.show()
    ui_status.lblStatus.setText(message)
    ui_status.lblStatus.setStyleSheet('color: ' + color)
    timesleep(t)
    StatusDialog.close()

def timedMessage(name, status, t=5000):
    TimedWindow.show()
    ui_timed.lblName.setText(name)
    ui_timed.lblStatus.setText("Time %s:"  % status)
    ui_timed.lblTime.setText(t)
    timesleep(t)
    TimedWindow.close()

def register_employee():
    print("Wow Admin ka")
    AdminWindow.show()
    FingerprintThread.exit()

def check_fingerprint():
    while True:
        try:
            error, fingerId = f.searchFingerprint()
            if error: raise Exception(error)
            # elif fingerId <= -1: raise Exception("No Fingerprint")
            print("FingerId: " + fingerId)
            if db.isAdmin(fingerId):
                register_employee()
            else:
                name, status = db.saveTime(fingerId)
                timedMessage(name, status)
        except Exception as e:
            if "Communication" in str(e): continue
            print("Error Message: %s"  % e)
            statusMessage(error, 'red')

# Initialize Events
ui_admin.btnCancel.clicked.connect(btnCancel_clicked)

if __name__ == "__main__":
    MainWindow.show()

    # Timer Loop
    timer = QtCore.QTimer()
    timer.timeout.connect(update_time)
    timer.start(1)

    FingerprintThread = Thread(target=check_fingerprint)
    FingerprintThread.start()

    sys.exit(app.exec_())
     