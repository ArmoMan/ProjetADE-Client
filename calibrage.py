# exemple 
from calibrer.calibrer_ph import CalibrerPh
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique

# exemple pour calibrer le ph
adc = ADS1115Controleur()
acide = 4.01
basique = 6.86
calibrage = CalibrerPh(adc, PinAnalogique.A1, 10, acide, basique)
#calibrage.commencer()
#calibrage.tester_marge(-0.1713915470494417)
calibrage.tester_marge(-0.1716754385964914)