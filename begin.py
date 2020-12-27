from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_startwindo(object):
    def __init__(self):
        self.fname = QtWidgets.QLineEdit(startwindo)
        self.lname = QtWidgets.QLineEdit(startwindo)
        self.name = QtWidgets.QLineEdit(startwindo)
        self.lname_l = QtWidgets.QLabel(startwindo)
        self.fname_l = QtWidgets.QLabel(startwindo)
        self.name_l = QtWidgets.QLabel(startwindo)
        self.label_4 = QtWidgets.QLabel(startwindo)
        self.exit = QtWidgets.QPushButton(startwindo)
        self.save = QtWidgets.QPushButton(startwindo)

    def setupUi(self, startwindo):
        startwindo.setObjectName("startwindo")
        startwindo.resize(500, 400)
        startwindo.setMinimumSize(QtCore.QSize(500, 400))
        startwindo.setMaximumSize(QtCore.QSize(500, 400))
        self.fname.setGeometry(QtCore.QRect(172, 100, 141, 22))
        self.fname.setObjectName("fname")
        self.lname.setGeometry(QtCore.QRect(172, 160, 141, 22))
        self.lname.setObjectName("lname")
        self.name.setGeometry(QtCore.QRect(172, 220, 141, 22))
        self.name.setObjectName("name")
        self.lname_l.setGeometry(QtCore.QRect(330, 160, 81, 16))
        self.lname_l.setObjectName("lname_l")
        self.fname_l.setGeometry(QtCore.QRect(380, 100, 31, 20))
        self.fname_l.setObjectName("fname_l")
        self.name_l.setGeometry(QtCore.QRect(330, 220, 81, 20))
        self.name_l.setObjectName("name_l")
        self.label_4.setGeometry(QtCore.QRect(200, 20, 111, 41))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.save.setGeometry(QtCore.QRect(130, 320, 93, 28))
        self.save.setObjectName("save")
        self.exit.setGeometry(QtCore.QRect(300, 320, 93, 28))
        self.exit.setObjectName("exit")
        #click
        self.save.clicked.connect(self.ret)
        self.exit.clicked.connect(self.close)

        self.retranslateUi(startwindo)
        QtCore.QMetaObject.connectSlotsByName(startwindo)

    def retranslateUi(self, startwindo):
        _translate = QtCore.QCoreApplication.translate
        startwindo.setWindowTitle(_translate("startwindo", "start windo"))
        self.lname_l.setText(_translate("startwindo", "نام خوانوادگی"))
        self.fname_l.setText(_translate("startwindo", "نام"))
        self.name_l.setText(_translate("startwindo", "نام واحد تجاری"))
        self.label_4.setText(_translate("startwindo", "<html><head/><body><p><span style=\" font-size:14pt;\">به نام خدا</span></p></body></html>"))
        self.save.setText(_translate("startwindo", "ذخیره"))
        self.exit.setText(_translate("startwindo", "انصراف"))

    def close(self):
        self.close()

    def ret(self):
        self.close()
        return self.name, self.fname, self.lname


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startwindo = QtWidgets.QWidget()
    ui = Ui_startwindo()
    ui.setupUi(startwindo)
    startwindo.show()
    sys.exit(app.exec_())
