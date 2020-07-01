# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autorize.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from regi import Ui_Form
from interf import Ui_MainWindow2

import codecs
import easygui
import tkinter
from tkinter import messagebox
import re
import random
import docx
import os
import time


class Ui_MainWindow(object):

    def openWindow(self):

        #Открываем окно РЕГИСТРАЦИИ

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def login (self):

        root=tkinter.Tk()
        root.withdraw()
        os.chdir(r"C:/Users/petuh/Desktop/Программа/Пароли")

        a=self.lineEdit_2.text()
        search=open('LOGIN.txt','r')
        text=search.read()
        search.close()
        y=(str(text).find(str(a)))
        if y!=-1:

            a=self.lineEdit.text()
            search=open('PAROL.txt','r')
            text=search.read()
            search.close()
            x=(str(text).find(str(a)))
            if x!=-1:
                #Открываем окно ЛИЧНОГО КАБИНЕТА ЭКСПЕРТА
                os.chdir(r"C:/Users/petuh/Desktop/Программа")

                createfile=open('vremennayahuynya.txt','w')
                createfile.write(self.lineEdit_2.text()+'\n'+self.lineEdit.text())
                createfile.close()
                time.sleep(2)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow2()
                self.ui.setupUi(self.window)
                self.window.show()

            else:
                messagebox.showinfo('','Неверный логин или пароль')
        else:
            messagebox.showinfo('','Неверный логин или пароль')


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 156)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)


        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.login)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "АВТОРИЗАЦИЯ"))
        self.label_3.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_2.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.pushButton.setText(_translate("MainWindow", "ЗАРЕГИСТРИРОВАТЬСЯ"))
        self.pushButton_3.setText(_translate("MainWindow", "ВОЙТИ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
