# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 580, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI/D1736762T14006492(web)(b).jpg"))
        self.label.setObjectName("label")
        self.wellcom = QtWidgets.QLabel(Form)
        self.wellcom.setGeometry(QtCore.QRect(140, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.wellcom.setFont(font)
        self.wellcom.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.wellcom.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom.setObjectName("wellcom")
        self.wellcom_2 = QtWidgets.QLabel(Form)
        self.wellcom_2.setGeometry(QtCore.QRect(280, 90, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_2.setFont(font)
        self.wellcom_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_2.setObjectName("wellcom_2")
        self.wellcom_3 = QtWidgets.QLabel(Form)
        self.wellcom_3.setGeometry(QtCore.QRect(280, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_3.setFont(font)
        self.wellcom_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_3.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_3.setObjectName("wellcom_3")
        self.wellcom_4 = QtWidgets.QLabel(Form)
        self.wellcom_4.setGeometry(QtCore.QRect(280, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_4.setFont(font)
        self.wellcom_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_4.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_4.setObjectName("wellcom_4")
        self.wellcom_5 = QtWidgets.QLabel(Form)
        self.wellcom_5.setGeometry(QtCore.QRect(280, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_5.setFont(font)
        self.wellcom_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_5.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_5.setObjectName("wellcom_5")
        self.wellcom_6 = QtWidgets.QLabel(Form)
        self.wellcom_6.setGeometry(QtCore.QRect(280, 240, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_6.setFont(font)
        self.wellcom_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_6.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_6.setObjectName("wellcom_6")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(62, 90, 151, 41))
        self.name.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.name.setObjectName("name")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(60, 190, 151, 41))
        self.email.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.email.setObjectName("email")
        self.role = QtWidgets.QComboBox(Form)
        self.role.setGeometry(QtCore.QRect(60, 250, 151, 41))
        self.role.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"\n"
"")
        self.role.setObjectName("role")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(60, 140, 151, 41))
        self.phone.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.phone.setObjectName("phone")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(60, 300, 151, 41))
        self.password.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.signup_1 = QtWidgets.QPushButton(Form)
        self.signup_1.setGeometry(QtCore.QRect(183, 351, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.signup_1.setFont(font)
        self.signup_1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"\n"
"")
        self.signup_1.setObjectName("signup_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wellcom.setText(_translate("Form", "فرم ثبت نام"))
        self.wellcom_2.setText(_translate("Form", "نام و نام خانوادگی:"))
        self.wellcom_3.setText(_translate("Form", "شماره تماس:"))
        self.wellcom_4.setText(_translate("Form", "آدرس پست الکترونیکی:"))
        self.wellcom_5.setText(_translate("Form", "رمز عبور:"))
        self.wellcom_6.setText(_translate("Form", "عنوان ثبت نام:"))
        self.role.setItemText(0, _translate("Form", "بیمار"))
        self.role.setItemText(1, _translate("Form", "پزشک"))
        self.role.setItemText(2, _translate("Form", "پرستار"))
        self.role.setItemText(3, _translate("Form", "حسابدار"))
        self.role.setItemText(4, _translate("Form", "مسئول داروخانه"))
        self.role.setItemText(5, _translate("Form", "مسئول پذیرش"))
        self.role.setItemText(6, _translate("Form", "مسئول آزمایشگاه"))
        self.signup_1.setText(_translate("Form", "ادامه"))

