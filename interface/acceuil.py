import threading
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,QApplication,QLineEdit, QVBoxLayout, QLabel, QCheckBox,QHBoxLayout,QPushButton,QMessageBox)
from PySide6.QtGui import  QFont,QColor
from controlleurs.application.application_controleur import ApplicationControleur
from controlleurs.application.createur_capteurs import CreateurCapteur

import sys

class Acceuil(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accueil")
        self.resize(1000,700)
        
        ######## Choix capteurs #############
        self.choix_cpateurs = CreateurCapteur()
        
        ######## API #############
        
        conteneur_tout = QVBoxLayout()
        conteneur_tout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        # texte
        self.text_cle_api = QLabel("Entrez Votre Clé API :")
        self.text_cle_api.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # font
        font_text_api = self.text_cle_api.font()
        font_text_api.setBold(True)
        font_text_api.setPointSize(20)
        self.text_cle_api.setFont(font_text_api)
        
        self.input_cle_api = QLineEdit()
        self.input_cle_api.setMaximumWidth(400)
        
        conteneur_tout.addWidget(self.text_cle_api)
        conteneur_tout.addWidget(self.input_cle_api)
        
        ########## checkbox ############
        
        conteneur_checkboxes = QHBoxLayout()
        conteneur_checkboxes.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        self.checkboxes = [
            {
                "checkbox":QCheckBox("Ky18"),
                "capteur": self.choix_cpateurs.generer_ky18
            },
            {
                "checkbox":QCheckBox("ds18b20"),
                "capteur": self.choix_cpateurs.generer_ds18b20
            },
            {
                "checkbox":QCheckBox("ph4502c"),
                "capteur": self.choix_cpateurs.generer_ph4502c
            }
        ]
        
        for checkbox in self.checkboxes: 
            conteneur_checkboxes.addWidget(checkbox.get("checkbox"))
        
        conteneur_tout.addLayout(conteneur_checkboxes)
        
        ####### Button commencer ##########        
        # Button commencer
        self.button_commencer = QPushButton("Commencer")
        self.button_commencer.clicked.connect(self.__commencer)
        
        conteneur_tout.addWidget(self.button_commencer)
        
        self.setLayout(conteneur_tout)
    
    def __commencer(self):
        """
        Methode pour commencer la prise de mesure
        """
        
        # verifier que cle api pas vide
        cle_api = self.input_cle_api.text()
        if len(cle_api) == 0:
            QMessageBox.warning(self, "Cle api vide")
            return
        
        #ajouter capteurs 
        self.__ajouter_capteurs_choisis()
        
        # cacher button commencer
        self.button_commencer.setVisible(False)
        
        # commencer à prendre des mesures
        # pour ne pas faire freezer l'interfacem utiliser des threads
        ApplicationControleur(self.choix_cpateurs.get_capteurs(), "ws://192.168.0.214:4545", cle_api)

       



    
    def __ajouter_capteurs_choisis(self):
        """
        Regarder les capteurs choisis et les ajouter
        """
        for checkbox_boite in self.checkboxes:
            checkbox: QCheckBox = checkbox_boite.get("checkbox")
            if checkbox.isChecked():
                checkbox_boite.get("capteur")()