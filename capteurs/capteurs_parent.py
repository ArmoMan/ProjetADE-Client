from abc import ABC, abstractmethod

class CapteursParent(ABC):
    """
    Class parent pour les capteurs
    """
    def __init__(self, nom: str, donnees: dict, pin):
        self._nom = nom
        self._donnees = donnees
        self._pin = pin
        self._est_actionnable = False
    
    def get_nom(self) -> str:
        return self._nom
    
    def get_est_actionnable(self) -> bool:
         return self._est_actionnable
     
    def get_donnees(self) -> dict:
        return self._donnees
    
    @abstractmethod
    def mesurer_donnees(self):
        """
        Mesurer les donnes et ajouter au dictionnaire
        """
        pass