import time
from capteurs.analogique.capteur_analogique_parent import CapteurAnalogiqueParent
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class Ph4502c(CapteurAnalogiqueParent):
    def __init__(self, controleur_adc: ADS1115Controleur, pin_analogique: PinAnalogique , marge: float):
        super().__init__("Ph4502c", {}, controleur_adc, pin_analogique)
        self._voltage_max = 5
        self._valeur_ph_neutre = 7
        self._valeur_voltage_neutre = 2.5275
        self._marge = marge
        
    def mesurer_donnees(self):
        """
        Methode qui permet de mesurer une ph
        """
        time.sleep(1)
        
        # equation 
        voltage_actuel = self._controleur_adc.lire_voltage(self._pin)
        ph_obtenu = self._valeur_ph_neutre  + ((self._valeur_voltage_neutre - voltage_actuel)/abs(self._marge))

        # ajouter aux données
        self._donnees.update({"Ph mesuré", ph_obtenu})