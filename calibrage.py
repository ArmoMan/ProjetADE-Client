# exemple 
from calibrer.calibrer_ph import CalibrerPh
from controlleurs.composants.adc.ads1115_controleur import ADS1115Controleur
from controlleurs.composants.adc.pin_analogique import PinAnalogique

#Cette page permet d’effectuer les calibrages avant de lancer le programme.

################################################################
############### exemple pour calibrer le ph ####################
################################################################
acide = 4.01 # valeur de votre ph
basique = 6.86 # valeur de votre ph
adc = ADS1115Controleur() #le controleur du ADC
pinPh =  PinAnalogique.A1 # pin dont votre ph capteur est branché (sur le ADC)
calibrage = CalibrerPh(adc, pinPh, 10, acide, basique) # initier class calibrage

#calibrage.commencer() # commencer à calibrer

#calibrage.tester_marge(-0.1713915470494417)
calibrage.tester_marge(-0.1716754385964914) # lire une mesure avec déja la marge
################################################################
################################################################
################################################################
