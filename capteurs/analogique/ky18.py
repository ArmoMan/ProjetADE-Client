from capteurs.analogique.capteur_analogique_parent import CapteurAnalogiqueParent
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class CapteurKY18(CapteurAnalogiqueParent):
    def __init__(self, controleur_adc: ADS1115Controleur, pin_analogique: PinAnalogique, resistance_interne: float):
        super().__init__("ky18", {}, controleur_adc, pin_analogique)
        self.__voltage_max = 5
        self.__resistance_interne = resistance_interne
        
    def mesurer_donnees(self):

        # Mesurer la résistance grâce à l’équation du diviseur de tension où R est isolée
        voltage = self._controleur_adc.lire_voltage(self._pin)
        resistance = self.__resistance_interne * (voltage / (self.__voltage_max - voltage))
        
        self._donnees[ "Résistance face à la lumière (Ohm)"] = resistance