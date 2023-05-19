from PyQt6 import QtCore, QtGui, QtWidgets
import GUI.PatientProfil


class Oplysning(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(723, 591)
        self.oplysningVindue = QtWidgets.QTextBrowser(parent=Dialog)
        self.oplysningVindue.setGeometry(QtCore.QRect(160, 130, 431, 341))
        self.oplysningVindue.setObjectName("textBrowser")

        self.oplysendeTekst = QtWidgets.QTextBrowser(parent=Dialog)
        self.oplysendeTekst.setGeometry(QtCore.QRect(240, 190, 281, 201))
        self.oplysendeTekst.setObjectName("textBrowser_2")

        self.tom = QtWidgets.QLabel(parent=Dialog)
        self.tom.setGeometry(QtCore.QRect(160, 130, 161, 31))
        self.tom.setText("")
        self.tom.setObjectName("label")

        self.tom2 = QtWidgets.QLabel(parent=Dialog)
        self.tom2.setGeometry(QtCore.QRect(240, 390, 35, 10))
        self.tom2.setScaledContents(True)
        self.tom2.setObjectName("label_2")

        self.tom3 = QtWidgets.QLabel(parent=Dialog)
        self.tom3.setGeometry(QtCore.QRect(480, 140, 171, 101))
        self.tom3.setText("")
        self.tom3.setPixmap(QtGui.QPixmap("../../Downloads/339490694_2294329397405148_6702489177475268657_n.png"))
        self.tom3.setObjectName("label_3")

        self.okKnap = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.okKnap.setGeometry(QtCore.QRect(360, 400, 164, 32))
        self.okKnap.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.okKnap.setObjectName("buttonBox")

        self.oplysningTekst = QtWidgets.QLabel(parent=Dialog)
        self.oplysningTekst.setGeometry(QtCore.QRect(180, 140, 81, 21))
        self.oplysningTekst.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.okKnap.clicked.connect(self.aendringGemt)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.oplysendeTekst.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Er du sikker på at du vil ændre dosis for pågældende medicin?</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Husk at den ændrede dosis kan have konseksvens for patientens andre sygdomme?</span></p></body></html>"))
        self.oplysningTekst.setText(_translate("Dialog", "OPLYSNING"))

    def aendringGemt(self):
        self.widget = QtWidgets.QWidget()
        self.ui = GUI.PatientProfil.PatientProfil()
        self.ui.setupUi(self.widget)
        self.widget.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
