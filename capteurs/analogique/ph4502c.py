import time
from capteurs.analogique.capteur_analogique_parent import CapteurAnalogiqueParent
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class Ph4502c(CapteurAnalogiqueParent):
    def __init__(self, controleur_adc: ADS1115Controleur, pin_analogique: PinAnalogique , marge: float):
        super().__init__("Ph4502c", {}, controleur_adc, pin_analogique)
        self.__voltage_max = 5
        self.__valeur_ph_neutre = 7
        self.__valeur_voltage_neutre = 2.5275
        self.__marge = marge
        
    def mesurer_donnees(self):
        """
        Méthode qui permet de mesurer un PH
        """
        time.sleep(1)
        
        # equation 
        voltage_actuel = self._controleur_adc.lire_voltage(self._pin)
        ph_obtenu = self.__valeur_ph_neutre  + ((self.__valeur_voltage_neutre - voltage_actuel)/abs(self.__marge))

        # ajouter aux données
        self._donnees["PH mesuré"] = ph_obtenu