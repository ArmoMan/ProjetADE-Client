from enum import Enum
import adafruit_ads1x15.ads1015 as ADS 

class PinAnalogique(Enum):
    A1 = ADS.P0
    A2 = ADS.P1
    A3 = ADS.P3
    A4 = ADS.P4
    