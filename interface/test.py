from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,QApplication,QLineEdit, QVBoxLayout, QLabel, QCheckBox,QHBoxLayout,QPushButton)
from PySide6.QtGui import  QFont,QColor

import sys

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accueil")
        self.resize(1000,700)
        ######## Choix capteurs #############
        ######## API #############
        conteneur_tout = QVBoxLayout()
        conteneur_tout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        # texte
        text_cle_api = QLabel("Entrez Votre Clé API :")
        text_cle_api.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # font
        font_text_api = text_cle_api.font()
        font_text_api.setBold(True)
        font_text_api.setPointSize(20)
        text_cle_api.setFont(font_text_api)
        
        input_cle_api = QLineEdit()
        input_cle_api.setMaximumWidth(400)
        
        conteneur_tout.addWidget(text_cle_api)
        conteneur_tout.addWidget(input_cle_api)
        #############################
        
        conteneur_checkboxes = QHBoxLayout()
        conteneur_checkboxes.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        self.checkboxes = [
            {
                "checkbox":QCheckBox("Ky18"),
            },
            {
                "checkbox":QCheckBox("ds18b20"),
            },
            {
                "checkbox":QCheckBox("ph4502c"),
            }
        ]
        
        for checkbox in self.checkboxes: 
            conteneur_checkboxes.addWidget(checkbox.get("checkbox"))
        
        conteneur_tout.addLayout(conteneur_checkboxes)
        
        #############################
        
        # Button commencer
        self.button_commencer = QPushButton("Commencer" )
        self.button_commencer.clicked.connect(self.ajouter_capteurs_choisis)
        
        conteneur_tout.addWidget(self.button_commencer)
        
        self.setLayout(conteneur_tout)
    def say(self):
        self.button_commencer.setText("defef")
    def ajouter_capteurs_choisis(self):
        for checkbox_boite in self.checkboxes:
            if checkbox_boite.get("checkbox").isChecked():
                self.say()