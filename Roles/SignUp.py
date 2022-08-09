
from PyQt5 import QtWidgets
from UI.signup_form import Ui_Form
from DataBase.Connectors import Connectors
from Roles.Signup2_1 import SignUp2_1Widget
from Roles.Signup2_2 import SignUp2_2Widget
#import other pages you want to go from this page

class SignUpWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, central_widget, parent=None):
        super(SignUpWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.setup()

    def setup(self):
        self.signup_1.clicked.connect(self.xx)

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

    def xx (self):
        self.hide()
        name = self.name.text()
        pas = self.password.text()
        e  = self.email.text()
        p = self.phone.text()

        roleId = str(int(self.role.currentIndex())+2)
        print("role",roleId)
        print("name:",name)
        print("pas:",pas)
        print("email",e)
        print("phone",p)
        #--------------------------------------------------------HERE
        if roleId == '3' or roleId == '4' or roleId == '6' or roleId == '8' or roleId == 5:
            signUp2_2 = SignUp2_2Widget(name, pas, e, p, roleId,self.central_widget)
            self.central_widget.addWidget(signUp2_2)
            self.central_widget.setCurrentWidget(signUp2_2)
            #-------------------------------------------------------------
        else:
            Connectors().insert_new_person(name,pas,e,p,'NULL',roleId,'NULL')
            signUp2_1 = SignUp2_1Widget(self.central_widget, self)
            self.central_widget.addWidget(signUp2_1)
            self.central_widget.setCurrentWidget(signUp2_1)


