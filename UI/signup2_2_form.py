# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup2_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 450)
        self.degree_2 = QtWidgets.QLabel(Dialog)
        self.degree_2.setGeometry(QtCore.QRect(10, -20, 561, 451))
        self.degree_2.setText("")
        self.degree_2.setPixmap(QtGui.QPixmap("UI\D1736762T14006492(web)(b).jpg"))
        self.degree_2.setObjectName("degree_2")
        self.medicalCode = QtWidgets.QLineEdit(Dialog)
        self.medicalCode.setGeometry(QtCore.QRect(100, 120, 161, 41))
        self.medicalCode.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.medicalCode.setObjectName("medicalCode")
        self.degree = QtWidgets.QLineEdit(Dialog)
        self.degree.setGeometry(QtCore.QRect(102, 180, 151, 41))
        self.degree.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgb(130, 133, 133)\n"
"\n"
"")
        self.degree.setObjectName("degree")
        self.signup2_2 = QtWidgets.QPushButton(Dialog)
        self.signup2_2.setGeometry(QtCore.QRect(200, 270, 151, 51))
        self.signup2_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"\n"
"")
        self.signup2_2.setObjectName("signup2_2")
        self.wellcom_2 = QtWidgets.QLabel(Dialog)
        self.wellcom_2.setGeometry(QtCore.QRect(180, 30, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_2.setFont(font)
        self.wellcom_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_2.setObjectName("wellcom_2")
        self.wellcom_3 = QtWidgets.QLabel(Dialog)
        self.wellcom_3.setGeometry(QtCore.QRect(300, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_3.setFont(font)
        self.wellcom_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_3.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_3.setObjectName("wellcom_3")
        self.wellcom_4 = QtWidgets.QLabel(Dialog)
        self.wellcom_4.setGeometry(QtCore.QRect(300, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wellcom_4.setFont(font)
        self.wellcom_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(158, 169, 176, 248));\n"
"\n"
"")
        self.wellcom_4.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_4.setObjectName("wellcom_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signup2_2.setText(_translate("Dialog", "ثبت نهایی"))
        self.wellcom_2.setText(_translate("Dialog", "فرم ثبت نام"))
        self.wellcom_3.setText(_translate("Dialog", "شماره نظام پزشکی:"))
        self.wellcom_4.setText(_translate("Dialog", "مدرک تحصیلی:"))

