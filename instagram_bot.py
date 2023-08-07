from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import csv
import os
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 590)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(108, 108, 162);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_27 = QtWidgets.QFrame(self.centralwidget)
        self.frame_27.setGeometry(QtCore.QRect(0, 110, 861, 481))
        self.frame_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.checkBox = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox.setGeometry(QtCore.QRect(190, 220, 77, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox_2.setGeometry(QtCore.QRect(290, 220, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 220, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(260, 410, 100, 40))
        self.pushButton_18.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_18.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(33, 33, 50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(260, 150, 361, 40))
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_7.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(30, 10, 661, 100))
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_39.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_39.setObjectName("label_39")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(30, 150, 200, 40))
        self.pushButton_20.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_20.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(33, 33, 50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(30, 230, 220, 40))
        self.pushButton_21.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_21.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(33, 33, 50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 230, 361, 40))
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_8.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Hashtag"))
        self.checkBox_2.setText(_translate("MainWindow", "User"))
        self.checkBox_3.setText(_translate("MainWindow", "Likes"))
        self.pushButton_18.setText(_translate("MainWindow", "Start"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Insta Bot</span></p></body></html>"))
        self.pushButton_20.setText(_translate("MainWindow", "Upload Login File"))
        self.pushButton_21.setText(_translate("MainWindow", "Upload User Name"))

class MainWindow(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.setWindowTitle('')
                self.ui.setupUi(self)
                self.ui.pushButton_20.clicked.connect(self.select_login_file)
                self.ui.pushButton_21.clicked.connect(self.select_username_file)
                self.ui.pushButton_18.clicked.connect(self.login)
                
        def select_login_file(self):
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
                if file_path:
                        print(file_path)
                        self.ui.lineEdit_7.setText(file_path)

        def select_username_file(self):
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
                if file_path:
                        print(file_path)
                        self.ui.lineEdit_8.setText(file_path)


        def login(self, file_path):
                
                df = pd.read_csv(file_path)
                id=df.split(',,')
                ide=id[0]
                password=id[1]
                print(ide)
                print(password)
                        


from sys import exit as sysExit         

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())