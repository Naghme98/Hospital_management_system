# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup2.1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signup2_form(object):
    def setupUi(self, signup2_form):
        signup2_form.setObjectName("signup2_form")
        signup2_form.resize(580, 480)
        self.label = QtWidgets.QLabel(signup2_form)
        self.label.setGeometry(QtCore.QRect(-2, 0, 581, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI/D1736762T14006492(web)(b).jpg"))
        self.label.setObjectName("label")
        self.endSignup1 = QtWidgets.QPushButton(signup2_form)
        self.endSignup1.setGeometry(QtCore.QRect(210, 200, 151, 51))
        self.endSignup1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.endSignup1.setObjectName("endSignup1")
        self.wellcom_2 = QtWidgets.QLabel(signup2_form)
        self.wellcom_2.setGeometry(QtCore.QRect(190, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.wellcom_2.setFont(font)
        self.wellcom_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_2.setObjectName("wellcom_2")
        self.wellcom_3 = QtWidgets.QLabel(signup2_form)
        self.wellcom_3.setGeometry(QtCore.QRect(20, 120, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_3.setFont(font)
        self.wellcom_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_3.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_3.setObjectName("wellcom_3")

        self.retranslateUi(signup2_form)
        QtCore.QMetaObject.connectSlotsByName(signup2_form)

    def retranslateUi(self, signup2_form):
        _translate = QtCore.QCoreApplication.translate
        signup2_form.setWindowTitle(_translate("signup2_form", "Dialog"))
        self.endSignup1.setText(_translate("signup2_form", "بازگشت به صفحه اصلی"))
        self.wellcom_2.setText(_translate("signup2_form", "فرم ثبت نام "))
        self.wellcom_3.setText(_translate("signup2_form", "کاربر گرامی، در صورت تایید ثبت نام ، نام کاربری شما به آدرس پستی تان ارسال خواهد شد"))

