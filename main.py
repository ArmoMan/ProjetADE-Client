from PySide6.QtWidgets import (QApplication)
import sys

from controlleurs.application.createur_capteurs import CreateurCapteur
from interface.acceuil_gui import AcceuilGUI

app = QApplication(sys.argv)
main_win = AcceuilGUI()
main_win.show()
sys.exit(app.exec())

# x = CreateurCapteur()
# x.generer_ky18()
# li = x.get_capteurs()
# for lis in li:
#     lis.mesurer_donnees()
# for lit in li:
#     print(lit.get_donnees())