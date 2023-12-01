# QR Code Maker

Ce script Python vous permet de créer des codes QR personnalisés en spécifiant divers paramètres tels que la taille des pixels, les couleurs, la version du code QR, et même l'ajout facultatif d'une image.

## Installation

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante :

```bash
python -m pip install qrcode[pil] colorama
```

- qrcode[pil] : Module pour la génération de codes QR.
- colorama : Module pour la coloration du texte dans la console.

## Comment lancer le script

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/VotreNom/QR_Code_Maker.git
   ```
2. Déplacez-vous dans le dossier du script :
   ```bash
   cd QR_Code_Maker
   ```
3. Lancez le script :
   ```bash
   python qr.py
   ```

## Utilisation du script

Le script vous guidera à travers la création de votre code QR en posant différentes questions sur les paramètres que vous souhaitez personnaliser. Vous pouvez choisir de spécifier la taille des pixels, les couleurs, la version du code QR, et même d'ajouter une image.

## Résultats

Les résultats de vos codes QR seront enregistrés dans le dossier `QR_Code_image` à la racine du projet. Vous pourrez y trouver les images générées avec les noms que vous avez fournis lors de l'exécution du script.

Voici un exemple de code QR généré :

![QR Code Example](QR_Code_image/qr_github.png)

N'hésitez pas à explorer et personnaliser davantage le script en modifiant les paramètres ou en ajoutant de nouvelles fonctionnalités selon vos besoins.
