from abc import ABC
from capteurs.capteurs_parent import CapteursParent
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class CapteurAnalogiqueParent(CapteursParent, ABC):
    def __init__(self, nom: str, donnees: dict, controleur_adc: ADS1115Controleur, pin_analogique: PinAnalogique ):
        super().__init__(nom, donnees)
        self._pin_analogique = pin_analogique
        self._controleur_adc = controleur_adc
        