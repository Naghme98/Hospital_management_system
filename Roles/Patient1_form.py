
from PyQt5 import QtWidgets
from UI.showdoctimesform_form import Ui_ShowTimes
from DataBase.Patient_Connecter import PatentConnectors

#import other pages you want to go from this page

class ShowTimesWidget(QtWidgets.QWidget,Ui_ShowTimes ):
    P = PatentConnectors()
    def __init__(self, central_widget, parent=None):
        super(ShowTimesWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.setup()

    def loadData(self):
        c = self.P.show_doc()
        for x in c:
            s = str(x[0])+" متخصص "+str(x[1])
            self.Doctorname.addItem(s)


    def clicked_get_d_name(self):
        i =str(self.Doctorname.currentIndex())
        self.show_times(i)

    def show_times(self,i):
        list = self.P.show_times(i)
        self.doctorTimeViwe.setRowCount(0)
        for rownumber ,rowdata in enumerate(list):
            self.doctorTimeViwe.insertRow(rownumber)
            self.doctorTimeViwe.setItem(rownumber,0,QtWidgets.QTableWidgetItem(str(rowdata[0])))
        self.doctorTimeViwe.resizeColumnsToContents()
        self.doctorTimeViwe.resizeRowsToContents()

    def setup(self):
        self.loadData()
        self.getDoctorName.clicked.connect(self.clicked_get_d_name)

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self



