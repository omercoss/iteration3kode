import mysql.connector
from PyQt6 import QtCore, QtWidgets
from GUI.MedicinAdministration import MedicinAdministration

class PatientProfil(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 526)
        self.patientprofilTitel = QtWidgets.QTextEdit(parent=Dialog)
        self.patientprofilTitel.setGeometry(QtCore.QRect(250, 30, 191, 31))
        self.patientprofilTitel.setObjectName("textEdit")

        self.cprnummerOmraade = QtWidgets.QTextBrowser(parent=Dialog)
        self.cprnummerOmraade.setGeometry(QtCore.QRect(20, 80, 311, 101))
        self.cprnummerOmraade.setObjectName("textBrowser")

        self.oplysningerOmraade = QtWidgets.QTextBrowser(parent=Dialog)
        self.oplysningerOmraade.setGeometry(QtCore.QRect(360, 80, 321, 431))
        self.oplysningerOmraade.setObjectName("textBrowser_2")

        self.medicinOplysningerKnap = QtWidgets.QCommandLinkButton(parent=Dialog)
        self.medicinOplysningerKnap.setGeometry(QtCore.QRect(530, 470, 141, 31))
        self.medicinOplysningerKnap.setObjectName("commandLinkButton")

        self.cprFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.cprFelt.setGeometry(QtCore.QRect(130, 100, 181, 21))
        self.cprFelt.setObjectName("textEdit_2")

        self.fornavnFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.fornavnFelt.setGeometry(QtCore.QRect(430, 120, 121, 21))
        self.fornavnFelt.setObjectName("textEdit_3")

        self.efternavnFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.efternavnFelt.setGeometry(QtCore.QRect(440, 150, 121, 21))
        self.efternavnFelt.setObjectName("textEdit_4")

        self.foedselsdagFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.foedselsdagFelt.setGeometry(QtCore.QRect(450, 180, 121, 21))
        self.foedselsdagFelt.setObjectName("textEdit_5")

        self.alderFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.alderFelt.setGeometry(QtCore.QRect(410, 220, 121, 21))
        self.alderFelt.setObjectName("textEdit_6")

        self.adresseFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.adresseFelt.setGeometry(QtCore.QRect(430, 250, 121, 21))
        self.adresseFelt.setObjectName("textEdit_7")

        self.telefonnummerFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.telefonnummerFelt.setGeometry(QtCore.QRect(490, 290, 121, 21))
        self.telefonnummerFelt.setObjectName("textEdit_8")

        self.visOplysningerKnap = QtWidgets.QPushButton(parent=Dialog)
        self.visOplysningerKnap.setGeometry(QtCore.QRect(190, 140, 131, 32))
        self.visOplysningerKnap.setObjectName("pushButton")

        self.sygdommeFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.sygdommeFelt.setGeometry(QtCore.QRect(460, 320, 121, 21))
        self.sygdommeFelt.setObjectName("textEdit_9")

        self.allergiFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.allergiFelt.setGeometry(QtCore.QRect(430, 360, 121, 21))
        self.allergiFelt.setObjectName("textEdit_10")

        self.koenFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.koenFelt.setGeometry(QtCore.QRect(410, 390, 121, 21))
        self.koenFelt.setObjectName("textEdit_11")

        self.hoejdeFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.hoejdeFelt.setGeometry(QtCore.QRect(420, 420, 121, 21))
        self.hoejdeFelt.setObjectName("textEdit_12")

        self.vaegtFelt = QtWidgets.QTextEdit(parent=Dialog)
        self.vaegtFelt.setGeometry(QtCore.QRect(410, 450, 121, 21))
        self.vaegtFelt.setObjectName("textEdit_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.visOplysningerKnap.clicked.connect(self.vis_oplysninger)
        self.visOplysningerKnap.clicked.connect(self.soegPatient)

        self.medicinOplysningerKnap.clicked.connect(self.MedicinAdministration)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.patientprofilTitel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#55aaff;\">Patient profil: </span></p></body></html>"))
        self.cprnummerOmraade.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">CPR-nummer: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.oplysningerOmraade.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Almene oplysninger </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Fornavn:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Efternavn:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Fødselsdag:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Alder:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Adresse:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Telefonnummer: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdomme: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Allergi:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Køn: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Højde:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Vægt:</span></p></body></html>"))
        self.medicinOplysningerKnap.setText(_translate("Dialog", "Medicinoplysninger"))
        self.visOplysningerKnap.setText(_translate("Dialog", "Vis oplysninger"))

    def vis_oplysninger(self):
        CPR = self.cprFelt.toPlainText()

        data = {
            '2610016748': {
                'Fornavn': 'Ömer',
                'Efternavn': 'Coskun',
                'Fødselsdag': '26-10-2001',
                'Alder': '21 år',
                'Adresse': 'Universitetsparken 2',
                'Telefonnummer': '68306738',
                'Sygdomme': 'PTSD / KOL',
                'Allergi': 'Pollen',
                'Køn': 'Mand',
                'Højde': '200 cm',
                'Vægt': '100 kg'
            },
            '1407669376': {
                'Fornavn': 'Sabrina',
                'Efternavn': 'Bibi',
                'Fødselsdag': '14-07-1966',
                'Alder': ' 56 år',
                'Adresse': 'Jagtvej 3',
                'Telefonnummer': '99338822',
                'Sygdomme': 'OCD / Astma',
                'Allergi': 'Husstøvmidler',
                'Køn': 'Kvinder',
                'Højde': '130 cm',
                'Vægt': '50 kg'
            }
        }

        patientdata = data.get(CPR)

        if patientdata:
            self.fornavnFelt.setText(patientdata['Fornavn'])
            self.efternavnFelt.setText(patientdata['Efternavn'])
            self.foedselsdagFelt.setText(patientdata['Fødselsdag'])
            self.alderFelt.setText(patientdata['Alder'])
            self.adresseFelt.setText(patientdata['Adresse'])
            self.telefonnummerFelt.setText(patientdata['Telefonnummer'])
            self.sygdommeFelt.setText(patientdata['Sygdomme'])
            self.allergiFelt.setText(patientdata['Allergi'])
            self.koenFelt.setText(patientdata['Køn'])
            self.hoejdeFelt.setText(patientdata['Højde'])
            self.vaegtFelt.setText(patientdata['Vægt'])

    def soegPatient(self):
        input = self.cprFelt.toPlainText()

        db = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Amagerkbh1313',
                database='dlm'
        )

        if db.is_connected():
            print("Forbindelse oprettet")
        else:
            print("Ingen forbindelse")
        
        print("Input:", input)

        cursor = db.cursor()

        query = f"SELECT * FROM patientoplysning WHERE CPRnummer = '{input}'"

        cursor.execute(query)

        resultater = cursor.fetchall()

        print(resultater)

        if resultater:
            patient_data = resultater[0]
            self.fornavnFelt.setPlainText(patient_data[1])
            self.efternavnFelt.setPlainText(patient_data[2])
            self.foedselsdagFelt.setPlainText(str(patient_data[3]))
            self.alderFelt.setPlainText(str(patient_data[4]))
            self.adresseFelt.setPlainText(patient_data[5])
            self.telefonnummerFelt.setPlainText(str(patient_data[6]))
            self.sygdommeFelt.setPlainText(patient_data[7])
            self.allergiFelt.setPlainText(patient_data[8])
            self.koenFelt.setPlainText(patient_data[9])
            self.hoejdeFelt.setPlainText(str(patient_data[10]))
            self.vaegtFelt.setPlainText(str(patient_data[11]))
        else:
            self.cprFelt.setText('Patient ikke fundet!')

    def MedicinAdministration(self):
        self.widget = QtWidgets.QWidget()
        self.ui = MedicinAdministration()
        self.ui.setupUi(self.widget)
        self.widget.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PatientProfil()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
