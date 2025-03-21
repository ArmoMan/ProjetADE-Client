import time
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique

class CalibrerPh:
    
    """
    Après avoir effectué le calibrage manuel du potentiomètre vide (avec un fil à l’intérieur) avec un voltmètre,
    Utilisez cette classe avec des pH différents (2) pour calculer la tension afin de déterminer la marge d’erreur.
    """
    
    def __init__(self, ads1115_controleur: ADS1115Controleur, pin_analogique: PinAnalogique, taille_echantillon: int, valeur_ph_acide: float, valeur_ph_basique: float):
        """
        Args:
            ads1115_controleur (ADS1115Controleur): le ADC
            pin_analogique (PinAnalogique): le pin de l'ADC dont le capteur est branché
            taille_echantillon (int): nombre de mesures prises avant de faire la moyenne
            valeur_ph_acide (float): valeur du ph plus acide
            valeur_ph_basique (float): valeur du ph plus basique 
        """
        self.__taille_echantillon = taille_echantillon
        self.__ads1115_controleur = ads1115_controleur
        self.__pin_analogique = pin_analogique
        self.__valeur_ph_acide = valeur_ph_acide
        self.__valeur_ph_basique = valeur_ph_basique
        self.__valeur_ph_neutre = 7
        self.__valeur_voltage_neutre = 2.5275

    def commencer(self):
        """
        Méthode pour mesurer la marge de calibration à l'aide de deux solutions de pH.
        Avant d'appeler cette méthode, veuillez avoir effectué la calibration manuelle, ainsi qu'avoir déjà préparé les deux solutions de pH et l'eau pour le nettoyage.
        """
        
        print("Avant d'appeler cette méthode, veuillez avoir effectué la calibration manuelle, ainsi qu'avoir déjà préparé les deux solutions de pH et l'eau pour le nettoyage.")
        
        # dictonnaire des voltage des 2 solutions de ph
        dict_voltage = {}
        
        # Mesurer la valeur du voltage des deux solutions de PH
        for numero_mesure in range (0,2):
            
            print("Lavez le bout du capteur: vous avez 30 secondes")
            time.sleep(30)
            
            if numero_mesure == 0:
                print("Inserez d'abord dans le ph acide. La mesure commence dans 30 secondes")
                ph_actuel = self.__valeur_ph_acide
            else:
                print("Inserez maintenant dans le ph plus basique. La mesure commence dans 30 secondes")
                ph_actuel = self.__valeur_ph_basique
            time.sleep(30)
            
            print("Commence la prise de mesure")
            
            compteur = 0
            mesures_ignorees = 3
            liste_resultats = []
        
            # Faire la moyenne en se basant sur le nombre d'échantillons souhaité,
            # en ignorant les premières valeurs, car elles peuvent fausser le résultat.
            while compteur < self.__taille_echantillon + mesures_ignorees :
            
                # lire le voltage
                mesure = self.__ads1115_controleur.lire_voltage(self.__pin_analogique)
            
                # commencer la vraie mesure
                if compteur >= mesures_ignorees  :
                    print(f"mesure {len(liste_resultats)} : {mesure}")
                    liste_resultats.append(mesure)
                else:
                    print(compteur)
                compteur += 1
                
                # attendre 3 secondes après chaque mesure
                time.sleep(3)
        
            # la moyenne des resultats
            moyenne = sum(liste_resultats) / len(liste_resultats)
        
            print(f"Pour PH {ph_actuel} le voltage est de {moyenne}")
            dict_voltage[ph_actuel] = moyenne
            
            
        # donner la marge d'erreur
        if self.__valeur_ph_basique != 0 and self.__valeur_ph_acide != 0:
            marge = self.__calculer_pente(self.__valeur_ph_acide, self.__valeur_ph_basique,dict_voltage.get(self.__valeur_ph_acide) ,dict_voltage.get(self.__valeur_ph_basique))
            print(f"La marge est de {marge}")
    
    def __calculer_pente(self, x1: float, x2: float, y1: float, y2: float):
        """

        Args:
            x1 (float): valeur ph acide
            x2 (float): valeur ph basique
            y1 (float): valeur voltage du ph acide
            y2 (float): valeur voltage du ph basique

        Returns:
            float: pente (marge d'erreur)
        """
        difference_y = y2 - y1
        difference_x = x2 - x1
        pente = difference_y / difference_x
        
        return pente
    
    def tester_marge(self, marge: float):
        """
        Méthode qui permet de mesurer une ph
        """
        time.sleep(3)
        
        # equation 
        voltage_act = self.__ads1115_controleur.lire_voltage(self.__pin_analogique)
        ph_obtenu = self.__valeur_ph_neutre  + ((self.__valeur_voltage_neutre-voltage_act)/abs(marge))

        # res
        print(f"PH: {ph_obtenu} et V: {voltage_act}")

