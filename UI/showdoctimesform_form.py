# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showdoctimesform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShowTimes(object):
    def setupUi(self, ShowTimes):
        ShowTimes.setObjectName("ShowTimes")
        ShowTimes.resize(500, 415)
        ShowTimes.setMaximumSize(QtCore.QSize(500, 415))
        self.label = QtWidgets.QLabel(ShowTimes)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 415))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI/blur-hospital_1203-7974.jpg"))
        self.label.setObjectName("label")
        self.Doctorname = QtWidgets.QComboBox(ShowTimes)
        self.Doctorname.setGeometry(QtCore.QRect(70, 60, 191, 41))
        self.Doctorname.setObjectName("Doctorname")
        self.Doctorname.addItem("")
        self.wellcom = QtWidgets.QLabel(ShowTimes)
        self.wellcom.setGeometry(QtCore.QRect(280, 50, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wellcom.setFont(font)
        self.wellcom.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgbrgba(214, 193, 171, 255)\n"
"\n"
"")
        self.wellcom.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom.setObjectName("wellcom")
        self.getDoctorName = QtWidgets.QPushButton(ShowTimes)
        self.getDoctorName.setGeometry(QtCore.QRect(110, 100, 111, 31))
        self.getDoctorName.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));\n"
"\n"
"")
        self.getDoctorName.setObjectName("getDoctorName")
        self.reserv = QtWidgets.QPushButton(ShowTimes)
        self.reserv.setGeometry(QtCore.QRect(100, 340, 171, 31))
        self.reserv.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(214, 193, 171, 255));\n"
"\n"
"")
        self.reserv.setObjectName("reserv")
        self.doctorTimeViwe = QtWidgets.QTableWidget(ShowTimes)
        self.doctorTimeViwe.setGeometry(QtCore.QRect(30, 160, 291, 161))
        self.doctorTimeViwe.setStyleSheet("")
        self.doctorTimeViwe.setObjectName("doctorTimeViwe")
        self.doctorTimeViwe.setColumnCount(1)
        self.doctorTimeViwe.setRowCount(0)
        self.wellcom_2 = QtWidgets.QLabel(ShowTimes)
        self.wellcom_2.setGeometry(QtCore.QRect(330, 160, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wellcom_2.setFont(font)
        self.wellcom_2.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color:rgbrgba(214, 193, 171, 255)\n"
"\n"
"")
        self.wellcom_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcom_2.setObjectName("wellcom_2")

        self.retranslateUi(ShowTimes)
        QtCore.QMetaObject.connectSlotsByName(ShowTimes)

    def retranslateUi(self, ShowTimes):
        _translate = QtCore.QCoreApplication.translate
        ShowTimes.setWindowTitle(_translate("ShowTimes", "Form"))
        self.Doctorname.setItemText(0, _translate("ShowTimes", "----"))
        self.wellcom.setText(_translate("ShowTimes", "پزشک مورد نظر خود را انتخاب فرمایید"))
        self.getDoctorName.setText(_translate("ShowTimes", "تایید"))
        self.reserv.setText(_translate("ShowTimes", "رزرو"))
        self.wellcom_2.setText(_translate("ShowTimes", "زمان های حضور پزشک:"))

