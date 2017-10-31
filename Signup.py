# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created: Sat Oct 14 11:58:03 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_SignupWindow(object):

    conn = sqlite3.connect('gre.db')

    def getUsername(self,username):
        self.username = username

    def setupUi(self, SignupWindow, flag, lw):

        self.sw = SignupWindow
        self.lw = lw

        SignupWindow.setObjectName(_fromUtf8("SignupWindow"))
        SignupWindow.resize(640, 480)
        SignupWindow.setGeometry(320, 100, 640, 480)
        SignupWindow.setMinimumSize(QtCore.QSize(640, 480))
        SignupWindow.setMaximumSize(QtCore.QSize(640, 480))
        SignupWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.981818, y2:0.955, stop:0 rgba(206, 36, 57, 255), stop:1 rgba(227, 100, 59, 255));"))
        self.txtUsername = QtGui.QLineEdit(SignupWindow)
        self.txtUsername.setGeometry(QtCore.QRect(440, 110, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        self.txtUsername.setFont(font)
        self.txtUsername.setToolTip(_fromUtf8(""))
        self.txtUsername.setAutoFillBackground(False)
        self.txtUsername.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);"))
        self.txtUsername.setInputMask(_fromUtf8(""))
        self.txtUsername.setText(_fromUtf8(""))
        self.txtUsername.setMaxLength(20)
        self.txtUsername.setFrame(False)
        self.txtUsername.setPlaceholderText(_fromUtf8(""))
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.txtPassword = QtGui.QLineEdit(SignupWindow)
        self.txtPassword.setGeometry(QtCore.QRect(440, 160, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setAutoFillBackground(False)
        self.txtPassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);"))
        self.txtPassword.setMaxLength(10)
        self.txtPassword.setFrame(False)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setPlaceholderText(_fromUtf8(""))
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.btnChangePwd = QtGui.QPushButton(SignupWindow)
        self.btnChangePwd.setGeometry(QtCore.QRect(350, 300, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnChangePwd.setFont(font)
        self.btnChangePwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnChangePwd.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btnChangePwd.setFlat(False)
        self.btnChangePwd.setObjectName(_fromUtf8("btnChangePwd"))
        self.label_5 = QtGui.QLabel(SignupWindow)
        self.label_5.setGeometry(QtCore.QRect(290, 50, 5, 361))
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(SignupWindow)
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
        self.label_7 = QtGui.QLabel(SignupWindow)
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
        self.label_8 = QtGui.QLabel(SignupWindow)
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
        self.lblUsername = QtGui.QLabel(SignupWindow)
        self.lblUsername.setGeometry(QtCore.QRect(310, 110, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.lblUsername.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUsername.setObjectName(_fromUtf8("lblUsername"))
        self.label_2 = QtGui.QLabel(SignupWindow)
        self.label_2.setGeometry(QtCore.QRect(440, 130, 161, 2))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(SignupWindow)
        self.label_3.setGeometry(QtCore.QRect(440, 180, 161, 2))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblPassword = QtGui.QLabel(SignupWindow)
        self.lblPassword.setGeometry(QtCore.QRect(310, 160, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword.setFont(font)
        self.lblPassword.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.lblPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.txtConfPassword = QtGui.QLineEdit(SignupWindow)
        self.txtConfPassword.setGeometry(QtCore.QRect(440, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtConfPassword.setFont(font)
        self.txtConfPassword.setAutoFillBackground(False)
        self.txtConfPassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);"))
        self.txtConfPassword.setMaxLength(10)
        self.txtConfPassword.setFrame(False)
        self.txtConfPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtConfPassword.setPlaceholderText(_fromUtf8(""))
        self.txtConfPassword.setObjectName(_fromUtf8("txtConfPassword"))
        self.label_4 = QtGui.QLabel(SignupWindow)
        self.label_4.setGeometry(QtCore.QRect(440, 230, 161, 2))
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 50);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lblConfPassword = QtGui.QLabel(SignupWindow)
        self.lblConfPassword.setGeometry(QtCore.QRect(310, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblConfPassword.setFont(font)
        self.lblConfPassword.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.lblConfPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblConfPassword.setObjectName(_fromUtf8("lblConfPassword"))
        self.btnCreateAC = QtGui.QPushButton(SignupWindow)
        self.btnCreateAC.setGeometry(QtCore.QRect(350, 300, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCreateAC.setFont(font)
        self.btnCreateAC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCreateAC.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btnCreateAC.setFlat(False)
        self.btnCreateAC.setObjectName(_fromUtf8("btnCreateAC"))

        self.btnCreateAC.clicked.connect(self.btnClicked)
        self.btnChangePwd.clicked.connect(self.btnChangePwdClicked)

        self.retranslateUi(SignupWindow)

        if flag==0:
            self.btnChangePwd.hide()
        else:
            self.btnChangePwd.show()
            self.btnCreateAC.hide()
            self.txtUsername.setText(self.username)
            self.txtUsername.setReadOnly(True)
            self.lblPassword.setText(_translate("SignupWindow", "New Password:", None))
            self.lblPassword.setGeometry(QtCore.QRect(310, 160, 121, 20))
            self.lblConfPassword = QtGui.QLabel(SignupWindow)

        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, SignupWindow):
        SignupWindow.setWindowTitle(_translate("SignupWindow", "GRE Vocab Builder", None))
        self.btnChangePwd.setText(_translate("SignupWindow", "CHANGE PASSWORD", None))
        self.label_6.setText(_translate("SignupWindow", "GRE", None))
        self.label_7.setText(_translate("SignupWindow", "VOCABULARY", None))
        self.label_8.setText(_translate("SignupWindow", "BUILDER", None))
        self.lblUsername.setText(_translate("SignupWindow", "USERNAME:", None))
        self.lblPassword.setText(_translate("SignupWindow", "PASSWORD:", None))
        self.lblConfPassword.setText(_translate("SignupWindow", "CONFIRM PASS:", None))
        self.btnCreateAC.setText(_translate("SignupWindow", "CREATE ACCOUNT", None))
        
        
    def btnClicked(self):
        if self.txtUsername.text()=="" or self.txtPassword.text()=="" or self.txtConfPassword.text()=="" :
            QtGui.QMessageBox.information(self.sw, 'Message', "Please provide appropriate information!")
        else:
        
            if self.txtPassword.text() == self.txtConfPassword.text():
                sql_stmt = "insert into users values(?,?);"
                try:
                    self.conn.execute(sql_stmt,(str(self.txtUsername.text()),str(self.txtPassword.text())))
                    self.conn.commit()
                    QtGui.QMessageBox.information(self.sw, 'Message', "Account Created Successfully!")
                    
                    self.conn.execute("alter table allwords add "+str(self.txtUsername.text())+" TEXT DEFAULT NA;")
                    self.conn.commit()

                    self.conn.execute("create table "+str(self.txtUsername.text())+" (Timestamp Date,QuizNo INT AUTO_INCREMENT,CorrectAnsCount INT,WrongAnsCount INT)")
                    self.conn.commit()

                    self.sw.hide()
                    self.lw.show()
                    
                    
                except sqlite3.IntegrityError:
                    QtGui.QMessageBox.information(self.sw, 'Message', "Username already exists!")
            else:
                QtGui.QMessageBox.information(self.sw, 'Message', "Password doesn't match!!Please re-enter password")
                
                
    def btnChangePwdClicked(self):
        if self.txtPassword.text() == self.txtConfPassword.text():
            sql_stmt = "update users set password ='"+str(self.txtPassword.text())+"' where username = '"+str(self.txtUsername.text())+"';"
            self.conn.execute(sql_stmt)
            self.conn.commit()
            QtGui.QMessageBox.information(self.sw, 'Message', "Password changed!")
            
            self.sw.hide()
            self.lw.show()
            
            
        else:
            QtGui.QMessageBox.information(self.sw, 'Message', "Password doesn't match!Please re-enter password")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SignupWindow = QtGui.QWidget()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec_())

