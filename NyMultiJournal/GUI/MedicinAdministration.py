from PyQt6 import QtCore, QtWidgets
from GUI.Vejledning import Vejledning
from GUI.Advarsel import Advarsel
from GUI.Oplysning import Oplysning

class MedicinAdministration(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 473)
        self.medicinadministrationTitel = QtWidgets.QTextBrowser(parent=Dialog)
        self.medicinadministrationTitel.setGeometry(QtCore.QRect(170, 10, 221, 31))
        self.medicinadministrationTitel.setObjectName("textBrowser")

        self.doseringOmraade = QtWidgets.QTextBrowser(parent=Dialog)
        self.doseringOmraade.setGeometry(QtCore.QRect(60, 60, 431, 401))
        self.doseringOmraade.setObjectName("textBrowser_2")

        self.doseringKnap1 = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doseringKnap1.setGeometry(QtCore.QRect(270, 100, 62, 22))
        self.doseringKnap1.setObjectName("doubleSpinBox")

        self.doseringKnap2 = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doseringKnap2.setGeometry(QtCore.QRect(270, 200, 62, 22))
        self.doseringKnap2.setObjectName("doubleSpinBox_2")

        self.doseringKnap3 = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doseringKnap3.setGeometry(QtCore.QRect(270, 300, 62, 22))
        self.doseringKnap3.setObjectName("doubleSpinBox_3")

        self.acceptKnap = QtWidgets.QPushButton(parent=Dialog)
        self.acceptKnap.setGeometry(QtCore.QRect(320, 410, 161, 32))
        self.acceptKnap.setObjectName("pushButton")

        self.vejledningKnap1 = QtWidgets.QToolButton(parent=Dialog)
        self.vejledningKnap1.setGeometry(QtCore.QRect(350, 100, 81, 22))
        self.vejledningKnap1.setObjectName("toolButton")

        self.vejledningKnap2 = QtWidgets.QToolButton(parent=Dialog)
        self.vejledningKnap2.setGeometry(QtCore.QRect(350, 200, 81, 22))
        self.vejledningKnap2.setObjectName("toolButton_2")

        self.vejledningKnap3 = QtWidgets.QToolButton(parent=Dialog)
        self.vejledningKnap3.setGeometry(QtCore.QRect(350, 300, 81, 22))
        self.vejledningKnap3.setObjectName("toolButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.vejledningKnap1.clicked.connect(self.vis_vejledning)
        self.vejledningKnap2.clicked.connect(self.vis_vejledning)
        self.vejledningKnap3.clicked.connect(self.vis_vejledning)

        self.acceptKnap.clicked.connect(self.accepter)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.medicinadministrationTitel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600;\">Medicin administration</span></p></body></html>"))
        self.doseringOmraade.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom1 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin1 = </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin2 = </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin3 =</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\"> Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.acceptKnap.setText(_translate("Dialog", "Accepter ændringer"))
        self.vejledningKnap1.setText(_translate("Dialog", "Vejledning"))
        self.vejledningKnap2.setText(_translate("Dialog", "Vejledning"))
        self.vejledningKnap3.setText(_translate("Dialog", "Vejledning"))

    def vis_vejledning(self):
        self.vejledning_widget = QtWidgets.QWidget()
        self.vejledning_widget_ui = Vejledning()
        self.vejledning_widget_ui.setupUi(self.vejledning_widget)
        self.vejledning_widget.show()

    def accepter(self):
        medicin1_dosering = self.doseringKnap1.value()
        medicin2_dosering = self.doseringKnap2.value()
        medicin3_dosering = self.doseringKnap3.value()

        if medicin1_dosering < 1 or medicin1_dosering > 5 or \
           medicin2_dosering < 1 or medicin2_dosering > 5 or \
           medicin3_dosering < 1 or medicin3_dosering > 5:

            self.advarsel_widget = QtWidgets.QWidget()
            self.advarsel_widget_ui = Advarsel()
            self.advarsel_widget_ui.setupUi(self.advarsel_widget)
            self.advarsel_widget.show()

        else:
            self.oplysning_widget = QtWidgets.QWidget()
            self.oplysning_widget_ui = Oplysning()
            self.oplysning_widget_ui.setupUi(self.oplysning_widget)
            self.oplysning_widget.show()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
