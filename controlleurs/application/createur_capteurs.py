
from capteurs.analogique.ky18 import CapteurKY18
from capteurs.analogique.ph4502c import Ph4502c
from capteurs.capteurs_parent import CapteursParent
from capteurs.numerique.ds18b20 import DS18B20
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique


class CreateurCapteur:
    """
    Classe pour générer des capteurs et utiliser cette classe pour donner la liste des capteurs à l'application contrôleur.
    """
    def __init__(self):
        self.__capteurs = []
        self.__est_capteurs_analogiques = False 
    
    def get_capteurs(self) -> list[CapteursParent]:
        return self.__capteurs
    
    def generer_ds18b20(self):
        self.__capteurs.append(DS18B20())
    
    def generer_ky18(self):
        self.__verifier_creation_adc()
        self.__capteurs.append(CapteurKY18(self._analogique_contoleur, PinAnalogique.A0))
    
    def generer_ph4502c(self):
        self.__verifier_creation_adc()
        self.__capteurs.append(Ph4502c(self._analogique_contoleur, PinAnalogique.A1, -0.17224))

    def __verifier_creation_adc(self):
        """
        Méthode à appeler afin de vérifier qu'un contrôleur de convertisseur a déjà été créé.
        """
        if not self.__est_capteurs_analogiques:
            self.__est_capteurs_analogiques = True
            self._analogique_contoleur = ADS1115Controleur()