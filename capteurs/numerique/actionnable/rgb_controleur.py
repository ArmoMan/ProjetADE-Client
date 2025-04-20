import RPi.GPIO as GPIO
from capteurs.numerique.actionnable.parent_controleur_gpio import ParentControleurGPIO


class RGBControleur(ParentControleurGPIO):
    def __init__(self, pin_rouge: int, pin_vert: int, pin_bleu: int):
        super().__init__("Lumière", "Électricité", {"pin_rouge": pin_rouge,"pin_vert": pin_vert,"pin_bleu": pin_bleu})

        # pour commencer desactivé
        self._desactiver()
        
    def mesurer_donnees(self):
        pass
    
    def _activer(self):
        """
        Méthode générique pour activer l’actionneur
        """
        for pin in self._gpio_pins.values():
            GPIO.output(pin, GPIO.LOW)
        self._donnees["Électricité"]=1

        
    def _desactiver(self):
        """
        Méthode générique pour désactiver l’actionneur
        """
        for pin in self._gpio_pins.values():
            GPIO.output(pin, GPIO.HIGH)
        self._donnees["Électricité"]=0

    
    