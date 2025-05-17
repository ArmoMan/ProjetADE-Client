import json
import time
import websocket
import rel
from communication.observateur_commandes import ObservateurCommandes

class WebSocketClient:
    """
    Class pour créer une connexion WebSocket et envoyer les données.
    """
    # https://websocket-client.readthedocs.io/en/latest/examples.html
    
    def __init__(self, lien: str, cle_api: str):
        self.__lien = lien
        self.__cle_api = cle_api
        self.__observateurs: list[ObservateurCommandes] = []
        
    def ajouter_observateur(self, observateur: ObservateurCommandes):
        self.__observateurs.append(observateur)
        
    def __on_message(self,mon_websocket,commande):
        """
        Méthode appelée lorsque le client reçoit un message de la part du serveur.
        Le message reçu sera traité comme un string dans notre cas. Donc, le serveur doit aussi envoyer les commandes au format texte simple, 
        Par exemple : "arreter_pompe" ou "envoyer_data".
        """
        # Notifier les observateurs (notamment l'ApplicationControleur)
        conversion_json = json.loads(commande)

        for observateur in self.__observateurs:
            observateur.sur_commande_recu(conversion_json)
        
    def __on_close(self, mon_websocket, close_status_code, close_msg):
        print("Connexion perdue")

    def __on_open(self, mon_websocket):
        print("Connexion websocket")
        
    def commencer_connexion(self):
        """
        Méthode pour commencer et maintenir une connexion WebSocket.
        """
        try: 
            self.__websocket = websocket.WebSocketApp(
            self.__lien, 
            header={"cle_api": f"{self.__cle_api}"} ,
            on_open=self.__on_open, 
            on_message=self.__on_message, 
            on_close=self.__on_close
            )
          
            # pour se reconnecter
            self.__websocket.run_forever(dispatcher=rel, reconnect=10)
            rel.dispatch()
        except:
            # arreter tout pendant 30 secondes et recommencer la connection
            time.sleep(30)  
            self.commencer_connexion()
    
    def envoyer_donnees(self, donnees_format_dict: dict):
        """
        Méthode pour convertir (le dictionnaire) et envoyer les données au format JSON vers le serveur.
        
        Args:
            donnees_format_json (dict): Les données qui vont être envoyées
        """
        # https://www.w3schools.com/python/python_json.asp
        try:
            conversion_json = json.dumps(donnees_format_dict)
            self.__websocket.send(conversion_json)
        except:
            print("Erreur durant l'envoie !")