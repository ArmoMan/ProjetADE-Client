from abc import ABC, abstractmethod

class CapteursParent(ABC):
    """
    Class parent pour les capteurs
    """
    def __init__(self, nom: str, donnees: dict, pin):
        self._nom = nom
        self._donnees = donnees
        self._pin = pin
    
    def get_nom(self) -> str:
        return self._name
    
    def get_donnees(self) -> dict:
        return self._donnees
    
    @abstractmethod
    def mesurer_donnees(self):
        """
        Mesurer les donnes et ajouter au dictionnaire
        """
        pass