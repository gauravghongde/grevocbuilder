# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Sat Oct 14 13:38:52 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Signup import Ui_SignupWindow
import sqlite3
from MainMenu import Ui_MainMenuWindow

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

class Ui_LoginWindow(object):
    conn = sqlite3.connect('gre.db')

    def setupUi(self, LoginWindow):

        self.lw = LoginWindow
        
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(640, 480)
        LoginWindow.setGeometry(320, 100, 640, 480)
        LoginWindow.setMinimumSize(QtCore.QSize(640, 480))
        LoginWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        LoginWindow.setFont(font)
        LoginWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.981818, y2:0.955, stop:0 rgba(206, 36, 57, 255), stop:1 rgba(227, 100, 59, 255));\n"
"color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(LoginWindow)
        self.label.setGeometry(QtCore.QRect(350, 70, 241, 51))
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.label_2.setMinimumSize(QtCore.QSize(31, 31))
        self.label_2.setMaximumSize(QtCore.QSize(31, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons8-User-48.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUsername = QtGui.QLineEdit(LoginWindow)
        self.txtUsername.setGeometry(QtCore.QRect(400, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.txtUsername.setFont(font)
        self.txtUsername.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtUsername.setToolTip(_fromUtf8(""))
        self.txtUsername.setAutoFillBackground(False)
        self.txtUsername.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.txtUsername.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtUsername.setInputMask(_fromUtf8(""))
        self.txtUsername.setText(_fromUtf8(""))
        self.txtUsername.setMaxLength(20)
        self.txtUsername.setFrame(False)
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.label_3 = QtGui.QLabel(LoginWindow)
        self.label_3.setGeometry(QtCore.QRect(360, 140, 31, 31))
        self.label_3.setMinimumSize(QtCore.QSize(31, 31))
        self.label_3.setMaximumSize(QtCore.QSize(31, 31))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icons8-Lock-26.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(LoginWindow)
        self.label_4.setGeometry(QtCore.QRect(350, 130, 241, 51))
        self.label_4.setMinimumSize(QtCore.QSize(241, 51))
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnLogin = QtGui.QPushButton(LoginWindow)
        self.btnLogin.setGeometry(QtCore.QRect(350, 200, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLogin.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.btnLogin.setFlat(False)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.label_5 = QtGui.QLabel(LoginWindow)
        self.label_5.setGeometry(QtCore.QRect(290, 50, 5, 361))
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(LoginWindow)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Audiowide"))
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(LoginWindow)
        self.label_7.setGeometry(QtCore.QRect(60, 220, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Audiowide"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(LoginWindow)
        self.label_8.setGeometry(QtCore.QRect(60, 250, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Audiowide"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.btnForgot = QtGui.QPushButton(LoginWindow)
        self.btnForgot.setGeometry(QtCore.QRect(455, 250, 131, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnForgot.setFont(font)
        self.btnForgot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnForgot.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnForgot.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.btnForgot.setObjectName(_fromUtf8("btnForgot"))
        self.label_9 = QtGui.QLabel(LoginWindow)
        self.label_9.setGeometry(QtCore.QRect(355, 300, 231, 20))
        self.label_9.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.btnSignup = QtGui.QPushButton(LoginWindow)
        self.btnSignup.setGeometry(QtCore.QRect(350, 350, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignup.setFont(font)
        self.btnSignup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignup.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSignup.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.btnSignup.setFlat(False)
        self.btnSignup.setObjectName(_fromUtf8("btnSignup"))
        self.txtPassword = QtGui.QLineEdit(LoginWindow)
        self.txtPassword.setGeometry(QtCore.QRect(400, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtPassword.setAutoFillBackground(False)
        self.txtPassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);"))
        self.txtPassword.setMaxLength(10)
        self.txtPassword.setFrame(False)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        
        self.txtUsername.setText("")

        self.btnLogin.clicked.connect(self.btnLoginClicked)
        self.btnSignup.clicked.connect(self.btnSignupClicked)
        self.btnForgot.clicked.connect(self.btnForgotClicked)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "GRE Vocab Builder", None))
        self.txtUsername.setPlaceholderText(_translate("LoginWindow", "Username", None))
        self.btnLogin.setText(_translate("LoginWindow", "LOGIN", None))
        self.label_6.setText(_translate("LoginWindow", "GRE", None))
        self.label_7.setText(_translate("LoginWindow", "VOCABULARY", None))
        self.label_8.setText(_translate("LoginWindow", "BUILDER", None))
        self.btnForgot.setText(_translate("LoginWindow", "Forgot Password ?", None))
        self.label_9.setText(_translate("LoginWindow", "------------ OR ------------", None))
        self.btnSignup.setText(_translate("LoginWindow", "SIGN UP", None))
        self.txtPassword.setPlaceholderText(_translate("LoginWindow", "Password", None))

    def btnForgotClicked(self):
        if self.txtUsername.text() =="" :
            QtGui.QMessageBox.information(self.lw, 'Message', "Please enter username!")
        else:
            cur = self.conn.cursor()
            cur.execute( "select username from users where username='"+str(self.txtUsername.text())+"';")
            rows = cur.fetchone()
            if rows == None:
                QtGui.QMessageBox.information(self.lw, 'Message', "Account doesn't exists!")
            else:
                self.lw.hide()
                self.window=QtGui.QWidget() 
            self.ui=Ui_SignupWindow()
            self.ui.getUsername(str(self.txtUsername.text()))
            self.ui.setupUi(self.window,1,self.lw)
            self.txtPassword.setText("")
            self.lw.hide()
            self.window.show()

    def btnSignupClicked(self):
        self.lw.hide()
        self.window=QtGui.QWidget() 
        self.ui=Ui_SignupWindow()
        self.ui.setupUi(self.window,0,self.lw)
        self.window.show()
    
    def btnLoginClicked(self):
        if self.txtUsername.text()=="" or self.txtPassword.text()=="":
            QtGui.QMessageBox.information(self.lw, 'Message', "Please enter username/password!")
        else:
            cur = self.conn.cursor()
            cur.execute( "select username,password from users where username='"+str(self.txtUsername.text())+"' and password='"+str(self.txtPassword.text())+"';")
            #cur.executemany(sql_stmt,(str(self.txtUsername.text()),str(self.txtPassword.text())))
            #self.conn.execute(sql_stmt,(str(self.txtUsername.text()),str(self.txtPassword.text())))
            #self.conn.commit()
            rows = cur.fetchone()
            #print rows
            if rows == None:#checking if LOGINID is present or not
                QtGui.QMessageBox.information(self.lw, 'Message', "Invalid username/password!")
            else:
                QtGui.QMessageBox.information(self.lw, 'Message', "Login successful!")
                self.lw.hide()
                self.MainWindow = QtGui.QMainWindow()
                self.ui = Ui_MainMenuWindow()
                self.ui.setupUi(self.MainWindow)
                self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginWindow = QtGui.QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

