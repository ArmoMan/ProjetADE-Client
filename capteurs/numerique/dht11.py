import time
import board
import adafruit_dht
from capteurs.capteurs_parent import CapteursParent

class DHT11(CapteursParent):
    """
    Classe représentant un capteur DHT11 qui utilise la bibliothèque
    adafruit-circuitpython-dht et le module board pour accéder aux broches du Raspberry Pi.
    """
    def __init__(self, pin: board):
        """
        Initialise le capteur DHT11.
        
        pin: La broche du Raspberry Pi spécifiée via le module board 
                    (exemple : board.D22 pour utiliser GPIO22).
        """
        # Appel du constructeur du parent en passant :
        # - "DHT11" comme nom du capteur,
        # - un dictionnaire vide pour stocker les mesures,
        # - la broche (pin) utilisée pour le capteur.
        super().__init__("DHT11", {}, pin)
        
        # Création de l'instance du capteur DHT11 à l'aide de la bibliothèque adafruit_dht.
        self._capteur = adafruit_dht.DHT11(pin)
    
    def mesurer_donnees(self):
        """
        Mesure la température et l'humidité à l'aide du capteur et met à jour le dictionnaire _donnees.
        
        Cette méthode récupère directement les attributs 'temperature' et 'humidity'
        de l'objet capteur. En cas d'erreur (par exemple, si le capteur ne répond pas),
        les valeurs seront enregistrées comme None et une erreur sera affichée.
        """
        try:
            # Récupération des mesures du capteur.
            temperature = self._capteur.temperature
            humidity = self._capteur.humidity
            
            # Mise à jour des données mesurées dans le dictionnaire.
            self._donnees["Temperature (C)"] = temperature
            self._donnees["Humidite (%)"] = humidity
        except Exception as e:
            # En cas d'erreur lors de la lecture, affecte None aux mesures et affiche l'erreur.
            self._donnees["Temperature (C)"] = None
            self._donnees["Humidite (%)"] = None
            print("Erreur lors de la lecture du capteur:", e)


