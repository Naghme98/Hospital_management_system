
from PyQt5 import QtWidgets
from UI.patientdashboard_form import Ui_patientD
from Roles.Patient1_form import ShowTimesWidget

#import other pages you want to go from this page

class PatientDashbordWidget(QtWidgets.QWidget, Ui_patientD):
    def __init__(self, central_widget, parent=None):
        super(PatientDashbordWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.setup()

    def setup(self):
        # self.visitPresc.clicked.connect()
        # self.chat.clicked.connect()
        self.getTime.clicked.connect(self.getTTime)
        # self.bedInfo.clicked.connect()
        # self.History.clicked.connect()
        # self.changeInfo.clicked.connect()

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

    def getTTime(self):
        self.hide()
        time_getting = ShowTimesWidget(self.central_widget)
        self.central_widget.addWidget(time_getting)
        self.central_widget.setCurrentWidget(time_getting)