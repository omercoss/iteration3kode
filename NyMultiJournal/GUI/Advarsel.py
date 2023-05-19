from PyQt6 import QtCore, QtGui, QtWidgets
import GUI.MedicinAdministration


class Advarsel(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 496)
        self.advarselVindue = QtWidgets.QTextBrowser(parent=Form)
        self.advarselVindue.setGeometry(QtCore.QRect(130, 50, 491, 381))
        self.advarselVindue.setObjectName("textBrowser")

        self.varslendeTekst = QtWidgets.QTextBrowser(parent=Form)
        self.varslendeTekst.setGeometry(QtCore.QRect(190, 180, 371, 141))
        self.varslendeTekst.setObjectName("textBrowser_2")

        self.tom = QtWidgets.QLabel(parent=Form)
        self.tom.setGeometry(QtCore.QRect(500, 60, 111, 111))
        self.tom.setText("")
        self.tom.setPixmap(QtGui.QPixmap("download-kopi.png"))
        self.tom.setObjectName("label")

        self.okKnap = QtWidgets.QDialogButtonBox(parent=Form)
        self.okKnap.setGeometry(QtCore.QRect(410, 350, 164, 32))
        self.okKnap.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.okKnap.setObjectName("buttonBox")

        self.advarselTekst = QtWidgets.QLabel(parent=Form)
        self.advarselTekst.setGeometry(QtCore.QRect(150, 70, 81, 16))
        self.advarselTekst.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.okKnap.clicked.connect(self.nyAendring)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.varslendeTekst.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#fc0107;\">Obs:</span><span style=\" font-size:14pt;\"> Den ændrede dosis, kan påvirke &quot;navn&quot; behandlingsforløb i sygdom 2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#21ff06;\">Dobbeltjek:</span><span style=\" font-size:14pt;\"> Om de rigtige oplysninger er indtastet eller kontakt venligst, patientens andre behandlere for yderliger information.</span></p></body></html>"))
        self.advarselTekst.setText(_translate("Form", "ADVARSEL"))

    def nyAendring(self):
        self.widget = QtWidgets.QWidget()
        self.ui = GUI.MedicinAdministration.MedicinAdministration()
        self.ui.setupUi(self.widget)
        self.widget.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
