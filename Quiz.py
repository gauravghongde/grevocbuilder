# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quiz.ui'
#
# Created: Wed Nov  1 17:04:00 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import random
import matplotlib.pyplot as plt
from QuizEnd import Ui_QuizResultWindow

conn = sqlite3.connect("gre.db")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QuizWindow(object):

    options = []
    counter = 0
    flag = ['NA']*10 #initializing flag with not attempted
    randWord = ""
    crctans = ""
    cur = conn.cursor()

######################################################################
    
    def disp(self):
    
        self.options[:] = []
        randno= random.randrange(1,231)
        
        self.cur.execute("select bwords from allwords where bid = "+str(randno)+";")
        self.randWord = self.cur.fetchone()[0]
        
        self.cur.execute("select bmeanings from allwords where bid = "+str(randno)+";")
        self.crctans = self.cur.fetchone()[0]
        #self.crctans = self.crctans.encode('utf-8')
        self.options.append(self.crctans)   #indicator1
        
        count = 1
        for i in range(10):
            if count!=4:
                randno= random.randrange(1,231)
                self.cur.execute("select bmeanings from allwords where bid = "+str(randno)+";")
                option = self.cur.fetchone()[0]
                if option not in self.options:
                    self.options.append(option)#skip the appending if mathes with other options.
                    count = count +1
            else:
                break
                
        random.shuffle(self.options)
        #print (self.options)
        #crrOp = options.index(crctans)
        self.cur.execute("select "+str(self.username)+" from allwords where bwords='"+str(self.randWord)+"'")
        self.status = self.cur.fetchone()[0]######ERROR
  
####################################################################

        self.labword.setText(_translate("QuizWindow", str(str(self.counter+1)+". "+self.randWord), None))
        self.rbutopA.setText(_translate("QuizWindow", self.options[0], None))
        self.rbutopB.setText(_translate("QuizWindow", self.options[1], None))
        self.rbutopC.setText(_translate("QuizWindow", self.options[2], None))
        self.rbutopD.setText(_translate("QuizWindow", self.options[3], None))
        self.counter = self.counter+1
        
        
    def setupUi(self, QuizWindow, MainMenuWindow,username):
        self.mw = MainMenuWindow
        self.form = QuizWindow
        self.username = username
        self.flag[:] = ['NA']*10 #reinitializing flag with NotAttemted
        self.s=0
        self.m=2
        
        QuizWindow.setObjectName(_fromUtf8("QuizWindow"))
        QuizWindow.resize(640, 480)
        QuizWindow.setGeometry(320, 100, 640, 480)
        QuizWindow.setMinimumSize(QtCore.QSize(640, 480))
        QuizWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        QuizWindow.setFont(font)
        QuizWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        
        self.labheader = QtGui.QLabel(QuizWindow)
        self.labheader.setGeometry(QtCore.QRect(20, 20, 601, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labheader.setFont(font)
        self.labheader.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);\n"
"color: rgb(255, 255, 255);"))
        self.labheader.setAlignment(QtCore.Qt.AlignCenter)
        self.labheader.setObjectName(_fromUtf8("labheader"))
        
        self.mainmenu_btn = QtGui.QPushButton(QuizWindow)
        self.mainmenu_btn.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.mainmenu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainmenu_btn.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.mainmenu_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenu_btn.setIcon(icon)
        self.mainmenu_btn.setIconSize(QtCore.QSize(25, 25))
        self.mainmenu_btn.setFlat(False)
        self.mainmenu_btn.setObjectName(_fromUtf8("mainmenu_btn"))
        
        self.labword = QtGui.QLabel(QuizWindow)
        self.labword.setGeometry(QtCore.QRect(10, 120, 621, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labword.setFont(font)
        self.labword.setLineWidth(0)
        self.labword.setAlignment(QtCore.Qt.AlignCenter)
        self.labword.setWordWrap(True)
        self.labword.setObjectName(_fromUtf8("labword"))
        self.bookmark_cb = QtGui.QCheckBox(QuizWindow)
        self.bookmark_cb.setGeometry(QtCore.QRect(380, 405, 99, 22))
        self.bookmark_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bookmark_cb.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.bookmark_cb.setObjectName(_fromUtf8("bookmark_cb"))
        self.bookmark_cb.hide()
        
        self.labnext = QtGui.QLabel(QuizWindow)
        self.labnext.setGeometry(QtCore.QRect(493, 401, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.labnext.setFont(font)
        self.labnext.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);\n"
"color: rgb(255, 255, 255);"))
        self.labnext.setText(_fromUtf8(""))
        self.labnext.setAlignment(QtCore.Qt.AlignCenter)
        self.labnext.setObjectName(_fromUtf8("labnext"))
        
        self.btn_next = QtGui.QPushButton(QuizWindow)
        self.btn_next.setGeometry(QtCore.QRect(493, 402, 99, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_next.setFont(font)
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        
        
        self.layoutWidget = QtGui.QWidget(QuizWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 208, 601, 128))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.D_indicator = QtGui.QLabel(self.layoutWidget)
        self.D_indicator.setMaximumSize(QtCore.QSize(20, 20))
        self.D_indicator.setText(_fromUtf8(""))
        self.D_indicator.setObjectName(_fromUtf8("D_indicator"))
        self.gridLayout.addWidget(self.D_indicator, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.A_indicator = QtGui.QLabel(self.layoutWidget)
        self.A_indicator.setMaximumSize(QtCore.QSize(20, 20))
        self.A_indicator.setText(_fromUtf8(""))
        self.A_indicator.setObjectName(_fromUtf8("A_indicator"))
        self.gridLayout.addWidget(self.A_indicator, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.B_indicator = QtGui.QLabel(self.layoutWidget)
        self.B_indicator.setMaximumSize(QtCore.QSize(20, 20))
        self.B_indicator.setText(_fromUtf8(""))
        self.B_indicator.setObjectName(_fromUtf8("B_indicator"))
        self.gridLayout.addWidget(self.B_indicator, 1, 1, 1, 1)
        self.rbutopB = QtGui.QRadioButton(self.layoutWidget)
        self.rbutopB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbutopB.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.rbutopB.setObjectName(_fromUtf8("rbutopB"))
        self.rbutopB.setAutoExclusive(False)
        self.gridLayout.addWidget(self.rbutopB, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.C_indicator = QtGui.QLabel(self.layoutWidget)
        self.C_indicator.setMaximumSize(QtCore.QSize(20, 20))
        self.C_indicator.setText(_fromUtf8(""))
        self.C_indicator.setObjectName(_fromUtf8("C_indicator"))
        self.gridLayout.addWidget(self.C_indicator, 2, 1, 1, 1)
        self.rbutopC = QtGui.QRadioButton(self.layoutWidget)
        self.rbutopC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbutopC.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.rbutopC.setObjectName(_fromUtf8("rbutopC"))
        self.rbutopC.setAutoExclusive(False)
        self.gridLayout.addWidget(self.rbutopC, 2, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.rbutopD = QtGui.QRadioButton(self.layoutWidget)
        self.rbutopD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbutopD.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.rbutopD.setObjectName(_fromUtf8("rbutopD"))
        self.rbutopD.setAutoExclusive(False)
        self.gridLayout.addWidget(self.rbutopD, 3, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 3, 1, 1)
        self.rbutopA = QtGui.QRadioButton(self.layoutWidget)
        self.rbutopA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbutopA.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.rbutopA.setCheckable(True)
        self.rbutopA.setChecked(False)
        self.rbutopA.setAutoExclusive(False)
        self.rbutopA.setObjectName(_fromUtf8("rbutopA"))
        self.gridLayout.addWidget(self.rbutopA, 0, 2, 1, 1)
        self.lblRemTime = QtGui.QLabel(QuizWindow)
        self.lblRemTime.setGeometry(QtCore.QRect(390, 90, 121, 17))
        self.lblRemTime.setObjectName(_fromUtf8("lblRemTime"))
        self.lcdNumber = QtGui.QLCDNumber(QuizWindow)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 82, 91, 31))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        
        
        self.btn_next.clicked.connect(self.nextbtnckd)
        self.mainmenu_btn.clicked.connect(self.btnMMClicked)
        self.rbutopA.clicked.connect(self.rdbtnAChecked)
        self.rbutopB.clicked.connect(self.rdbtnBChecked)
        self.rbutopC.clicked.connect(self.rdbtnCChecked)
        self.rbutopD.clicked.connect(self.rdbtnDChecked)
        
        self.disp()
        
        self.retranslateUi(QuizWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizWindow)
        
        time = "{0}:{1}".format(self.m,self.s)
       
        self.lcdNumber.setDigitCount(len(time))
        self.lcdNumber.display(time)
 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Time)
        self.Start()

        
    def rdbtnAChecked(self):
        self.rbutopA.setChecked(True)
        self.rbutopB.setChecked(False)
        self.rbutopC.setChecked(False)
        self.rbutopD.setChecked(False)
    def rdbtnBChecked(self):
        self.rbutopA.setChecked(False)
        self.rbutopB.setChecked(True)
        self.rbutopC.setChecked(False)
        self.rbutopD.setChecked(False)
    def rdbtnCChecked(self):
        self.rbutopA.setChecked(False)
        self.rbutopB.setChecked(False)
        self.rbutopC.setChecked(True)
        self.rbutopD.setChecked(False)
    def rdbtnDChecked(self):
        self.rbutopA.setChecked(False)
        self.rbutopB.setChecked(False)
        self.rbutopC.setChecked(False)
        self.rbutopD.setChecked(True)


    def nextbtnckd(self):

        if self.btn_next.text() == "SUBMIT":

            crrOp = self.options.index(self.crctans)
            if crrOp == 0:
                self.A_indicator.setPixmap(QtGui.QPixmap("crr.png"))
            elif crrOp == 1:
                self.B_indicator.setPixmap(QtGui.QPixmap("crr.png"))
            elif crrOp == 2:
                self.C_indicator.setPixmap(QtGui.QPixmap("crr.png"))
            elif crrOp == 3:
                self.D_indicator.setPixmap(QtGui.QPixmap("crr.png"))

            self.bookmark_cb.show()
            if self.status==1 or self.status==3:
                self.bookmark_cb.setChecked(True)
            else:
                self.bookmark_cb.setChecked(False)

            self.btn_next.setText(_translate("QuizWindow", "NEXT", None))

            if self.rbutopA.isChecked()==True:
                if self.crctans==self.options[0]:
                    self.flag.insert(self.counter-1,'Correct')
                else:
                    self.flag.insert(self.counter-1,'Wrong')
                    self.A_indicator.setPixmap(QtGui.QPixmap("wrng.png"))
            elif self.rbutopB.isChecked()==True:
                if self.crctans==self.options[1]:
                    self.flag.insert(self.counter-1,'Correct')
                else:
                    self.flag.insert(self.counter-1,'Wrong')
                    self.B_indicator.setPixmap(QtGui.QPixmap("wrng.png"))
            elif self.rbutopC.isChecked()==True:
                if self.crctans==self.options[2]:
                    self.flag.insert(self.counter-1,'Correct')
                else:
                    self.flag.insert(self.counter-1,'Wrong')
                    self.C_indicator.setPixmap(QtGui.QPixmap("wrng.png"))
            elif self.rbutopD.isChecked()==True:
                if self.crctans==self.options[3]:
                    self.flag.insert(self.counter-1,'Correct')
                else:
                    self.flag.insert(self.counter-1,'Wrong')
                    self.D_indicator.setPixmap(QtGui.QPixmap("wrng.png"))
            else:#if nothing is checked
                self.btn_next.setText(_translate("QuizWindow", "SUBMIT", None))
                self.A_indicator.setText(_translate("QuizWindow"," ",None))
                self.B_indicator.setText(_translate("QuizWindow"," ",None))
                self.C_indicator.setText(_translate("QuizWindow"," ",None))
                self.D_indicator.setText(_translate("QuizWindow"," ",None))
                self.bookmark_cb.hide()
                QtGui.QMessageBox.information(self.form, 'Message', "Select an option first!")

            

        elif self.btn_next.text() == "NEXT":
            self.rbutopA.setChecked(False)
            self.rbutopB.setChecked(False)
            self.rbutopC.setChecked(False)
            self.rbutopD.setChecked(False)
            
            if self.bookmark_cb.isChecked():
                if self.status==0 or self.status==2:
                    self.status = self.status+1
            else:
                if self.status==1 or self.status==3:
                    self.status = self.status-1
            
            conn.execute("update allwords set "+str(self.username)+"="+str(self.status)+" where bwords='"+str(self.randWord)+"'")
            conn.commit()
            self.bookmark_cb.hide()
            
        
            if self.counter<10:
                
                self.A_indicator.setText(_translate("QuizWindow"," ",None))
                self.B_indicator.setText(_translate("QuizWindow"," ",None))
                self.C_indicator.setText(_translate("QuizWindow"," ",None))
                self.D_indicator.setText(_translate("QuizWindow"," ",None))

                self.btn_next.setText(_translate("QuizWindow", "SUBMIT", None))
                self.disp() #in2

            else:
                self.form.hide()
                self.timer.stop()
                self.quizendwin=QtGui.QWidget()                             #CALLING QUIZ STAT WINDOW 
                self.qendui=Ui_QuizResultWindow()                           
                self.qendui.setupUi(self.quizendwin, self.flag, self.mw, self.username)    #flag = list
                self.quizendwin.show()


    def Start(self):
        self.timer.start(1000)

    def Time(self):

        if self.s > 0:
            self.s -=1
        else:
            if self.m > 0:
                self.m -= 1
                self.s = 59
            elif self.m == 0:
                self.timer.stop()
                self.form.hide()
                self.quizendwin=QtGui.QWidget()                             #CALLING QUIZ STAT WINDOW 
                self.qendui=Ui_QuizResultWindow()                           
                self.qendui.setupUi(self.quizendwin, self.flag, self.mw, self.username)    #flag = list
                self.quizendwin.show()

        time = "{0}:{1}".format(self.m,self.s)

        self.lcdNumber.setDigitCount(len(time))
        self.lcdNumber.display(time)


    def retranslateUi(self, QuizWindow):
        QuizWindow.setWindowTitle(_translate("QuizWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("QuizWindow", "GRE - Quiz", None))
        #self.labword.setText(_translate("QuizWindow", "WORD", None))
        self.bookmark_cb.setText(_translate("QuizWindow", "Bookmark", None))
        self.btn_next.setText(_translate("QuizWindow", "SUBMIT", None))
       
        self.lblRemTime.setText(_translate("QuizWindow", "Remaining Time:", None))
        
    def btnMMClicked(self):
        self.timer.stop()
        self.mw.show()
        self.form.hide()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QuizWindow = QtGui.QWidget()
    ui = Ui_QuizWindow()
    ui.setupUi(QuizWindow)
    QuizWindow.show()
    sys.exit(app.exec_())

