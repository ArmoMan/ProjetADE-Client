from capteurs.analogique.capteur_analogique_parent import CapteurAnalogiqueParent
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique




class CapteurArduinoWaterSensor(CapteurAnalogiqueParent):
    def __init__(self, controleur_adc: ADS1115Controleur, pin_analogique: PinAnalogique, voltage_max: float, voltage_min: float):
        super().__init__("Arduino Water Sensor", {}, controleur_adc, pin_analogique, )
        self._voltage_max = voltage_max 
        self._voltage_min = voltage_min 


        
    def mesurer_donnees(self):
        voltage = self._controleur_adc.lire_voltage(self._pin)
        if voltage > self._voltage_max :
            pourcentage_immersion = 100.0
        elif voltage < self._voltage_min:
            pourcentage_immersion = 0.0
        else:
            pourcentage_immersion = ((voltage - self._voltage_min) / (self._voltage_max  - self._voltage_min)) * 100
        
        self._donnees["Niveau d'eau [%]"] = pourcentage_immersion
        





























