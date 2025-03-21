 
from controlleurs.composants.adc.pin_analogique import PinAnalogique
import board 
import busio
import adafruit_ads1x15.ads1115 as ADS 
from adafruit_ads1x15.analog_in import AnalogIn

class ADS1115Controleur:    
    """
    Cette classe permet de contrôler le convertisseur ADS1115. 
    Il contient des methodes qui permettent de lire la valeur analogique et de mesurer la tension en volts.    
    """
    
    def __init__(self):
        # mettre en place le type de communication -> esclave & maitre
        self.__i2c_communication = busio.I2C(board.SCL, board.SDA)
        
        # ajouter cette type de communication au convertiseur voulu (pour nous c'est le ADS1115)
        self.__convertiseur = ADS.ADS1115(self.__i2c_communication)
        
    
    # Class pour retourner la valeur analogique du convertiseur. C'est entre 0 et 65535, car le ADC est de 16-bit
    def lire_analogique(self,pin_analogique: PinAnalogique) -> int:
        """
        Methode pour lire la valeur analogique
        
        Args:
            pin_analogique (PinAnalogique): le pin choisi pour lire la valeur

        Returns:
            int: la valeur analogique du convertiseur. C'est entre 0 et 65535, car le ADC est de 16-bit
        """
        # Lecture de signale analogue au pin choisi
        lecture_pin = AnalogIn(self.__convertiseur, pin_analogique.value)
        
        return lecture_pin.value
    
    # methode pour lire le voltage
    def lire_voltage(self,pin_analogique: PinAnalogique) -> float:
        """
        Methode pour lire le voltage
        
        Args:
            pin_analogique (PinAnalogique): le pin choisi pour lire la valeur

        Returns:
            float: voltage
        """
        # Lecture de signale analogue au pin choisi
        lecture_pin = AnalogIn(self.__convertiseur, pin_analogique.value)
        
        return lecture_pin.voltage
    