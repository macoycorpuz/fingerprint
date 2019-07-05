import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Admin import Ui_AdminWindow
from Views.Main import Ui_MainWindow
from Views.Timed import Ui_TimedWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
AdminWindow = QtWidgets.QMainWindow()
TimedWindow = QtWidgets.QMainWindow()
    
def show_main_window():
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

def show_admin_window():
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()

def show_timed_window():
    ui = Ui_TimedWindow()
    ui.setupUi(TimedWindow)
    TimedWindow.show()


if __name__ == "__main__":
    show_main_window()
    sys.exit(app.exec_())
     