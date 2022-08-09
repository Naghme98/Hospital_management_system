# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nurse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 581, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../nurse.jpg"))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 88, 561, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_3 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_4.addWidget(self.listWidget_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addRButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.addRButton_3.setObjectName("addRButton_3")
        self.verticalLayout_3.addWidget(self.addRButton_3)
        self.deleteRButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteRButton_3.setObjectName("deleteRButton_3")
        self.verticalLayout_3.addWidget(self.deleteRButton_3)
        self.editRButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.editRButton_3.setObjectName("editRButton_3")
        self.verticalLayout_3.addWidget(self.editRButton_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, -10, 101, 91))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.layoutWidget.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addRButton_3.setText(_translate("MainWindow", "اضافه کردن گزارش"))
        self.deleteRButton_3.setText(_translate("MainWindow", "حذف گزارش"))
        self.editRButton_3.setText(_translate("MainWindow", "ویرایش گزارش"))
        self.label_2.setText(_translate("MainWindow", "پرستار"))

