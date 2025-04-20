from abc import ABC, abstractmethod
from capteurs.capteurs_parent import CapteursParent
import RPi.GPIO as GPIO
from capteurs.numerique.actionnable.actionnable import Actionnable

class ParentControleurGPIO(CapteursParent, Actionnable, ABC):
    def __init__(self, nom, nom_donnee, pins:dict[str, int]):
        """
        Classe de base pour les actionneurs contrôlés par les pins GPIO (out)
        """
        super().__init__(nom, {nom_donnee: 0}, pins)
        self._gpio_pins = pins
        self._est_actionnable = True
        self.__configurer_pins()
    
    def __configurer_pins(self):
        """
        Configure les broches GPIO comme sortant
        """
        GPIO.setmode(GPIO.BCM)
        for pin in self._gpio_pins.values():
            GPIO.setup(pin, GPIO.OUT)

    def action(self):
        """
        Méthode pour entâmer une action: eteindre ou allumer
        """
        if self._donnees.get("Électricité") == 0:
            self._activer()
        else:
            self._desactiver()
            
