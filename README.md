# Tutoriel d'Installation — Script d'impression Raspberry

---

## Prérequis

Avant de commencer, vous devez être en possession des trois fichiers suivants sur une clé USB :

- `Impression.py` — le programme principal d'impression
- `deljdb.sh` — le script de suppression automatique des anciens journaux
- `deploiement.sh` — le script d'installation

 Vous pouvez télécharger les scripts nécessaires ici :
 **https://github.com/Ahm2d376/Programme-impression-raspberry**

Dézipper et déplacer les fichiers dans votre clé usb.

>**Les trois fichiers doivent tous se trouver directement à la racine de la clé USB, et non dans un sous-dossier de la clé.**

---

## Débit symbole par poste

Avant de commencer l'installation, repérez le débit symbole correspondant au poste dans le tableau ci-dessous :

| Poste | Vitesse de transmission (b/s) |
|---|---|
| BUGELLERIE | 2400 |
| CHATELLERAULT | 1200 |
| CHAUMONT | — |
| CHAUVIGNY | 9600 |
| CIVRAY | 9600 |
| COLOMBIERS | 1200 / SEVEN / ODD |
| ISLE JOURDAIN | 9600 |
| JAUNAY CLAN | - |
| LENCLOITRE | 9600 |
| LOUDUN | 2400 |
| MELLE | 9600 |
| MEUNIERS | 9600 |
| MONTMORILLON | 2400 |
| NIORT | 2400 |
| ORANGERIE | 9600 |
| PAPAULT | 1200 / SEVEN |
| PARTHENAY | 9600 |
| PLEUMARTIN | 9600 |
| POINTE A MITEAU | 2400 |
| POITIERS SUD | 1200 |
| ST FLORENT | 9600 |
| ST MAIXENT | 9600 |
| THOUARS | 9600 |

---

## Étapes d'installation

### 1. Brancher la clé USB

Branchez la clé USB sur le Raspberry Pi puis ouvrez l'explorateur de fichiers. Si un ancien programme d'impression est ouvert, fermez le.

### 2. Naviguer vers la clé USB

Dans l'explorateur de fichiers, naviguez vers le répertoire `/media/pi`. Celui-ci doit contenir un répertoire portant le nom de votre clé USB.

<img width="715" height="517" alt="image" src="https://github.com/user-attachments/assets/4d0c125e-0c0a-4366-bd3f-52f6289f4fc2" />



### 3. Ouvrir un terminal dans le répertoire de la clé

Faites un **clic droit** sur le répertoire de la clé USB et sélectionnez **"Ouvrir dans un terminal"**.

<img width="711" height="512" alt="image" src="https://github.com/user-attachments/assets/d914e969-4d04-439e-be12-fbe82e3c17d0" />



### 4. Exécuter le script d'installation

Dans le terminal qui vient de s'ouvrir, saisissez la commande suivante :

```bash
sudo bash deploiement_imprimante.sh
```

### 5. Sélectionner le débit symbole

Le script vous demande de sélectionner le baudrate adapté à votre poste :

```
=== Deploiement Raspberry Pi ===

Sélectionner le baudrate :
(1) 1200 bauds
(2) 2400 bauds
(3) 4800 bauds
(4) 9600 bauds
(5) 19200 bauds
Choix [1-5] :
```

Saisissez le numéro correspondant et appuyez sur **Entrée**.



### 6. Déroulement automatique de l'installation

Une fois le baudrate sélectionné, le script effectue automatiquement les opérations suivantes :

- Copie de `Impression.py` et `deljdb.sh` vers `/home/pi/`
- Mise à jour du baudrate dans `Impression.py`
- Création du répertoire `Journal` sur le bureau
- Ajout de la tâche cron pour la suppression automatique des anciens journaux
- Configuration du démarrage automatique du programme au boot

<img width="551" height="197" alt="image" src="https://github.com/user-attachments/assets/7141b65a-ec5f-4b26-98ff-0bd856cf4836" />



### 7. Mise à l'heure

Le script vous demande si vous souhaitez mettre à l'heure le Raspberry Pi. A faire si la raspberry n'est pas à l'heure pour que les fichiers journaux soient bien datés.

```
Voulez-vous mettre a l'heure le Raspberry Pi ? (o/n) :
```

Si vous répondez `o`, saisissez la date et l'heure au format `AAAA-MM-JJ HH:MM` puis appuyez sur **Entrée**.

### 8. Redémarrage

Le script vous propose ensuite de redémarrer la Raspberry Pi :

```
Installation termine. Redemarrer maintenant ? (o/n) :
```

Répondez `o` pour redémarrer immédiatement.

Au redémarrage, un terminal doit s'ouvrir automatiquement et lance `Impression.py`.


---

## Vérifications post-installation



### Vérifier la tâche cron

Une tâche cron a été installée pour supprimer automatiquement les fichiers journaux vieux de plus de 30 jours. Pour vérifier qu'elle est bien en place, ouvrez un terminal et tapez :

```bash
crontab -l
```

La ligne suivante doit apparaître :

```
0 0 * * * /home/pi/deljdb.sh
```

<img width="364" height="25" alt="image" src="https://github.com/user-attachments/assets/8d398e39-5224-4bad-9068-4293fbfcc4f9" />



### Vérifier le répertoire Journal

Le répertoire `Journal` doit être présent sur le bureau. C'est dans ce dossier que seront enregistrés les fichiers journaux au format `JDB_AAAA-MM-JJ.txt`. Vérifiez qu'un fichier avec la date du jour a bien été crée.

---

## Personnalisation et dépannage

Si vous rencontrez des erreurs ou souhaitez adapter les scripts à votre environnement, voici les paramètres modifiables dans chaque fichier.

---

### deploiement_imprimante.sh

En haut du script se trouvent les variables de configuration. Ce sont les seules lignes à modifier :

```bash
# --- À CONFIGURER ---
PYTHON_SCRIPT="Impression.py"   # Nom du programme Python à installer
BASH_SCRIPT="deljdb.sh"         # Nom du script de suppression des anciens journaux
DEST_DIR="/home/pi"             # Répertoire de destination sur la raspberry
CRON_USER="pi"                  # Utilisateur cible pour la crontab
# --------------------
```

| Variable | À modifier si... |
|---|---|
| `PYTHON_SCRIPT` | Vous renommez le fichier `Impression.py` |
| `BASH_SCRIPT` | Vous renommez le fichier `deljdb.sh` |
| `DEST_DIR` | Vous souhaitez installer les scripts dans un autre répertoire |
| `CRON_USER` | L'utilisateur du Raspberry Pi n'est pas `pi` |

---

### Impression.py

Les paramètres modifiables se trouvent aussi en haut du fichier :



| Paramètre             | À modifier si...                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| `REPERTOIRE_LOGS`     | Le bureau ne s'appelle pas `Desktop` ou vous voulez stocker les journaux ailleurs                     |
| `port='/dev/ttyUSB0'` | Le port série de votre appareil est différent (ex: `/dev/ttyUSB1`, `/dev/ttyS0`)                      |
|                       |                                                                                                       |
| `baudrate=9600`       | Normalement mis à jour automatiquement par le script de déploiement, mais modifiable manuellement ici |
| `parity`              | Si vous voulez changer le mode de parité du port série                                                |
| `stopbits`              | Si vous voulez changer le nombre de bits de stop                                                      |
| `bytesize`              | Si vous voulez changer le nombre de bits d'un byte                                                    |




---

### deljdb.sh

Si vous avez modifié le chemin du répertoire `Journal` dans `Impression.py`, il faut répercuter ce changement dans `deljdb.sh`. Ouvrez le fichier et modifiez la ligne correspondant au chemin du répertoire.

---

