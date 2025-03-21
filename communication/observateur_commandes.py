from abc import ABC, abstractmethod


class ObservateurCommandes(ABC):
    """
    Observateur pour la gestion des commandes reçues par le WebSocketClient.
    """
    @abstractmethod
    def sur_commande_recu(self, commande: dict):
        """
        Méthode pour la gestion des commandes reçues par le WebSocketClient.
        """
        pass