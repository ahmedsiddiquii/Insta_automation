from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 580)
        MainWindow.setMinimumSize(QtCore.QSize(699, 580))
        MainWindow.setMaximumSize(QtCore.QSize(699, 580))
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
        self.checkBox.setGeometry(QtCore.QRect(190, 350, 77, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox_2.setGeometry(QtCore.QRect(290, 350, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 350, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_22.setGeometry(QtCore.QRect(30, 190, 220, 40))
        self.pushButton_22.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_22.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
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
        self.pushButton_22.setObjectName("pushButton_22")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 190, 361, 40))
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_9.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_23.setGeometry(QtCore.QRect(30, 270, 220, 40))
        self.pushButton_23.setMinimumSize(QtCore.QSize(220, 40))
        self.pushButton_23.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton {\n"
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
        self.pushButton_23.setObjectName("pushButton_23")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_10.setGeometry(QtCore.QRect(260, 270, 361, 40))
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_10.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(260, 510, 100, 40))
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
        self.pushButton_21.setGeometry(QtCore.QRect(30, 220, 220, 40))
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
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 220, 361, 40))
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
        self.pushButton_22.setText(_translate("MainWindow", "Hash Tag"))
        self.pushButton_23.setText(_translate("MainWindow", "Post"))
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
        self.ui.pushButton_22.clicked.connect(self.select_hashtag_file)
        self.ui.pushButton_23.clicked.connect(self.select_post_file)
        self.ui.pushButton_18.clicked.connect(self.main)

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
        file_path2, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path2:
            print(file_path2)
            self.ui.lineEdit_8.setText(file_path2)
    def select_hashtag_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path3, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path3:
            print(file_path3)
            self.ui.lineEdit_9.setText(file_path3)
    def select_post_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path4, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path4:
            print(file_path4)
            self.ui.lineEdit_10.setText(file_path4)       

    



    def main(self):
        # Get the file paths from the line edits
        file_path = self.ui.lineEdit_7.text()
        file_path2 = self.ui.lineEdit_8.text()
        file_path3 = self.ui.lineEdit_9.text()
        file_path4 = self.ui.lineEdit_10.text()

        # Call the login and user methods
        self.login(file_path,file_path2,file_path3,file_path4)
        

        

    def login(self, file_path,file_path2,file_path3,file_path4):
        ids=[]
        passwords=[]
        with open(file_path, 'r') as file:
                content = file.read()

                lines = content.splitlines()
                for line in lines:
                        id= line.split(',,')
                        ide=id[0]
                        pas=id[1]
                        ids.append(id[0])
                        passwords.append(id[1])
                        print(ide)
                        print(pas)
        
        for i in range(len(ids)):
                try:
                        self.driver = webdriver.Chrome()
                        self.driver.get("https://www.instagram.com/")
                        time.sleep(5)  
                        login_insta = self.driver.find_element(by='xpath',value=  '//input[@aria-label="Phone number, username, or email"]').send_keys(ids[i])
                        password= self.driver.find_element(by='xpath',value='//input[@type="password"]').send_keys(passwords[i])
                        time.sleep(5)
                        login= self.driver.find_element(by='xpath', value='//div//button[@class="_acan _acap _acas _aj1-"]').click()
                        time.sleep(10)
                except:
                        pass
                if self.ui.checkBox.isChecked():
                        self.tags(file_path3)
                if self.ui.checkBox_2.isChecked():
                        self.send_Post_users(file_path4)
                        
                if self.ui.checkBox_3.isChecked():
                        self.user(file_path2)

    def user(self, file_path2):
        print("user====user")
        with open(file_path2, 'r') as file:
            content = file.read()

            lines = content.splitlines()
            for line in lines:
                line=line
        for searches in lines:
                self.driver.get("https://www.instagram.com/direct/t")
                time.sleep(15)

                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Send message")]')
                send_message_button.click()
                time.sleep(5)
                self.driver.find_element(by='xpath',value='//input[@placeholder="Search..."]').send_keys(searches)
                time.sleep(5)
                self.driver.find_element(by='xpath',value='//div[@class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"]').click()
                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Chat")]')
                send_message_button.click()
                time.sleep(5)
                message_input= self.driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
                message_input.send_keys("hello")
                message_input.send_keys(Keys.ENTER)
               

    def send_Post_users(self,file_path4):
        print("message=====message")
        
        with open(file_path4, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            for line in lines:
                line=line
        for link in lines:
                self.driver.get(link)
                time.sleep(5)
                likes_button = self.driver.find_element(by='xpath', value='//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
                likes_button.click()
                time.sleep(5)
                temp = []
                likes_popup = self.driver.find_elements(by='xpath', value='//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]//a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 x1ykvv32 xougopr x159fomc xnp5s1o x194ut8o x1vzenxt xd7ygy7 xt298gk x1xrz1ek x1s928wv x1n449xj x2q1x1w x1j6awrg x162n7g1 x1m1drc7 x1ypdohk x4gyw5p _a6hd"]')
                for i in range(min(30, len(likes_popup))):
                        link = likes_popup[i].get_attribute("href")
                        
                        temp.append(link)
                        if len(set(temp)) >= 30:
                                break
                for link in temp:
                        link=link.split("/")
                        
                        try:
                                self.driver.get("https://www.instagram.com/direct/t")
                                time.sleep(15)
                                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Send message")]')
                                send_message_button.click()
                                time.sleep(5)
                                self.driver.find_element(by='xpath',value='//input[@placeholder="Search..."]').send_keys(link[3])
                                time.sleep(5)
                                self.driver.find_element(by='xpath',value='//div[@class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"]').click()
                                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Chat")]')
                                send_message_button.click()
                                time.sleep(5)
                                message_input= self.driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
                                message_input.send_keys("hello")
                                message_input.send_keys(Keys.ENTER)
                        except:
                                pass


    def tags(self,file_path3):
        print("tags=======tags")
        with open(file_path3, 'r') as file:
                content = file.read()

                lines = content.splitlines()
                for line in lines:
                        line=line     
        
        for tag in lines:
                tag=tag.replace('/n','')
                self.driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
                time.sleep(15)
                post = self.driver.find_element(by='xpath',value='//div[@class="_aabd _aa8k  _al3l"]')
                post.click()
                time.sleep(5)
                likes_button = self.driver.find_element(by='xpath', value='//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
                likes_button.click()
                time.sleep(5)
                temp = []
                likes_popup = self.driver.find_elements(by='xpath', value='//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]//a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 x1ykvv32 xougopr x159fomc xnp5s1o x194ut8o x1vzenxt xd7ygy7 xt298gk x1xrz1ek x1s928wv x1n449xj x2q1x1w x1j6awrg x162n7g1 x1m1drc7 x1ypdohk x4gyw5p _a6hd"]')
                for i in range(min(30, len(likes_popup))):
                        link = likes_popup[i].get_attribute("href")
                        temp.append(link)
                        if len(set(temp)) >= 30:
                                break
                for link in temp:
                        link=link.split("/")
                        
                        
                        time.sleep(15)     
                        try:
                                self.driver.get("https://www.instagram.com/direct/t")
                                time.sleep(15)
                                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Send message")]')
                                send_message_button.click()
                                time.sleep(5)
                                self.driver.find_element(by='xpath',value='//input[@placeholder="Search..."]').send_keys(link[3])
                                time.sleep(5)
                                self.driver.find_element(by='xpath',value='//div[@class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"]').click()
                                send_message_button = self.driver.find_element(by='xpath', value='//div[contains(text(), "Chat")]')
                                send_message_button.click()
                                time.sleep(5)
                                message_input= self.driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
                                message_input.send_keys("hello")
                                message_input.send_keys(Keys.ENTER)
                        except:
                                pass
                        





from sys import exit as sysExit         

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())


