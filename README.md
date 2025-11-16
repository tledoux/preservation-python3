# Preservation Python3

[![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/tledoux/preservation-python3/blob/main/README.md) [![fr](https://img.shields.io/badge/README-fr-green.svg)](https://github.com/tledoux/preservation-python3/blob/main/README.fr.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/tledoux/preservation-python3.svg)](https://github.com/tledoux/preservation-python3/issues "Open issues on GitHub")
![](https://img.shields.io/github/release/tledoux/preservation-python3.svg)
[![GitHub Downloads (latest release)](https://img.shields.io/github/downloads/tledoux/preservation-python3/latest/total)](https://github.com/tledoux/preservation-python3/releases/latest "Latest release downloads")
[![Play on Chrome](https://img.shields.io/badge/Play_On-Chrome-blue?color=blue)](https://tledoux.github.io/preservation-python3/index.html)


_Preservation Python3 is a snake-type game where the player controls a continually shrinking python (though you might not always notice!), a metaphor for obsolescence and data loss. The python must ingest, pun intended, content and preservation information while avoiding elements that accelerate data loss. If the python survives a certain length of time, the required elements will change into preservation actions needed to maintain continued access._

_The game is meant to introduce the elements of an OAIS Archival Information Package to beginners in a fun and interactive way, as well as to present digital preservation as a continuous activity. The fast-paced nature of a snake game also encourages the player to make decisions on which elements they prefer to prioritize._

_The game is directly derived from [Preservation Python](https://github.com/archivistnathan/preservation-python)._

## Ingest Preservation Information and avoid preservation failure!

### Capture your Data Object and Accompanying PDIs

- Data Object

- Provenance

- Fixity

- Context

- Reference

- Access Rights

- Representation Information

- Packaging Information


### Avoid elements that could lead to data loss

- Malware

- Obsolescence

- Accidental Deletion

- Hardware Malfunction

- Software Bugs

- Legal Issues

- Lack of Organizational Commitment


### Keep it going and ensure continued accessibility over time!

- Media Refreshment

- Technology Watch

- Format Migration

- Emulation

- Backups

_Each PDI or preservation action increases your score. Obsolescence and data loss will halve your current score._

__The game ends when your score goes below 1 or when you hit the walls or yourself.__

## Installations

### Execution from the source

Download the project either by cloning it (`git clone`) or by getting the full ZIP of it.

Make sure you have Python3 installed.

Optionally but highly recommended, activate a [virtual environment](https://docs.python.org/3/library/venv.html) with:
```bash
python -m venv venv

venv\Scripts\activate (Windows)
source venv/bin/activate (Linux)
```

Add the dependencies (e.g. pygame) using `pip`.
```bash
pip install -r requirements.txt
```

Navigate to the folder containing `main.py` and run with Python3:
```bash
python main.py
```


Enjoy!

### Generation of an executable (tested in Windows)

In order to generate a `preservation-python3.exe`, you need to:

- add `pyinstaller` using `pip`:
```bash
pip install pyinstaller
```

- run
```bash
pyinstaller preservation.spec
```

_The executable will be generated in the `dist` directory._

## Contributing

If you wish to contribute, read the file [CONTRIBUTING.md](CONTRIBUTING.md) to know how.

## Credits

The code is directly derived from the [preservation-python code](https://github.com/archivistnathan/preservation-python) by Jonathan Isip.

The game images come from [Flaticon](https://www.flaticon.com/free-icons).

The snake image come from [OpenGameArt](https://opengameart.org/content/snake-sprite-sheet).
