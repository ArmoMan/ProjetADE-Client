from capteurs.capteurs_parent import CapteursParent
import RPi.GPIO as GPIO

from capteurs.numerique.actionnable.parent_controleur_gpio import ParentControleurGPIO

class PompeControleur(ParentControleurGPIO):
    def __init__(self, pin_input_1: int, pin_input_2: int, pin_enable: int ):
        super().__init__("Pompe", {"Électricité", 0} ,{"pin_input_1":pin_input_1,"pin_input_2": pin_input_2,"pin_enable": pin_enable} )
        
        # freq et vitesse
        self.__pwm_pin = GPIO.PWM(pin_enable, 1000)
        self.__pwm_pin.start(0)
        
        # direction
        GPIO.output(pin_input_1, GPIO.HIGH)
        GPIO.output(pin_input_2, GPIO.LOW)

    def _activer(self):
        self.__pwm_pin.start(90)
        self._donnees["Électricité"]=1

    def _desactiver(self):
        self.__pwm_pin.start(0)
        self._donnees["Électricité"]=0

    def mesurer_donnees(self):
        pass
    
