# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flcards.ui'
#
# Created: Wed Nov  1 17:25:41 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, QuizWindow):
        QuizWindow.setObjectName(_fromUtf8("QuizWindow"))
        QuizWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        QuizWindow.setFont(font)
        QuizWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.mainmenu_btn = QtGui.QPushButton(QuizWindow)
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
        self.labheader = QtGui.QLabel(QuizWindow)
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
        self.labword = QtGui.QLabel(QuizWindow)
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
        self.bookmark_cb = QtGui.QCheckBox(QuizWindow)
        self.bookmark_cb.setGeometry(QtCore.QRect(271, 359, 99, 22))
        self.bookmark_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bookmark_cb.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.bookmark_cb.setObjectName(_fromUtf8("bookmark_cb"))
        self.labnext = QtGui.QLabel(QuizWindow)
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
        self.btn_next = QtGui.QPushButton(QuizWindow)
        self.btn_next.setGeometry(QtCore.QRect(503, 412, 99, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_next.setFont(font)
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.layoutWidget = QtGui.QWidget(QuizWindow)
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
        self.labshowbtn = QtGui.QLabel(QuizWindow)
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
        self.rb_know = QtGui.QRadioButton(QuizWindow)
        self.rb_know.setGeometry(QtCore.QRect(240, 280, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.rb_know.setFont(font)
        self.rb_know.setObjectName(_fromUtf8("rb_know"))
        self.rb_notknow = QtGui.QRadioButton(QuizWindow)
        self.rb_notknow.setGeometry(QtCore.QRect(240, 310, 191, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.rb_notknow.setFont(font)
        self.rb_notknow.setObjectName(_fromUtf8("rb_notknow"))
        self.labprev = QtGui.QLabel(QuizWindow)
        self.labprev.setGeometry(QtCore.QRect(387, 411, 101, 31))
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
        self.btn_prev = QtGui.QPushButton(QuizWindow)
        self.btn_prev.setGeometry(QtCore.QRect(387, 412, 99, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_prev.setFont(font)
        self.btn_prev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_prev.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_prev.setObjectName(_fromUtf8("btn_prev"))
        self.btn_show = QtGui.QPushButton(QuizWindow)
        self.btn_show.setGeometry(QtCore.QRect(250, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.btn_show.setFont(font)
        self.btn_show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_show.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btn_show.setObjectName(_fromUtf8("btn_show"))

        self.retranslateUi(QuizWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizWindow)

    def retranslateUi(self, QuizWindow):
        QuizWindow.setWindowTitle(_translate("QuizWindow", "GRE Vocab Builder", None))
        self.labheader.setText(_translate("QuizWindow", "FLASHCARDS", None))
        self.labword.setText(_translate("QuizWindow", "WORD", None))
        self.bookmark_cb.setText(_translate("QuizWindow", "Bookmark", None))
        self.btn_next.setText(_translate("QuizWindow", "NEXT", None))
        self.labmeaning.setText(_translate("QuizWindow", "meaning", None))
        self.rb_know.setText(_translate("QuizWindow", "I knew this word", None))
        self.rb_notknow.setText(_translate("QuizWindow", "I didn\'t know this word", None))
        self.btn_prev.setText(_translate("QuizWindow", "BACK", None))
        self.btn_show.setText(_translate("QuizWindow", "SHOW MEANING", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QuizWindow = QtGui.QWidget()
    ui = Ui_QuizWindow()
    ui.setupUi(QuizWindow)
    QuizWindow.show()
    sys.exit(app.exec_())

