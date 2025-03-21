from abc import ABC, abstractmethod


class Actionnable(ABC):
    """
    Interface pour les classes qui peuvent faire une action
    """
    @abstractmethod
    def action(self,commande):
        """
        Méthode pour entâmer une action
        """
        pass
    
    @abstractmethod
    def _activer(self):
        """
        Méthode générique pour activer l’actionneur
        """
        pass
        
    @abstractmethod
    def _desactiver(self):
        """
        Méthode générique pour désactiver l’actionneur
        """
        pass