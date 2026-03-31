#!/bin/bash
 
# --- A CONFIGURER ---
PYTHON_SCRIPT="Impression.py"
BASH_SCRIPT="deljdb.sh"
DEST_DIR="/home/pi"
CRON_USER="pi"
# --------------------
 
echo "=== Deploiement Imprimante ==="
 
USB_DIR=$(pwd)
 

cp "$USB_DIR/$PYTHON_SCRIPT" "$DEST_DIR/" || { echo "Erreur : impossible de copier $PYTHON_SCRIPT"; exit 1; }
cp "$USB_DIR/$BASH_SCRIPT"   "$DEST_DIR/" || { echo "Erreur : impossible de copier $BASH_SCRIPT"; exit 1; }
 

echo ""
echo "Selectionner le baudrate :"
echo "(1) 1200 bauds"
echo "(2) 2400 bauds"
echo "(3) 4800 bauds"
echo "(4) 9600 bauds"
echo "(5) 19200 bauds"
 
debitSymbole=""
 
while true; do
    read -p "Choix [1-5] : " debitSymbole
    if [[ "$debitSymbole" =~ ^[1-5]$ ]]; then
        break
    else
        echo "Choix invalide, reessayer."
    fi
done
 
if [ $debitSymbole = 1 ]; then
    debitSymbole=1200
elif [ $debitSymbole = 2 ]; then
    debitSymbole=2400
elif [ $debitSymbole = 3 ]; then
    debitSymbole=4800
elif [ $debitSymbole = 4 ]; then
    debitSymbole=9600
elif [ $debitSymbole = 5 ]; then
    debitSymbole=19200
fi
 
echo "Bauds selectionne : $debitSymbole bauds"
 

sed -i "s/baudrate=[0-9]*/baudrate=$debitSymbole/" "$DEST_DIR/$PYTHON_SCRIPT"
echo "Debit symbole mis a jour dans $PYTHON_SCRIPT"
 

chmod +x "$DEST_DIR/$BASH_SCRIPT" "$DEST_DIR/$PYTHON_SCRIPT"
chmod 777 "$DEST_DIR/$BASH_SCRIPT" "$DEST_DIR/$PYTHON_SCRIPT"
usermod -a -G dialout pi
 
if [ -d "/home/pi/Bureau" ]; then
    BUREAU="/home/pi/Bureau"
else
    BUREAU="/home/pi/Desktop"
fi
 

mkdir -p "$BUREAU/Journal"
chmod 777 "$BUREAU/Journal"
echo "Repertoire $BUREAU/Journal cree (777)"
 

echo "0 0 * * * $DEST_DIR/$BASH_SCRIPT" | crontab -u "$CRON_USER" -
echo "Tache Cron ajoutee"
 


AUTOSTART="/etc/xdg/lxsession/LXDE-pi/autostart"
lineprogramme="@lxterminal --command python3 $DEST_DIR/$PYTHON_SCRIPT"



if grep -qxF "$lineprogramme" "$AUTOSTART"; then
    echo "autostart deja config"
	elif grep -qxF "@lxterminal --command python3 Impression.py" "$AUTOSTART"; then
    echo "autostart deja config"
    else
    echo "$lineprogramme" >> $AUTOSTART
fi
 



echo ""
read -p "Voulez-vous mettre a l'heure le Raspberry Pi ? (o/n) : " reponseHeure
if [ "$reponseHeure" = "o" ]; then
    read -p "Entrez la date et l'heure (format AAAA-MM-JJ HH:MM) : " dateHeure
    date -s "$dateHeure"
    echo "Date et heure mises a jour."
fi
 
echo ""
read -p "Installation termine. Redemarrer maintenant ? (o/n) : " reponse
if [ "$reponse" = "o" ]; then
    echo "Redemarrage..."
    sudo reboot
else
    echo "Pensez a redemarrer le Pi pour appliquer les changements."
fi
