# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created: Sat Oct 14 11:55:32 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Quiz import Ui_QuizWindow
#from wordlist import Ui_Wordlist

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

class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):

        self.mw = MainMenuWindow;

        MainMenuWindow.setObjectName(_fromUtf8("MainMenuWindow"))
        MainMenuWindow.resize(640, 480)
        MainMenuWindow.setGeometry(320, 100, 640, 480)
        MainMenuWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainMenuWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        MainMenuWindow.setFont(font)
        MainMenuWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.labfcards = QtGui.QLabel(MainMenuWindow)
        self.labfcards.setGeometry(QtCore.QRect(253, 184, 141, 40))
        self.labfcards.setStyleSheet(_fromUtf8("background-color: rgb(227, 100, 59);"))
        self.labfcards.setText(_fromUtf8(""))
        self.labfcards.setObjectName(_fromUtf8("labfcards"))
        self.butfcards = QtGui.QPushButton(MainMenuWindow)
        self.butfcards.setGeometry(QtCore.QRect(260, 189, 131, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.butfcards.setFont(font)
        self.butfcards.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butfcards.setFocusPolicy(QtCore.Qt.NoFocus)
        self.butfcards.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("flashcadsicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butfcards.setIcon(icon)
        self.butfcards.setObjectName(_fromUtf8("butfcards"))
        self.header = QtGui.QLabel(MainMenuWindow)
        self.header.setGeometry(QtCore.QRect(10, 10, 621, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet(_fromUtf8("background-color: rgba(212, 36, 60, 200);\n"
"color: rgb(255, 255, 255);"))
        self.header.setScaledContents(True)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName(_fromUtf8("header"))
        self.labquiz = QtGui.QLabel(MainMenuWindow)
        self.labquiz.setGeometry(QtCore.QRect(253, 234, 141, 40))
        self.labquiz.setStyleSheet(_fromUtf8("background-color: rgb(227, 100, 59);"))
        self.labquiz.setText(_fromUtf8(""))
        self.labquiz.setObjectName(_fromUtf8("labquiz"))
        self.butquiz = QtGui.QPushButton(MainMenuWindow)
        self.butquiz.setGeometry(QtCore.QRect(270, 240, 111, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.butquiz.setFont(font)
        self.butquiz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butquiz.setFocusPolicy(QtCore.Qt.NoFocus)
        self.butquiz.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("quizicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butquiz.setIcon(icon1)
        self.butquiz.setObjectName(_fromUtf8("butquiz"))
        self.labwlist = QtGui.QLabel(MainMenuWindow)
        self.labwlist.setGeometry(QtCore.QRect(253, 284, 141, 40))
        self.labwlist.setStyleSheet(_fromUtf8("background-color: rgb(227, 100, 59);"))
        self.labwlist.setText(_fromUtf8(""))
        self.labwlist.setObjectName(_fromUtf8("labwlist"))
        self.butwordlst = QtGui.QPushButton(MainMenuWindow)
        self.butwordlst.setGeometry(QtCore.QRect(257, 289, 130, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.butwordlst.setFont(font)
        self.butwordlst.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butwordlst.setFocusPolicy(QtCore.Qt.NoFocus)
        self.butwordlst.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("listicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butwordlst.setIcon(icon2)
        self.butwordlst.setObjectName(_fromUtf8("butwordlst"))
        self.labfav = QtGui.QLabel(MainMenuWindow)
        self.labfav.setGeometry(QtCore.QRect(253, 335, 141, 40))
        self.labfav.setStyleSheet(_fromUtf8("background-color: rgb(227, 100, 59);"))
        self.labfav.setText(_fromUtf8(""))
        self.labfav.setObjectName(_fromUtf8("labfav"))
        self.butfav = QtGui.QPushButton(MainMenuWindow)
        self.butfav.setGeometry(QtCore.QRect(257, 340, 131, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.butfav.setFont(font)
        self.butfav.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butfav.setFocusPolicy(QtCore.Qt.NoFocus)
        self.butfav.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("favoriteicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butfav.setIcon(icon3)
        self.butfav.setIconSize(QtCore.QSize(20, 20))
        self.butfav.setObjectName(_fromUtf8("butfav"))
        self.labstats = QtGui.QLabel(MainMenuWindow)
        self.labstats.setGeometry(QtCore.QRect(254, 385, 141, 40))
        self.labstats.setStyleSheet(_fromUtf8("background-color: rgb(227, 100, 59);"))
        self.labstats.setText(_fromUtf8(""))
        self.labstats.setObjectName(_fromUtf8("labstats"))
        self.butstats = QtGui.QPushButton(MainMenuWindow)
        self.butstats.setGeometry(QtCore.QRect(258, 390, 131, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.butstats.setFont(font)
        self.butstats.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butstats.setFocusPolicy(QtCore.Qt.NoFocus)
        self.butstats.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("statsicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butstats.setIcon(icon4)
        self.butstats.setObjectName(_fromUtf8("butstats"))
        

        self.butwordlst.clicked.connect(self.btnWordlistClicked)
        self.butquiz.clicked.connect(self.btnquizClicked)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def btnquizClicked(self):
        self.mw.hide()
        self.quizwin = QtGui.QWidget()
        self.quizui = Ui_QuizWindow()
        self.quizui.setupUi(self.quizwin,self.mw)
        self.quizwin.show() 

    def btnWordlistClicked(self):
        self.mw.hide()
        self.quizwin = QtGui.QWidget()
        self.quizui = Ui_Wordlist()
        self.quizui.setupUi(self.quizwin,self.mw)
        self.quizwin.show() 


    def retranslateUi(self, MainMenuWindow):
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "GRE Vocab Builder", None))
        self.butfcards.setText(_translate("MainMenuWindow", "    FlashCards", None))
        self.header.setText(_translate("MainMenuWindow", "GRE VOCABULARY BUILDER ", None))
        self.butquiz.setText(_translate("MainMenuWindow", "   Take a Quiz", None))
        self.butwordlst.setText(_translate("MainMenuWindow", "    WordList", None))
        self.butfav.setText(_translate("MainMenuWindow", "    Favorites", None))
        self.butstats.setText(_translate("MainMenuWindow", "    Statistics", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainMenuWindow = QtGui.QWidget()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec_())

