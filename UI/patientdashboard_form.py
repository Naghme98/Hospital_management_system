# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientdashboard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_patientD(object):
    def setupUi(self, patientD):
        patientD.setObjectName("patientD")
        patientD.resize(500, 415)
        self.ax = QtWidgets.QLabel(patientD)
        self.ax.setGeometry(QtCore.QRect(-2, -125, 521, 666))
        self.ax.setText("")
        self.ax.setPixmap(QtGui.QPixmap("UI/blur-hospital_1203-7974.jpg"))
        self.ax.setObjectName("ax")
        self.wellcom = QtWidgets.QLabel(patientD)
        self.wellcom.setGeometry(QtCore.QRect(170, 40, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.wellcom.setFont(font)
        self.wellcom.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgbrgba(214, 193, 171, 255)\n"
"\n"
"")
        self.wellcom.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom.setObjectName("wellcom")
        self.getTime = QtWidgets.QPushButton(patientD)
        self.getTime.setGeometry(QtCore.QRect(290, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.getTime.setFont(font)
        self.getTime.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));")
        self.getTime.setObjectName("getTime")
        self.visitPresc = QtWidgets.QPushButton(patientD)
        self.visitPresc.setGeometry(QtCore.QRect(290, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.visitPresc.setFont(font)
        self.visitPresc.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));\n"
"")
        self.visitPresc.setObjectName("visitPresc")
        self.bedInfo = QtWidgets.QPushButton(patientD)
        self.bedInfo.setGeometry(QtCore.QRect(290, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bedInfo.setFont(font)
        self.bedInfo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));")
        self.bedInfo.setObjectName("bedInfo")
        self.History = QtWidgets.QPushButton(patientD)
        self.History.setGeometry(QtCore.QRect(73, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.History.setFont(font)
        self.History.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));")
        self.History.setObjectName("History")
        self.chat = QtWidgets.QPushButton(patientD)
        self.chat.setGeometry(QtCore.QRect(73, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chat.setFont(font)
        self.chat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));")
        self.chat.setObjectName("chat")
        self.changeInfo = QtWidgets.QPushButton(patientD)
        self.changeInfo.setGeometry(QtCore.QRect(73, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.changeInfo.setFont(font)
        self.changeInfo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));")
        self.changeInfo.setObjectName("changeInfo")

        self.retranslateUi(patientD)
        QtCore.QMetaObject.connectSlotsByName(patientD)

    def retranslateUi(self, patientD):
        _translate = QtCore.QCoreApplication.translate
        patientD.setWindowTitle(_translate("patientD", "Dialog"))
        self.wellcom.setText(_translate("patientD", "خوش آمدید"))
        self.getTime.setText(_translate("patientD", "گرفتن نوبت"))
        self.visitPresc.setText(_translate("patientD", "مشاهده نسخه ها"))
        self.bedInfo.setText(_translate("patientD", "اطلاعات بستری شدن"))
        self.History.setText(_translate("patientD", "مشاهده سوابق"))
        self.chat.setText(_translate("patientD", "پیام ها"))
        self.changeInfo.setText(_translate("patientD", "اصلاح اطلاعات"))

