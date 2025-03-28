
import json
import time
import socketio
import threading
from communication.observateur_commandes import ObservateurCommandes

class SocketIOClient:
    """
    Class pour créer une connexion socketio et envoyer les données.
    """
    
    def __init__(self, lien: str, cle_api: str):
        self.__lien = lien
        self.__cle_api = cle_api
        self.__observateurs: list[ObservateurCommandes] = []
        self.sio = socketio.Client()
        
        @self.sio.event
        def connect():
            print("Connexion avec succes")
            
        @self.sio.event
        def disconnect():
            print("Deconnexion")
        
        @self.sio.on("commande")
        def on_commande(data):
            # Notifier les observateurs (notamment l'ApplicationControleur) et retourner derniere reponse non null d'un des observateurs
            resultat_final = {
                "fini": True
            }
            try:
                conversion_json = data
            
                for observateur in self.__observateurs:
                    reponse = observateur.sur_commande_recu(conversion_json)
                    if reponse is not None:
                        resultat_final = reponse
                        
            except Exception as e:
                print(e)
                
            return self.convertir_donnees(resultat_final)
            
    
    def ajouter_observateur(self, observateur: ObservateurCommandes):
        self.__observateurs.append(observateur)
        
    def __connecter_serveur(self):
        print(self.__lien)
        self.sio.connect(self.__lien, headers={"cle_api": self.__cle_api})
        self.sio.wait()    
        
    def commencer_connexion(self):
        
        """
        Méthode pour commencer et maintenir une connexion socketio.
        """
            
        try: 
            # commencer sur un thread pour pas bloquer l'application
            self.thread = threading.Thread(target=self.__connecter_serveur)
            self.thread.daemon = True
            self.thread.start()
        except:
            # arreter tout pendant 30 secondes et recommencer la connection
            time.sleep(30)  
            self.commencer_connexion()
            
            
    def convertir_donnees(self, donnees_format_dict: dict):
        """
        Méthode pour convertir (le dictionnaire) au format JSON
        
        Args:
            donnees_format_json (dict): Les données qui vont être convertis
        """
        # https://www.w3schools.com/python/python_json.asp
        try:
            conversion_json = json.dumps(donnees_format_dict)
            return conversion_json
        except:
            print("Erreur durant l'envoie !")
            return False