from enum import Enum
import adafruit_ads1x15.ads1115 as ADS 

class PinAnalogique(Enum):
    A0 = ADS.P0
    A1 = ADS.P1
    A2 = ADS.P2
    A3 = ADS.P3
    