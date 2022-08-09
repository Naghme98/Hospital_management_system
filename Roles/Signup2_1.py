from PyQt5 import QtWidgets
from UI.signup2_1_form import Ui_signup2_form
from DataBase.Connectors import Connectors
#import other pages you want to go from this page

class SignUp2_1Widget(QtWidgets.QWidget, Ui_signup2_form):
    def __init__(self, central_widget, parent=None):
        super(SignUp2_1Widget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        # self.setup()

    def setup(self):
        self.signup_1.clicked.connect(self.xx)

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self
