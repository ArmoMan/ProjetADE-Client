
from w1thermsensor import W1ThermSensor

from capteurs.capteurs_parent import CapteursParent

# Attention !!! Le capteur doit etre bracnhe au pin 4
# installer: pip install w1thermsensor --break-system-packages
# ou : sudo apt-get install python3-w1thermsensor
# ensuite allez dans terminal et faites: sudo nano /boot/firmware/config.txt
# allez dans la phrase "dtoverlay=w1-gpio" et de-commenter la 
# reboot le system

class DS18B20(CapteursParent):
    def __init__(self):
        super().__init__("DS18B20", {}, 4)
        self._capteur = W1ThermSensor()
    
    def mesurer_donnees(self):
        temp = self._capteur.get_temperature()
        self._donnees.update({"Temperature (C)", temp})