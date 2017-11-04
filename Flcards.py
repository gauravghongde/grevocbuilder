# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flcards.ui'
#
# Created: Wed Nov  1 17:57:23 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import random

conn = sqlite3.connect("gre.db")#

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

class Ui_Flashcard(object):
    randWord = ""#
    meaning = "" #
    cur = conn.cursor()
    flag=0
    
    def disp(self):# 
         
        self.bookmark_cb.hide()
        self.labnext.hide()
        self.labmeaning.hide()
        self.rb_know.hide()
        self.rb_notknow.hide()
        self.btn_prev.hide()
        self.btn_next.hide()
        self.labshowbtn.show()
        self.btn_show.show()
        self.bookmark_cb.setChecked(False)
        self.rb_know.setChecked(False)
        self.rb_notknow.setChecked(False)
        

        self.flag=0

        self.cur.execute("select bwords from allwords where "+str(self.username)+" =0 or "+str(self.username)+" =1 ORDER BY RANDOM() LIMIT 1")

        #cur.execute("select bwords from allwords where "+self.username+" =0 or "+self.username+" =1")
        self.randWord = self.cur.fetchone()[0]

	self.cur.execute("select "+str(self.username)+" from allwords where bwords='"+self.randWord+"'")
	self.bookmarked =  self.cur.fetchone()[0]
	if self.bookmarked == 1:
		self.bookmark_cb.setChecked(True)
	
        self.labword.setText(_translate("FlWindow", str(self.randWord), None))
        
        
    def setupUi(self, FlWindow, MainMenuWindow, username):
        self.mw = MainMenuWindow
        self.fw = FlWindow
        self.username = username
        
        FlWindow.setObjectName(_fromUtf8("FlWindow"))
        FlWindow.resize(640, 480)
        FlWindow.setGeometry(320, 100, 640, 480)
        FlWindow.setMinimumSize(QtCore.QSize(640, 480))
        FlWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        FlWindow.setFont(font)
        FlWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))

        self.labheader = QtGui.QLabel(FlWindow)
        self.labheader.setGeometry(QtCore.QRect(20, 22, 601, 51))
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
    
        self.mainmenu_btn = QtGui.QPushButton(FlWindow)
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
       
        self.labword = QtGui.QLabel(FlWindow)
        self.labword.setGeometry(QtCore.QRect(9, 130, 621, 41))
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
        
        self.bookmark_cb = QtGui.QCheckBox(FlWindow)
        self.bookmark_cb.setGeometry(QtCore.QRect(271, 359, 99, 22))
        self.bookmark_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bookmark_cb.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.bookmark_cb.setObjectName(_fromUtf8("bookmark_cb"))
       
        self.labnext = QtGui.QLabel(FlWindow)
        self.labnext.setGeometry(QtCore.QRect(503, 411, 101, 31))
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
        
        self.btn_next = QtGui.QPushButton(FlWindow)
        self.btn_next.setGeometry(QtCore.QRect(503, 412, 99, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_next.setFont(font)
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        
        self.layoutWidget = QtGui.QWidget(FlWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 205, 601, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        
        self.labmeaning = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.labmeaning.setFont(font)
        self.labmeaning.setObjectName(_fromUtf8("labmeaning"))
        self.gridLayout.addWidget(self.labmeaning, 0, 1, 1, 1)
        
        self.labshowbtn = QtGui.QLabel(FlWindow)
        #self.labshowbtn.hide()
        self.labshowbtn.setGeometry(QtCore.QRect(250, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labshowbtn.setFont(font)
        self.labshowbtn.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);\n"
"color: rgb(255, 255, 255);"))
        self.labshowbtn.setText(_fromUtf8(""))
        self.labshowbtn.setAlignment(QtCore.Qt.AlignCenter)
        self.labshowbtn.setObjectName(_fromUtf8("labshowbtn"))
        
        self.rb_know = QtGui.QRadioButton(FlWindow)
        self.rb_know.setGeometry(QtCore.QRect(240, 280, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.rb_know.setFont(font)
        self.rb_know.setObjectName(_fromUtf8("rb_know"))
        self.rb_know.setAutoExclusive(False)
        self.rb_notknow = QtGui.QRadioButton(FlWindow)
        self.rb_notknow.setGeometry(QtCore.QRect(240, 310, 191, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.rb_notknow.setFont(font)
        self.rb_notknow.setObjectName(_fromUtf8("rb_notknow"))
        self.rb_notknow.setAutoExclusive(False)
        
        self.labprev = QtGui.QLabel(FlWindow)
        self.labprev.setGeometry(QtCore.QRect(387, 411, 101, 31))
        self.labprev.hide()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labprev.setFont(font)
        self.labprev.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);\n"
"color: rgb(255, 255, 255);"))
        self.labprev.setText(_fromUtf8(""))
        self.labprev.setAlignment(QtCore.Qt.AlignCenter)
        self.labprev.setObjectName(_fromUtf8("labprev"))
        
        self.btn_prev = QtGui.QPushButton(FlWindow)
        self.btn_prev.setGeometry(QtCore.QRect(387, 412, 99, 31))
        self.btn_prev.hide()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_prev.setFont(font)
        self.btn_prev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_prev.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_prev.setObjectName(_fromUtf8("btn_prev"))
            
        self.btn_show = QtGui.QPushButton(FlWindow)
        self.btn_show.setGeometry(QtCore.QRect(250, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_show.setFont(font)
        self.btn_show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_show.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        
        self.btn_show.clicked.connect(self.btnShowClicked)
        self.btn_next.clicked.connect(self.btnNextClicked)
        self.mainmenu_btn.clicked.connect(self.btnMMClicked)
        self.rb_know.clicked.connect(self.rdbtnKnowClicked)
        self.rb_notknow.clicked.connect(self.rdbtnNotknowClicked)
       
        self.retranslateUi(FlWindow)
        QtCore.QMetaObject.connectSlotsByName(FlWindow)
        
      
        self.disp()#decide how many words to fetch for flashcards and iterate that many times

        
    def rdbtnKnowClicked(self):
    	self.rb_know.setChecked(True)
    	self.rb_notknow.setChecked(False)
    	
    def rdbtnNotknowClicked(self):
    	self.rb_know.setChecked(False)
    	self.rb_notknow.setChecked(True)
    	    
    def btnShowClicked(self):
        self.btn_show.hide()
        self.labshowbtn.hide()
        self.rb_notknow.show()
        self.rb_notknow.setText(_translate("FlWindow", "I didn\'t know this word", None))
        self.rb_know.show()
        self.rb_know.setText(_translate("FlWindow", "I knew this word", None))
        self.btn_next.show()
        self.labnext.show()
        self.labnext.setText("NEXT")
        self.labmeaning.show()
        self.bookmark_cb.show()
        
        #query for fetching meaning
        self.cur.execute("select bmeanings from allwords where bwords='"+str(self.randWord)+"';")
        self.meaning = self.cur.fetchone()[0]
        self.labmeaning.setText(str(self.meaning))
        
    def btnNextClicked(self):
        if self.rb_know.isChecked()==True and  self.bookmark_cb.isChecked()==True:
            sql_stmt = "update allwords set "+str(self.username)+" =3 where bwords='"+str(self.randWord)+"';"
            self.flag=1
        elif self.rb_notknow.isChecked()==True and self.bookmark_cb.isChecked()==True:
            sql_stmt = "update allwords set "+str(self.username)+" =1 where bwords='"+str(self.randWord)+"';"
            self.flag=1
        elif self.rb_know.isChecked()==True and  self.bookmark_cb.isChecked()==False:
            sql_stmt = "update allwords set "+str(self.username)+" =2 where bwords='"+str(self.randWord)+"';"
            self.flag=1
        elif self.rb_notknow.isChecked()==True and  self.bookmark_cb.isChecked()==False:
            sql_stmt = "update allwords set "+str(self.username)+" =0 where bwords='"+str(self.randWord)+"';"
            self.flag=1
        else:
            QtGui.QMessageBox.information(self.fw, 'Message', "Please select one of the options!")
            
        if self.flag==1:
            conn.execute(sql_stmt)
            conn.commit()
            self.disp()
            

        

    def btnMMClicked(self):
        self.fw.hide()
        self.mw.show()
            
    def retranslateUi(self, FlWindow):
        FlWindow.setWindowTitle(_translate("FlWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("FlWindow", "FLASHCARDS", None))
        self.bookmark_cb.setText(_translate("FlWindow", "Bookmark", None))
        self.btn_prev.setText(_translate("FlWindow", "BACK", None))
        self.btn_show.setText(_translate("FlWindow", "SHOW MEANING", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FlWindow = QtGui.QWidget()
    ui = Ui_Flashcard()
    ui.setupUi(FlWindow)
    FlWindow.show()
    sys.exit(app.exec_())

