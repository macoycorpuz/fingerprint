from PyQt5 import QtCore
from datetime import datetime
from Views.Main import Ui_MainWindow

class MainController(object):
    def initialize(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        timer = QtCore.QTimer()
        timer.timeout.connect(update_time)
        timer.start(50)

    def update_time(self):
        self.now=datetime.now()
        self.currentTime=now.strftime("%I:%M:%S %p")
        self.currentDate=now.strftime("%b, %d %Y")
        self.ui.lblTime.setText(currentTime)
        self.ui.lblDate.setText(currentDate)