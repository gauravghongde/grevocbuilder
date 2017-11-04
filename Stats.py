# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stats.ui'
#
# Created: Fri Nov  3 17:16:47 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Lboard import Ui_LboardWindow
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

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

class Ui_StatsWindow(QtGui.QWidget):
    cur = conn.cursor()

    def __init__(self,parent = None):
        super(Ui_StatsWindow,self).__init__()
        self.figure = plt.figure(figsize =(50,20),facecolor="white")#
        self.canvas = FigureCanvas(self.figure) #create canvas that will hold our plot
        self.toolbar = NavigationToolbar(self.canvas,self)

    def setupUi(self, StatsWindow, MainWindow, username):

        self.mw = MainWindow
        self.username = username
        self.sw = StatsWindow

        StatsWindow.setObjectName(_fromUtf8("StatsWindow"))
        StatsWindow.resize(640, 480)
        StatsWindow.setGeometry(320, 100, 640, 480)
        StatsWindow.setMinimumSize(QtCore.QSize(640, 480))
        StatsWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        StatsWindow.setFont(font)
        StatsWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.labheader = QtGui.QLabel(StatsWindow)
        self.labheader.setGeometry(QtCore.QRect(18, 22, 601, 51))
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
        self.mainmenu_btn = QtGui.QPushButton(StatsWindow)
        self.mainmenu_btn.setGeometry(QtCore.QRect(18, 22, 51, 51))
        self.mainmenu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainmenu_btn.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.mainmenu_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenu_btn.setIcon(icon)
        self.mainmenu_btn.setIconSize(QtCore.QSize(25, 25))
        self.mainmenu_btn.setFlat(False)
        self.mainmenu_btn.setObjectName(_fromUtf8("mainmenu_btn"))
        self.gridLayoutWidget_2 = QtGui.QWidget(StatsWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(210, 175, 401, 280))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridlayout_progress = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridlayout_progress.setMargin(0)
        self.gridlayout_progress.setObjectName(_fromUtf8("gridlayout_progress"))
        self.btn_lboard = QtGui.QPushButton(StatsWindow)
        self.btn_lboard.setGeometry(QtCore.QRect(485, 92, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_lboard.setFont(font)
        self.btn_lboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_lboard.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(206, 36, 57)"))
        self.btn_lboard.setFlat(False)
        self.btn_lboard.setObjectName(_fromUtf8("btn_lboard"))
        self.lab_prog = QtGui.QLabel(StatsWindow)
        self.lab_prog.setGeometry(QtCore.QRect(210, 140, 401, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_prog.setFont(font)
        self.lab_prog.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_prog.setObjectName(_fromUtf8("lab_prog"))
        self.profile_lab = QtGui.QLabel(StatsWindow)
        self.profile_lab.setGeometry(QtCore.QRect(49, 136, 81, 81))
        self.profile_lab.setText(_fromUtf8(""))
        self.profile_lab.setPixmap(QtGui.QPixmap(_fromUtf8("userblu.png")))
        self.profile_lab.setScaledContents(True)
        self.profile_lab.setObjectName(_fromUtf8("profile_lab"))
        self.line = QtGui.QLabel(StatsWindow)
        self.line.setGeometry(QtCore.QRect(170, 91, 5, 361))
        self.line.setStyleSheet(_fromUtf8("background-color: rgba(206, 36, 57, 100);"))
        self.line.setText(_fromUtf8(""))
        self.line.setObjectName(_fromUtf8("line"))
        self.lab_username = QtGui.QLabel(StatsWindow)
        self.lab_username.setGeometry(QtCore.QRect(34, 236, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_username.setFont(font)
        self.lab_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lab_username.setObjectName(_fromUtf8("lab_username"))
        self.lab_gcount = QtGui.QLabel(StatsWindow)
        self.lab_gcount.setGeometry(QtCore.QRect(40, 318, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_gcount.setFont(font)
        self.lab_gcount.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_gcount.setObjectName(_fromUtf8("lab_gcount"))
        self.lab_img_g = QtGui.QLabel(StatsWindow)
        self.lab_img_g.setGeometry(QtCore.QRect(32, 283, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_img_g.setFont(font)
        self.lab_img_g.setText(_fromUtf8(""))
        self.lab_img_g.setPixmap(QtGui.QPixmap(_fromUtf8("gold.png")))
        self.lab_img_g.setScaledContents(True)
        self.lab_img_g.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_img_g.setObjectName(_fromUtf8("lab_img_g"))
        self.lab_img_s = QtGui.QLabel(StatsWindow)
        self.lab_img_s.setGeometry(QtCore.QRect(72, 283, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_img_s.setFont(font)
        self.lab_img_s.setText(_fromUtf8(""))
        self.lab_img_s.setPixmap(QtGui.QPixmap(_fromUtf8("silver.png")))
        self.lab_img_s.setScaledContents(True)
        self.lab_img_s.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_img_s.setObjectName(_fromUtf8("lab_img_s"))
        self.lab_scount = QtGui.QLabel(StatsWindow)
        self.lab_scount.setGeometry(QtCore.QRect(80, 318, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_scount.setFont(font)
        self.lab_scount.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_scount.setObjectName(_fromUtf8("lab_scount"))
        self.lab_img_b = QtGui.QLabel(StatsWindow)
        self.lab_img_b.setGeometry(QtCore.QRect(112, 283, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_img_b.setFont(font)
        self.lab_img_b.setText(_fromUtf8(""))
        self.lab_img_b.setPixmap(QtGui.QPixmap(_fromUtf8("bronze.png")))
        self.lab_img_b.setScaledContents(True)
        self.lab_img_b.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_img_b.setObjectName(_fromUtf8("lab_img_b"))
        self.lab_bcount = QtGui.QLabel(StatsWindow)
        self.lab_bcount.setGeometry(QtCore.QRect(120, 318, 16, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_bcount.setFont(font)
        self.lab_bcount.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_bcount.setObjectName(_fromUtf8("lab_bcount"))

        ###########################################################

        self.mainmenu_btn.clicked.connect(self.btnMMClicked)
        self.btn_lboard.clicked.connect(self.btnLBClicked)

        self.lab_username.setText("@"+str(self.username))
        self.cur.execute("select count(Badges) from "+str(self.username)+" where Badges='G'")
        self.gcount = self.cur.fetchone()[0]
        self.lab_gcount.setText(str(self.gcount))
        self.cur.execute("select count(Badges) from "+str(self.username)+" where Badges='S'")
        self.scount = self.cur.fetchone()[0]
        self.lab_scount.setText(str(self.scount))
        self.cur.execute("select count(Badges) from "+str(self.username)+" where Badges='B'")
        self.bcount = self.cur.fetchone()[0]
        self.lab_bcount.setText(str(self.bcount))

        self.gridlayout_progress.addWidget(self.canvas,1,0,1,2)
        #self.gridlayout_progress.addWidget(self.toolbar,0,0,1,2)

        self.cur.execute("select CorrectAnsCount from "+str(self.username))
        quiz_scores = [int(record[0]) for record in self.cur.fetchall()]

        #quiz_scores=[5,7,8,5,9,6,3,5,5,7,4,8,6,8,3,8,9,9,7,5,3,5,6,7,2,6,8,9,6]
        attempt_no= range(1,len(quiz_scores)+1)

        plt.cla()

        ax = self.figure.add_subplot(111)
        ax.set_xlabel('Attempt_No',fontname='Ubuntu Condensed',fontsize=16, fontweight='bold')
        ax.set_ylabel('Score',fontsize=16, fontname='Ubuntu Condensed', fontweight='bold')

        ax.plot(attempt_no,quiz_scores,'ro',label='Progress',color='blue',linewidth=2,linestyle='-')
        
        axes=plt.gca()
        axes.set_xlim([0,(len(quiz_scores)+1)])
        axes.set_ylim([0,10])
        plt.tight_layout(rect=[0.10, 0.12, 0.98, 0.97])
        ax.set_title('Quiz Stats', fontname='Ubuntu Condensed',fontsize=1, fontweight='bold')

        #############################################################

        self.retranslateUi(StatsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatsWindow)

    def btnLBClicked(self):
        self.sw.hide()
        self.lbwin = QtGui.QWidget()
        self.lbui = Ui_LboardWindow()
        self.lbui.setupUi(self.lbwin,self.sw,self.username)
        self.lbwin.show()

    def retranslateUi(self, StatsWindow):
        StatsWindow.setWindowTitle(_translate("StatsWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("StatsWindow", "QUIZ STATS", None))
        self.btn_lboard.setText(_translate("StatsWindow", "LeaderBoard ->", None))
        self.lab_prog.setText(_translate("StatsWindow", "My Progress ", None))
        #self.lab_username.setText(_translate("StatsWindow", "Username", None))
        #self.lab_gcount.setText(_translate("StatsWindow", "3", None))
        #self.lab_scount.setText(_translate("StatsWindow", "2", None))
        #self.lab_bcount.setText(_translate("StatsWindow", "0", None))

    def btnMMClicked(self):
        self.mw.show()
        self.sw.hide()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    StatsWindow = QtGui.QWidget()
    ui = Ui_StatsWindow()
    ui.setupUi(StatsWindow)
    StatsWindow.show()
    sys.exit(app.exec_())

