import json
import time
import threading
from websockets.sync.client import connect

from communication.observateur_commandes import ObservateurCommandes

class WebSocketClient:
    """
    Classe pour créer une connexion WebSocket et envoyer des données
    en utilisant du threading (avec l'aide du commencer_connexion() ).
    """
    
    def __init__(self, lien: str, cle_api: str):
        self.__lien = lien
        self.__cle_api = cle_api
        self.__observateurs: list[ObservateurCommandes] = []
        self.__websocket = None

    def ajouter_observateur(self, observateur: ObservateurCommandes):
        self.__observateurs.append(observateur)

    def __on_message(self, message):
        """
        Méthode appelée lorsqu'un message est reçu.
        Le message est converti en JSON et envoye aux observateurs.
        """
        conversion_json = json.loads(message)
        for observateur in self.__observateurs:
            observateur.sur_commande_recu(conversion_json)

    def __handle_connection(self):
        """
        Méthode de boucle de connexion qui :
          - Ouvre la connexion WebSocket.
          - Itère sur les messages reçus.
          - Gère les erreurs et tente de se reconnecter après un délai.
        """
        headers = {"cle_api": self.__cle_api}
        while True:
            try:
                # Ouverture de la connexion via le context manager
                with connect(
                    self.__lien,
                    open_timeout=10,
                    ping_interval=20,
                    ping_timeout=20,
                    close_timeout=10,
                    additional_headers=headers
                ) as ws:
                    self.__websocket = ws
                    print("Connexion websocket établie")
                    
                    for message in ws:
                        self.__on_message(message)
                    
                    
            except Exception as e:
                print("Erreur ou connexion perdue:", e)
                
            
            temps_connexion = 30
            print(f"Reconnexion dans {temps_connexion} secondes...")
            time.sleep(temps_connexion)

    def commencer_connexion(self):
        """
        Commencer la connexion WebSocket dans un thread 
        """
        thread = threading.Thread(target=self.__handle_connection, daemon=True)
        thread.start()
        self.__thread = thread  # On peut conserver la référence si nécessaire

    def envoyer_donnees(self, donnees_format_dict: dict):
        """
        Convertit le dictionnaire en JSON et envoie les données vers serveur
        """
        # https://www.w3schools.com/python/python_json.asp
        try:
            conversion_json = json.dumps(donnees_format_dict)
            self.__websocket.send(conversion_json)
        except:
            print("Erreur durant l'envoie !")
