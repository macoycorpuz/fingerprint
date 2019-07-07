import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Admin import Ui_AdminWindow
from Views.Main import Ui_MainWindow
from Views.Timed import Ui_TimedWindow
from Views.Status import Ui_StatusDialog
# import fingerprint
import database


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

# Set up in a thread
def statusMessage(message, color='green', t=5):
    StatusDialog.show()
    ui_status.lblStatus.setText(message)
    ui_status.lblStatus.setStyleSheet('color: ' + color)
    #Set Timer
    StatusDialog.close()

# Set up in a thread
def timedMessage(name, status, t):
    TimedWindow.show()
    ui_timed.lblName.setText(name)
    ui_timed.lblStatus.setText(status)
    ui_timed.lblTime.setText(t)
    #Set Timer
    TimedWindow.close()

def check_fingerprint():
    error, fingerId = f.searchFingerprint()
    if error:
        print("Error Message: %s"  % error)
        return statusMessage(error, 'red')
    
    # if db.isAdmin(fingerId):
    #     register_employee()
    # else:
    #     name, status = db.saveTime(fingerId)
    #     timedMessage(name, status, t)


# Initialize Events
ui_admin.btnCancel.clicked.connect(btnCancel_clicked)

if __name__ == "__main__":
    MainWindow.show()

    # Timer Loop
    timer = QtCore.QTimer()
    timer.timeout.connect(update_time)
    timer.start(1)

    # Run this in a different thread
    # Thread(check_fingerprint)
    check_fingerprint()

    sys.exit(app.exec_())
     