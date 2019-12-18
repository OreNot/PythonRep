# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python_projects\p_1\src\MS\design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(218, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 219, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loginEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginEdit.setObjectName("loginEdit")
        self.horizontalLayout.addWidget(self.loginEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passEdit.setObjectName("passEdit")
        self.horizontalLayout_2.addWidget(self.passEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.countEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.countEdit.setObjectName("countEdit")
        self.horizontalLayout_3.addWidget(self.countEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.btnBrowse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.verticalLayout.addWidget(self.btnBrowse)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обращения"))
        self.label.setText(_translate("MainWindow", "Логин : "))
        self.label_2.setText(_translate("MainWindow", "Пароль : "))
        self.label_3.setText(_translate("MainWindow", "Количество : "))
        self.btnBrowse.setText(_translate("MainWindow", "Запуск"))

