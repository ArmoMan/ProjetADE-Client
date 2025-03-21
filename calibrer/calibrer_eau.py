import time
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique
 
class CalibrerEau:
   
    """
    Après avoir effectué le calibrage manuel du potentiomètre vide (avec un fil à l’intérieur) avec un voltmètre,
    Utilisez cette classe avec des niveaux d'eau différents (2) pour mesurer les niveaux de voltage différents
    """
   
    def __init__(self, ads1115_controleur: ADS1115Controleur, pin_analogique: PinAnalogique, taille_echantillon: int):
        """
        Args:
            ads1115_controleur (ADS1115Controleur): le ADC
            pin_analogique (PinAnalogique): le pin de l'ADC dont le capteur est branché
            taille_echantillon (int): nombre de mesures prises avant de faire la moyenne
            valeur_eau_min (float): valeur du niveau d'eau minimal
            valeur_eau_max (float): valeur du niveau d'eau maximal
        """
        self.__taille_echantillon = taille_echantillon
        self.__ads1115_controleur = ads1115_controleur
        self.__pin_analogique = pin_analogique
   
 
    def commencer(self):
        #"""
        #Méthode pour mesurer la marge de calibration à l'aide de deux niveaux différents d'eau.
        #Avant d'appeler cette méthode, veuillez avoir effectué la calibration manuelle (?)
        #"""
       
        # print("Avant d'appeler cette méthode, veuillez avoir effectué la calibration manuelle, ainsi qu'avoir déjà préparé les deux solutions de pH et l'eau pour le nettoyage.")
       
        # dictonnaire des voltage des 2 niveaux d'eau
        dict_voltage = {}
       
        # Mesurer la valeur du voltage des 2 niveaux d'eau
        for numero_mesure in range (0,2):
       
           
            if numero_mesure == 0:
                print("Inserez d'abord le capteur dans l'ensemble sans eau (niveau minimal). La mesure commence dans 30 secondes")
                niveau_eau_actuel = "Min"
            else:
                print("Inserez maintenant dans l'ensemble plein d'eau (niveau maximal). La mesure commence dans 30 secondes")
                niveau_eau_actuel = "Max"
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
       
            print(f"Pour le niveau d'eau de {niveau_eau_actuel} le voltage est de {moyenne}")
            dict_voltage[niveau_eau_actuel] = moyenne
           
   
   
   