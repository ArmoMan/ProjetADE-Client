from PySide6.QtWidgets import (QApplication)
import sys

from controlleurs.application.createur_capteurs import CreateurCapteur
from interface.acceuil_gui import AcceuilGUI

app = QApplication(sys.argv)
main_win = AcceuilGUI()
main_win.show()
sys.exit(app.exec())