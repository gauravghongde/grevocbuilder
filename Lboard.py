# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lboard.ui'
#
# Created: Sat Nov  4 11:16:37 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

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

class Ui_LboardWindow(QtGui.QWidget):

    user_names = []
    learned_count= []
    #Quiztaken= []
    #avg_quiz_score= []
    cur = conn.cursor()
    uname=[]
    name=""
    total=0
    
    def __init__(self,parent = None):
        super(Ui_LboardWindow,self).__init__()
        self.figure = plt.figure(figsize =(50,20),facecolor="white")#
        self.canvas = FigureCanvas(self.figure) #create canvas that will hold our plot
        #self.toolbar = NavigationToolbar(self.canvas,self)

    def setupUi(self, LboardWindow, StatusWindow, username):

        self.lw = LboardWindow
        self.username = username
        self.sw = StatusWindow
        self.cur.execute("select count(*) from users")
        self.rcount = self.cur.fetchone()[0]

        LboardWindow.setObjectName(_fromUtf8("LboardWindow"))
        LboardWindow.resize(640, 480)
        LboardWindow.setGeometry(320, 100, 640, 480)
        LboardWindow.setMinimumSize(QtCore.QSize(640, 480))
        LboardWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        LboardWindow.setFont(font)
        LboardWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.gridLayoutWidget = QtGui.QWidget(LboardWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(17, 141, 601, 311))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labheader = QtGui.QLabel(LboardWindow)
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
        self.tableWidget = QtGui.QTableWidget(LboardWindow)
        self.tableWidget.setGeometry(QtCore.QRect(104, 207, 430, 210))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        #self.tableWidget.setMinimumSize(QtCore.QSize(600, 310))
        #self.tableWidget.setMaximumSize(QtCore.QSize(600, 310))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)

        self.tableWidget.setRowCount(self.rcount)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)

        self.btn_showgraph = QtGui.QPushButton(LboardWindow)
        self.btn_showgraph.setGeometry(QtCore.QRect(530, 130, 41, 41))
        self.btn_showgraph.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);"))
        self.btn_showgraph.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("fwd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_showgraph.setIcon(icon)
        self.btn_showgraph.setObjectName(_fromUtf8("btn_showgraph"))
        self.btn_showtable = QtGui.QPushButton(LboardWindow)
        self.btn_showtable.setGeometry(QtCore.QRect(470, 130, 41, 41))
        self.btn_showtable.setStyleSheet(_fromUtf8("background-color: rgb(206, 36, 57);"))
        self.btn_showtable.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("rewnd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_showtable.setIcon(icon1)
        self.btn_showtable.setObjectName(_fromUtf8("btn_showtable"))

        #self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setHorizontalHeaderLabels(('Rank', 'Name', 'Score'))
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.lab_headoftable = QtGui.QLabel(LboardWindow)
        self.lab_headoftable.setGeometry(QtCore.QRect(40, 140, 200, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.lab_headoftable.setFont(font)
        self.lab_headoftable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_headoftable.setObjectName(_fromUtf8("lab_headoftable"))
        self.bck_btn = QtGui.QPushButton(LboardWindow)
        self.bck_btn.setGeometry(QtCore.QRect(18, 22, 51, 51))
        self.bck_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bck_btn.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.bck_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bck_btn.setIcon(icon)
        self.bck_btn.setIconSize(QtCore.QSize(25, 25))
        self.bck_btn.setFlat(False)
        self.bck_btn.setObjectName(_fromUtf8("bck_btn"))
        
        self.btn_showgraph.clicked.connect(self.btnShowGraphClicked)
        self.btn_showtable.clicked.connect(self.btnShowTableClicked)
        self.bck_btn.clicked.connect(self.btnBKClicked)

        self.btn_showgraph.show()
        self.btn_showtable.hide()
        
        for i in range(self.rcount):
            self.newitem3 = QtGui.QTableWidgetItem(str(i+1))
            self.newitem3.setTextAlignment(0x0004 | 0x0080)
            self.tableWidget.setItem(i,0,self.newitem3)
        
        self.bck_btn.clicked.connect(self.btnBKClicked)
        
        fetch = self.cur.execute("select username, score from users order by score desc")
        fetch = list(fetch)

        for i in range(self.rcount):
            self.newitem1 = QtGui.QTableWidgetItem(fetch[i][0])
            self.newitem2 = QtGui.QTableWidgetItem(str(fetch[i][1]))
            self.newitem1.setTextAlignment(0x0004 | 0x0080)
            self.newitem2.setTextAlignment(0x0004 | 0x0080)
            self.tableWidget.setItem(i,1,self.newitem1)
            self.tableWidget.setItem(i,2,self.newitem2)
        
        self.retranslateUi(LboardWindow)
        QtCore.QMetaObject.connectSlotsByName(LboardWindow)

    def retranslateUi(self, LboardWindow):
        LboardWindow.setWindowTitle(_translate("LboardWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("LboardWindow", "LeaderBoard", None))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lab_headoftable.setText(_translate("LboardWindow", "Current LeaderBoard ", None))
        
    def btnShowTableClicked(self):
        self.lab_headoftable.setText("Current LeaderBoard ")
        self.btn_showgraph.show()
        self.btn_showtable.hide()
        self.canvas.hide()
        self.tableWidget.show()
        
    def btnShowGraphClicked(self):
        self.figure = plt.figure(figsize =(50,20),facecolor="white")#
        self.canvas = FigureCanvas(self.figure) #create canvas that will hold our plot
        self.learned_count[:] = []
        self.uname[:] = []
        self.tableWidget.hide()
        self.btn_showgraph.hide()
        self.btn_showtable.show()
        self.gridLayout.addWidget(self.canvas,1,0,1,2)
        self.cur.execute("select count(username) from users")
        self.total = self.cur.fetchone()[0]
        
        self.cur1 = conn.execute("select username from users")
        for row in self.cur1:
            name = row[0]
            name = name.encode('utf-8')
            self.uname.append(name)
        
        
        for user in self.uname:
        
            self.cur.execute("select count("+user+") from allwords where "+user+"=2 or "+user+"=3")
            self.lCount = self.cur.fetchone()[0]
            self.learned_count.append(self.lCount)
        
        width = 0.2
        ind1 = np.arange(len(self.uname)) 
        plt.cla()
        ax = self.figure.add_subplot(111)
        
        rects1 = ax.bar(ind1+width,self.learned_count,width,color='blue',error_kw=dict(elinewidth=2,ecolor='red'))
        ax.set_xticks(ind1+0.0+width)
        ax.set_xticklabels(self.uname,rotation= 'vertical')
        ax.set_ylabel("Learned Words")
        ax.set_xlabel(" ")
        self.lab_headoftable.setText("Learned Words Comparision")
        plt.tight_layout(rect=[0.15, 0.20, 0.90, 0.85])
        #ax.set_title("Learning Stats for all users",fontsize = 20)
        #ax.legend((rects1[0],rects2[0]),('Learned','avg_score'))



    def btnBKClicked(self):
        self.lw.hide()
        self.sw.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LboardWindow = QtGui.QWidget()
    ui = Ui_LboardWindow()
    ui.setupUi(LboardWindow)
    LboardWindow.show()
    sys.exit(app.exec_())

