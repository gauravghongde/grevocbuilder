# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Favorites.ui'
#
# Created: Thu Nov  2 16:52:41 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_FavWindow(object):
    cur = conn.cursor()

    def setupUi(self, FavWindow, MainMenuWindow, username):

        self.mw = MainMenuWindow
        self.fw = FavWindow
        self.username = username
        FavWindow.setGeometry(320, 100, 640, 480)
        self.cur.execute("select count(*) from allwords where "+str(self.username)+"=3 or "+str(self.username)+"=1")
        self.rcount = self.cur.fetchone()[0]
        #print self.rcount

        FavWindow.setObjectName(_fromUtf8("FavWindow"))
        FavWindow.resize(640, 463)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        FavWindow.setFont(font)
        FavWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        
        self.labheader = QtGui.QLabel(FavWindow)
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
        self.tableWidget = QtGui.QTableWidget(FavWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 600, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.mainmenu_btn = QtGui.QPushButton(FavWindow)
        self.mainmenu_btn.setGeometry(QtCore.QRect(20, 22, 51, 51))
        self.mainmenu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainmenu_btn.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.mainmenu_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenu_btn.setIcon(icon)
        self.mainmenu_btn.setIconSize(QtCore.QSize(25, 25))
        self.mainmenu_btn.setFlat(False)
        self.mainmenu_btn.setObjectName(_fromUtf8("mainmenu_btn"))

        self.tableWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.tableWidget.setMaximumSize(QtCore.QSize(600, 300))
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
        
        self.tableWidget.setColumnCount(2)
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
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)

        self.retranslateUi(FavWindow)
        QtCore.QMetaObject.connectSlotsByName(FavWindow)

        self.mainmenu_btn.clicked.connect(self.btnMMClicked)

        fetch = self.cur.execute("select bwords, bmeanings from allwords where "+str(self.username)+"=3 or "+str(self.username)+"=1 order by bwords asc")
        fetch = list(fetch)

        for i in range(self.rcount):
            self.newitem1 = QtGui.QTableWidgetItem(fetch[i][0])
            self.newitem2 = QtGui.QTableWidgetItem(fetch[i][1])
            self.tableWidget.setItem(i,0,self.newitem1)
            self.tableWidget.setItem(i,1,self.newitem2)

    def retranslateUi(self, FavWindow):
        FavWindow.setWindowTitle(_translate("FavWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("FavWindow", "Favorites", None))
        self.tableWidget.setSortingEnabled(True)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def btnMMClicked(self):
        self.fw.hide()
        self.mw.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FavWindow = QtGui.QWidget()
    ui = Ui_FavWindow()
    ui.setupUi(FavWindow)
    FavWindow.show()
    sys.exit(app.exec_())

