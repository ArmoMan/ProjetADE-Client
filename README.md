# ProjetADE-Raspberry
## Contenu
* [Installation et mise en place](#installation-de-python-et-pip)

---
| warning: Attention                              |
|:-----------------------------------------------:|
| La section suivante concerne le Raspberry Pi    |
---

## Installation de python et pip

**Vérifiez** que Python et pip sont bien installés.

```
python3 --version
```
et
```
pip3 --version
```

## Autorisations

### Activer la communication I2C sur l'appareil

Dans le **Terminal** entrez la [commande](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/) suivante

```
sudo raspi-config
```

Visitez **"Interfacing Options"**, choisissez **I2C** et **activez** l'option

## Installation des bibliothèques pour Raspberry Pi 4 Model B

### Lecture de signale analogique avec ADS1115 (Convertisseur Analogique-Numérique)

**Installez** la bibliothèque nécessaire avec la commande suivante :
```
sudo pip3 install adafruit-circuitpython-ads1x15
```

Si votre Raspberry Pi **ne permet pas** une installation globale de cette bibliothèque, utilisez l'option `--break-system-packages` pour **forcer l'installation**:
```
sudo pip3 install --break-system-packages adafruit-circuitpython-ads1x15
```

### Pour l'interface graphique il faut PyQt6

**Installez [PyQt6](https://pypi.org/project/PyQt6/)** avec la [commande](https://forums.raspberrypi.com/viewtopic.php?t=369140) suivante :
```
sudo apt install python3-pyqt6
```
ou
```
pip3 install PyQt6
```

### Installation du package w1thermsensor

Pour le capteur DS18B20, il faut faire des installations et ajustements

#### **Vous avez deux options pour installer la bibliothèque :**

```
pip install w1thermsensor --break-system-packages
```

ou  

```
sudo apt-get install python3-w1thermsensor
```

#### **Ensuite, il faut configurer le raspberry pi:**

1. **Ouvrir le fichier de configuration**  
   Dans un terminal, exécutez :
   ```
   sudo nano /boot/firmware/config.txt
   ```

2. **Activer le capteur 1-Wire**  
   Recherchez la ligne suivante :
   ```
   #dtoverlay=w1-gpio
   ```

   Supprimez le `#` au début pour activer l'option :
   ```
   dtoverlay=w1-gpio
   ```

3. **Redémarrer le système**  
   Une fois la modification enregistrée, redémarrez votre Raspberry Pi :
   ```
   sudo reboot
   ```

> [!CAUTION]
> Le capteur doit être branché sur le pin. C'est obligatoire, sinon visitez [w1thermsensor](https://github.com/timofurrer/w1thermsensor) pour la configuration.