from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QDateTime
from GUI.PatientProfil import PatientProfil
from GUI.LoginFejl import ForkertLogin as LoginFejl

class StartSide(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 631)
        self.startSideOmraade = QtWidgets.QListWidget(parent=Form)
        self.startSideOmraade.setGeometry(QtCore.QRect(70, 40, 671, 531))
        self.startSideOmraade.setObjectName("listWidget")

        self.brugernavnTekst = QtWidgets.QLabel(parent=Form)
        self.brugernavnTekst.setGeometry(QtCore.QRect(240, 230, 91, 16))
        self.brugernavnTekst.setObjectName("label")

        self.kodeordTekst = QtWidgets.QLabel(parent=Form)
        self.kodeordTekst.setGeometry(QtCore.QRect(260, 280, 60, 16))
        self.kodeordTekst.setObjectName("label_2")

        self.datoTid = QtWidgets.QDateTimeEdit(parent=Form)
        self.datoTid.setGeometry(QtCore.QRect(130, 450, 194, 24))
        self.datoTid.setObjectName("dateTimeEdit")

        nuværendeDatoTid = QDateTime.currentDateTime()
        self.datoTid.setDateTime(nuværendeDatoTid)
        self.datoTid.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.datoTid.setMinimumDateTime(nuværendeDatoTid)

        self.logIndKnap = QtWidgets.QPushButton(parent=Form)
        self.logIndKnap.setGeometry(QtCore.QRect(490, 320, 113, 32))
        self.logIndKnap.setObjectName("pushButton")

        self.startsideTitel = QtWidgets.QTextBrowser(parent=Form)
        self.startsideTitel.setGeometry(QtCore.QRect(170, 100, 421, 51))
        self.startsideTitel.setObjectName("textBrowser_3")

        self.laegeTekst = QtWidgets.QLabel(parent=Form)
        self.laegeTekst.setGeometry(QtCore.QRect(80, 50, 60, 16))
        self.laegeTekst.setObjectName("label_3")

        self.brugernavnFelt = QtWidgets.QTextEdit(parent=Form)
        self.brugernavnFelt.setGeometry(QtCore.QRect(320, 220, 271, 31))
        self.brugernavnFelt.setObjectName("textEdit")

        self.kodeordFelt = QtWidgets.QTextEdit(parent=Form)
        self.kodeordFelt.setGeometry(QtCore.QRect(320, 270, 271, 31))
        self.kodeordFelt.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.logIndKnap.clicked.connect(self.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.brugernavnTekst.setText(_translate("Form", "Læge-ID:"))
        self.kodeordTekst.setText(_translate("Form", "Kodeord:"))
        self.logIndKnap.setText(_translate("Form", "Log ind"))
        self.startsideTitel.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Multi-Electronic-Journal</span></p></body></html>"))
        self.laegeTekst.setText(_translate("Form", "Læge"))

    def login(self):
        brugernavn = self.brugernavnFelt.toPlainText()
        kodeord = self.kodeordFelt.toPlainText()

        if brugernavn == "læge" and kodeord == "112233":
            self.patient_profil = QtWidgets.QWidget()
            self.patient_profil_ui = PatientProfil()
            self.patient_profil_ui.setupUi(self.patient_profil)
            self.patient_profil.show()

        else:
            self.loginFejl = QtWidgets.QWidget()
            self.loginFejlUi = LoginFejl()
            self.loginFejlUi.setupUi(self.loginFejl)
            self.loginFejl.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())