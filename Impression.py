#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial              
from datetime import datetime  
import os                  
import shutil              
import glob                

#Config

REPERTOIRE_LOGS = "/home/pi/Desktop/Journal"


if not os.path.exists(REPERTOIRE_LOGS):
    os.makedirs(REPERTOIRE_LOGS)


port_serie = serial.Serial(
    port='/dev/ttyUSB0',              
    baudrate=9600,                     
    parity=serial.PARITY_NONE,         
    stopbits=serial.STOPBITS_ONE,      
    bytesize=serial.EIGHTBITS,         
    timeout=0                     
)



def obtenir_nom_fichier_log():
    date_str = datetime.now().strftime("%Y-%m-%d")
    # TEST :
    #date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    return f"{REPERTOIRE_LOGS}/JDB_{date_str}.txt"

try:
    
    date_actuelle = datetime.now().date()
    # TEST :
    #date_actuelle = datetime.now().strftime("%Y-%m-%d_%H-%M")
    fichier = open(obtenir_nom_fichier_log(), "a", encoding='utf-8')
    
  
    

    while 1:
        # date actuelle
        nouvelle_date = datetime.now().date()
        # TEST :
        #nouvelle_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
        
    
        if nouvelle_date != date_actuelle:
            # ferme le fichier de la veille
            fichier.flush()
            
            
            date_actuelle = nouvelle_date
            
            
            fichier = open(obtenir_nom_fichier_log(), "a", encoding='utf-8')
            
            
            
        
       
        donnees = port_serie.readline()
        
        # parcourt chaque octet reçu depuis le port série
        for valeur_octet in donnees:
            
            if valeur_octet == 13:  # 13 = ASCII entrée
                # affiche un saut de ligne
                print('')
                fichier.write('\n')
                fichier.flush()
            else:
                print(chr(valeur_octet), end='')
                fichier.write(chr(valeur_octet))
                fichier.flush()


                
except KeyboardInterrupt:
    print(' ', end='')
        
except Exception as e:
    print(e)
