from PyQt5 import QtWidgets
from Roles.SignUp import SignUpWidget
from Roles.Patient1_form import ShowTimesWidget
from Roles.PatientDashBord import PatientDashbordWidget
import mysql.connector


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = SignUpWidget( self.central_widget, self)
        # login_widget = ShowTimesWidget(self.central_widget, self)
        #login_widget = PatientDashbordWidget(self.central_widget, self)
        self.central_widget.addWidget(login_widget)


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
