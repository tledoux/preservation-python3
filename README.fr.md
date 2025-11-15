# Préservation Python3

[![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/tledoux/preservation-python3/blob/main/README.md) [![fr](https://img.shields.io/badge/README-fr-green.svg)](https://github.com/tledoux/preservation-python3/blob/main/README.fr.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/tledoux/preservation-python3.svg)](https://github.com/tledoux/preservation-python3/issues "Open issues on GitHub")
![](https://img.shields.io/github/release/tledoux/preservation-python3.svg)
[![GitHub Downloads (latest release)](https://img.shields.io/github/downloads/tledoux/preservation-python3/latest/total)](https://github.com/tledoux/preservation-python3/releases/latest "Déchargements dernière version")
[![Jouer sur Chrome](https://img.shields.io/badge/Jouer_sur-Chrome-blue?color=blue)](https://tledoux.github.io/preservation-python3/index.html)

_Preservation Python3 est un jeu du type **snake** (serpent) où le joueur contrôle un python qui grandit sans arrêt (même si vous ne vous en apercevez pas toujours), une métaphore pour l'obsolescence et la perte de données. Le python doit ingérer de l'information de contenu et de préservation tout en évitant les éléments qui accélère la perte d'information. Si le python survit un certain temps, les éléments requis vont changer en des actions de préservation nécessaires pour maintenir un accès permanent._

_Ce jeu a pour but d'initier les débutants aux éléments d'un paquet d'information archivé (**AIP**) de l'OAIS de manière ludique et interactive, et de présenter la préservation numérique comme une activité continue. Le rythme rapide d'un jeu de serpent incite également le joueur à choisir les éléments qu'il souhaite prioriser._

_Ce jeu est directement dérivé de [Preservation Python](https://github.com/archivistnathan/preservation-python)._

## Ingérer l'Information de Préservation et éviter les risques associés !

### Saisir les Objets-Données et les éléments de l'Information de Pérennisation (PDI) associés

- Objet-Donnée

- Provenance

- Intégrité

- Contexte

- Référence

- Droits d'accès

- Information de Représentation

- Information d'Empaquetage


### Éviter les éléments susceptibles d'entraîner des pertes de données

- Virus informatique

- Obsolescence

- Suppression accidentelle

- Dysfonctionnement matériel

- Bugs logiciels

- Problèmes juridiques

- Manque d'engagement organisationnel


### Continuez ainsi et assurez un accès permanent au fil du temps !

- Rafraîchissement de support

- Veille technologique

- Migration de formats

- Émulation

- Sauvegardes

_Chaque PDI ou action de préservation augmente votre score. L'obsolescence ou la perte de données divise par deux votre score._

_Le jeu finit quand votre score descend sous la barre de 1 ou si vous heurtez les murs ou vous-même._

## Installations

### Exécution depuis le code source

Téléchargez le projet soit en le clonant (`git clone`), soit en obtenant le fichier ZIP complet.

Assurez-vous d'avoir Python3 installé.

Facultativement mais hautement recommandé, activez un [environnement virtuel](https://docs.python.org/3/library/venv.html) avec :
```bash
python -m venv venv

venv\Scripts\activate (Windows)
source venv/bin/activate (Linux)
```

Ajoutez les dépendances (i.e. pygame) en utilisant `pip`.
```bash
pip install -r requirements.txt
```

Naviguez vers le dossier contenant `main.py` et exécutez-le avec Python3 :
```bash
python main.py
```


Profitez !

### Génération d'un exécutable (testé sous Windows)

Pour générer `preservation-python3.exe`, vous devez :

- ajouter `pyinstaller` en utilisant `pip` :
```bash
pip install pyinstaller
```

- exécuter
```bash
pyinstaller preservation.spec
```

_L'exécutable sera généré dans le dossier `dist`._

## Contributions

Si vous souhaitez contribuer, lisez le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour savoir comment le faire.

## Crédits

Le code est directement dérivé du code de [preservation-python](https://github.com/archivistnathan/preservation-python) par Jonathan Isip.

Les images du jeu proviennent de [Flaticon](https://www.flaticon.com/free-icons).

Les images du serpent proviennent de [OpenGameArt](https://opengameart.org/content/snake-sprite-sheet).
