from PyQt6.QtWidgets import QApplication, QWidget
from GUI.StartSide import StartSide
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    ui = StartSide()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())