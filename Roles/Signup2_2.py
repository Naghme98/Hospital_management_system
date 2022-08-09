from PyQt5 import QtWidgets
from UI.signup2_2_form import Ui_Dialog
from DataBase.Connectors import Connectors
from Roles.Signup2_1 import SignUp2_1Widget
#import other pages you want to go from this page


class SignUp2_2Widget(QtWidgets.QWidget, Ui_Dialog ):

    def __init__(self, name, pas, email, phone, role, central_widget, parent=None):
        super(SignUp2_2Widget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        print("role2: ", role)
        print("name2: ", name)
        print("pass2: ", pas)
        print("email:", email)
        print("phone", phone)
        print("--------------------")
        self.name = name
        self.passs = pas
        self.email = email
        self.phone = phone
        self.role = role
        self.setup()


    def setup(self):
        self.signup2_2.clicked.connect(self.setValue)

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

    def setValue (self):
        self.hide()
        Connectors().insert_new_person(self.name, self.passs,self.email,self.phone,self.medicalCode.text(), self.role, self.degree.text())
        signUp2_1 = SignUp2_1Widget(self.central_widget, self)
        self.central_widget.addWidget(signUp2_1)
        self.central_widget.setCurrentWidget(signUp2_1)
