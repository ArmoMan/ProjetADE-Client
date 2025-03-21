
from w1thermsensor import W1ThermSensor

from capteurs.capteurs_parent import CapteursParent

class DS18B20(CapteursParent):
    """
    Classe pour calculer la température    
    
    ATTENTION !!! Le capteur doit être branché sur le pin 4 et :
    
    - Installation :
        pip install w1thermsensor --break-system-packages
        ou :
        sudo apt-get install python3-w1thermsensor
    - Configuration :
        1. Ouvrir le terminal et exécuter : sudo nano /boot/firmware/config.txt
        2. Trouver la ligne "dtoverlay=w1-gpio" et la décommenter
        3. Redémarrer le système
    """
    def __init__(self):
        super().__init__("DS18B20", {}, 4)
        self._capteur = W1ThermSensor()
    
    def mesurer_donnees(self):
        temp = self._capteur.get_temperature()
        self._donnees["Temperature (C)"] = temp