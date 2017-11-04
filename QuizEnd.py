# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuizEnd.ui'
#
# Created: Thu Nov  2 15:27:09 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

class Ui_QuizResultWindow(QtGui.QWidget):
    cur = conn.cursor()
    countCrct=0
    countWrng=0
    countNa=0
    badge="NA"

    def __init__(self,parent = None):
        super(Ui_QuizResultWindow,self).__init__()
        self.figure = plt.figure(figsize =(50,20))
        self.canvas = FigureCanvas(self.figure) #create canvas that will hold our plot
        #self.toolbar = NavigationToolbar(self.canvas,self)
        
    def setupUi(self, QuizResultWindow,flag,MainWindow,username):
        self.mw=MainWindow
        self.QuizResultWindow=QuizResultWindow
        self.flag = flag
        self.username = username
        
        QuizResultWindow.setObjectName(_fromUtf8("QuizResultWindow"))
        QuizResultWindow.resize(640, 480)
        QuizResultWindow.setGeometry(320, 100, 640, 480)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        QuizResultWindow.setFont(font)
        QuizResultWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))

        self.labheader = QtGui.QLabel(QuizResultWindow)
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
    
        self.mainmenu_btn = QtGui.QPushButton(QuizResultWindow)
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
        
        self.gridLayoutWidget = QtGui.QWidget(QuizResultWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 180, 621, 291))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.glayout_pie = QtGui.QGridLayout(self.gridLayoutWidget)
        self.glayout_pie.setMargin(0)
        self.glayout_pie.setObjectName(_fromUtf8("glayout_pie"))
        self.layoutWidget = QtGui.QWidget(QuizResultWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(229, 130, 181, 33))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labstatic = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labstatic.setFont(font)
        self.labstatic.setObjectName(_fromUtf8("labstatic"))
        self.gridLayout.addWidget(self.labstatic, 0, 0, 1, 1)
        self.lab_score = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lab_score.setFont(font)
        self.lab_score.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_score.setObjectName(_fromUtf8("lab_score"))
        self.gridLayout.addWidget(self.lab_score, 0, 1, 1, 1)
        self.labstatic2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labstatic2.setFont(font)
        self.labstatic2.setObjectName(_fromUtf8("labstatic2"))
        self.labbadge = QtGui.QLabel(QuizResultWindow)
        self.labbadge.setGeometry(QtCore.QRect(425, 119, 41, 41))
        self.labbadge.setText(_fromUtf8(""))
        #self.labbadge.setPixmap(QtGui.QPixmap(_fromUtf8("silver.png")))
        self.labbadge.setScaledContents(True)
        self.labbadge.setObjectName(_fromUtf8("labbadge"))
        self.gridLayout.addWidget(self.labstatic2, 0, 2, 1, 1)
        
        self.glayout_pie.addWidget(self.canvas,1,0,1,2)
        self.mainmenu_btn.clicked.connect(self.btnMMClicked)
        
        plt.cla()
        ax = self.figure.add_subplot(111)
        plt.rcParams['axes.facecolor'] = 'white'
        
        for i in range(10):
            if self.flag[i] == "Correct":
                self.countCrct=self.countCrct+1
            elif self.flag[i] == "Wrong":
                self.countWrng = self.countWrng+1
            else:
                self.countNa = self.countNa+1

        self.cur.execute("select score from users where username='"+str(self.username)+"'")
        self.currscore = self.cur.fetchone()[0]

        if self.countCrct in [10, 9]:
            self.badge = "G"
            self.currscore = self.currscore+100
            self.labbadge.setPixmap(QtGui.QPixmap(_fromUtf8("gold.png")))
        elif self.countCrct in [8, 7]:
            self.badge = "S"
            self.currscore = self.currscore+10
            self.labbadge.setPixmap(QtGui.QPixmap(_fromUtf8("silver.png")))
        elif self.countCrct in [6, 5]:
            self.badge = "B"
            self.currscore = self.currscore+1
            self.labbadge.setPixmap(QtGui.QPixmap(_fromUtf8("bronze.png")))
        else:
            self.badge = "NA"

        conn.execute("update users set score="+str(self.currscore)+" where username='"+str(self.username)+"'")

        today = date.today()
        print self.countCrct
        print self.countWrng
        print self.countNa
        stmt = "insert into "+str(self.username)+" (Timestamp, CorrectAnsCount, Badges) values(?, ?, ?);"
        conn.execute(stmt,(today, self.countCrct, self.badge))
        conn.commit()

        labels = 'Correct','Incorrect','NotAttemted'
        sizes = [self.countCrct, self.countWrng, self.countNa]
        #explode = (0.03,0)
        colors = ['yellowgreen','lightcoral', 'lightskyblue']
        
        #ax.pie(sizes,colors = colors ,labels = labels, autopct = '%1.1f%%',shadow = True,startangle = 90)
        pie = ax.pie(sizes, colors = colors, shadow=True, autopct='%1.1f%%',startangle = 90)
        ax.legend(pie[0], labels, loc="lower right")
        ax.axis('equal')
        
        self.lab_score.setText(str(self.countCrct))

        self.retranslateUi(QuizResultWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizResultWindow)

    def retranslateUi(self, QuizResultWindow):
        QuizResultWindow.setWindowTitle(_translate("QuizResultWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("QuizResultWindow", "Your Score", None))
        self.labstatic.setText(_translate("QuizResultWindow", "SCORE : ", None))
        #self.lab_score.setText(_translate("QuizResultWindow", "0", None))
        self.labstatic2.setText(_translate("QuizResultWindow", "/ 10", None))

    def btnMMClicked(self):
        self.mw.show()
        self.QuizResultWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QuizResultWindow = QtGui.QWidget()
    ui = Ui_QuizResultWindow()
    ui.setupUi(QuizResultWindow)
    QuizResultWindow.show()
    sys.exit(app.exec_())

