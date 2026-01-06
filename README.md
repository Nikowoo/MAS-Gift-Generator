# MAS Gift Generator

A simple desktop tool to generate `.gift` files for the *[Monika After Story](https://www.monikaafterstory.com/)* mod.  
This GUI helps you quickly create all the gifts you could ever need, sorted neatly by category or all together, with options to control overwriting and file placement.

---
 
![Screenshot of MAS Gift Generator GUI](https://raw.githubusercontent.com/Nikowoo/MAS-Gift-Generator/2a551d1d3beaaff190a70a2fa6f2b574607c70c4/giftdemo.gif)  

---

## Prerequisites

- Windows PC  
- Python 3.7 or higher (if running from source)  

---


## Building the executable

To build your own executable use PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=MAS.ico --add-data "MAS.ico;." gift.py
