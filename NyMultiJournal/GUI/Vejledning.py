from PyQt6 import QtCore, QtGui, QtWidgets
import GUI.MedicinAdministration

class Vejledning(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 477)
        self.vejledningVindue = QtWidgets.QTextBrowser(parent=Form)
        self.vejledningVindue.setGeometry(QtCore.QRect(100, 70, 391, 271))
        self.vejledningVindue.setObjectName("textBrowser")

        self.vejledningTekst = QtWidgets.QLabel(parent=Form)
        self.vejledningTekst.setGeometry(QtCore.QRect(110, 80, 71, 16))
        self.vejledningTekst.setObjectName("label")

        self.tilbageKnap = QtWidgets.QPushButton(parent=Form)
        self.tilbageKnap.setGeometry(QtCore.QRect(360, 290, 113, 32))
        self.tilbageKnap.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.tilbageKnap.clicked.connect(self.tilbageFunktion)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vejledningVindue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#fc0107;\">Husk</span><span style=\" font-size:18pt;\"> at denne patient lider af \'sygdom\' og må ikke indtage mere end \'dosering\' af denne medicin om dagen</span></p></body></html>"))
        self.vejledningTekst.setText(_translate("Form", "Vejledning"))
        self.tilbageKnap.setText(_translate("Form", "Tilbage"))

    def tilbageFunktion(self):
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
