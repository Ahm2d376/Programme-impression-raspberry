#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import serial              
from datetime import datetime  
import os                  
import time
 
#Config
 
REPERTOIRE_LOGS = "/home/pi/Desktop/Journal"
 
 
if not os.path.exists(REPERTOIRE_LOGS):
    os.makedirs(REPERTOIRE_LOGS)
 
 
def connecter_port_serie():
    port_serie = None
    while port_serie is None:
        try:
            port_serie = serial.Serial(
                port='/dev/ttyUSB0',              
                baudrate=9600,                     
                parity=serial.PARITY_NONE,         
                stopbits=serial.STOPBITS_ONE,      
                bytesize=serial.EIGHTBITS,         
                timeout=0                     
            )
        except serial.SerialException:
            print("Port serie non disponible")
            time.sleep(10)
    return port_serie
 
 
def obtenir_nom_fichier_log():
    date_str = datetime.now().strftime("%Y-%m-%d")
    return "{}/JDB_{}.txt".format(REPERTOIRE_LOGS, date_str)
 
try:
    port_serie = connecter_port_serie()
    date_actuelle = datetime.now().date()
    fichier = open(obtenir_nom_fichier_log(), "a", encoding='utf-8')
 
    while 1:
        nouvelle_date = datetime.now().date()
        
        if nouvelle_date != date_actuelle:
            fichier.flush()
            date_actuelle = nouvelle_date
            fichier = open(obtenir_nom_fichier_log(), "a", encoding='utf-8')
        
        try:
            donnees = port_serie.readline()
            
            for valeur_octet in donnees:
                if valeur_octet == 13:
                    print('')
                    fichier.write('\n')
                    fichier.flush()
                else:
                    print(chr(valeur_octet), end='')
                    fichier.write(chr(valeur_octet))
                    fichier.flush()
 
        except serial.SerialException:
            print("Port serie non disponible")
            port_serie.close()
            port_serie = connecter_port_serie()
 
except KeyboardInterrupt:
    print(' ', end='')
        
except Exception as e:
    print(e)
