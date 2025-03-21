# import time
# import platform
# import Adafruit_DHT

# from capteurs.capteurs_parent import CapteursParent

# class DHTSensor(CapteursParent):
#     """
#     Classe pour un capteur d'humidité et de température (DHT22)
#     """
#     def __init__(self, sensor_type=Adafruit_DHT.DHT22, gpio_pin=22):
#         super().__init__("DHT22", {}, gpio_pin)
#         self.sensor_type = sensor_type
#         self._gpio_pin = gpio_pin
#         self._donnees = {}

#     def mesurer_donnees(self):
#         """
#         Lit l'humidité et la température du capteur et met à jour le dictionnaire _donnees.
#         """
#         humidity, temperature = Adafruit_DHT.read_retry(self.sensor_type, self._gpio_pin)
#         if humidity is not None and temperature is not None:
#             self._donnees["Temperature (C)"] = temperature
#             self._donnees["Humidite (%)"] = humidity
#         else:
#             self._donnees["Temperature (C)"] = None
#             self._donnees["Humidite (%)"] = None

#     def get_donnees(self):
#         return self._donnees

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


