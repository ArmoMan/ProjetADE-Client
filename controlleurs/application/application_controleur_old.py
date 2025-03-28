import threading
from typing import Union
from capteurs.numerique.actionnable.actionnable import Actionnable
from capteurs.numerique.ds18b20 import DS18B20
from capteurs.analogique.ky18 import CapteurKY18
from capteurs.analogique.ph4502c import Ph4502c
from capteurs.capteurs_parent import CapteursParent
from communication.observateur_commandes import ObservateurCommandes
from communication.websocket_client_2 import WebSocketClient
from capteurs.numerique.actionnable.pompe_controleur import PompeControleur
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class ApplicationControleur(ObservateurCommandes):
    
    def __init__(self, capteurs_choisis: list[CapteursParent], url: str, cle_api: str):
        self.__cle_api = cle_api
        self.__url = url
        self.__donees_pour_envoyer = {}
    
        # mettre en place les capteurs etc
        self.__capteurs_choisis = capteurs_choisis
 
        self.__gestionnaire_commandes = {
            "envoyer_donnees": self.__envoyer_donnees, 
            "actionner": self.__actionner_capteur
        }

        # le websocket
        self.__ws = WebSocketClient(url, cle_api)
        self.__ws.ajouter_observateur(self)
        self.__ws.commencer_connexion()
    
           
   
    def sur_commande_recu(self, commande:dict):
        """
        Méthode pour la gestion des commandes reçues par le WebSocketClient.
        """        
        command_valeur = commande.get("commande")
        if command_valeur in self.__gestionnaire_commandes:
            self.__gestionnaire_commandes[command_valeur](commande)
    
    def __actionner_capteur(self, commande:dict):
        nom_capteur = commande.get("nom_capteur")
        for capteur in self.__capteurs_choisis:
            if capteur.get_nom() == nom_capteur and isinstance(capteur, Actionnable):
                capteur.action()
    
    def __envoyer_donnees(self, commande):
        #prendre les mesures 
        self.__prendre_donnees()
                
        # envoyer les données
        self.__ws.envoyer_donnees(self.__donees_pour_envoyer)
    
    def __prendre_donnees(self):
        """
        Méthode pour récupérer les données et les mettre dans un dictionnaire.
        """

        # prendre mesures
        tous_les_capteurs = []
        for capteur in self.__capteurs_choisis:
            # mesurer donnees
            capteur.mesurer_donnees()
            donnees_recuperer = capteur.get_donnees()

            # recuperer donnees
            for nom_donnee, valeur in donnees_recuperer.items():
                tous_les_capteurs.append(
                    { "nom_capteur": capteur.get_nom(), "nom_donnee":nom_donnee, "donnee_collectee":valeur, "est_actionnable": capteur.get_est_actionnable() }
                )


        # former la forme de donnee
        self.__donees_pour_envoyer = {
            "appareil":{
                "cle_api": self.__cle_api,
                "tous_les_capteurs":tous_les_capteurs
            }
        }

                
