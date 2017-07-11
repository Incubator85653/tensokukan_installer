#!/usr/bin/python3

# You can cd to solution path and
# have some fun with the powershell!
# (gci -include *py -recurse | select-string .).Count

# Install references:
# pip install pyyaml winshell pypiwin32

# I have to remember, put anything path in "os.path.normpath".

# Debug Codes

# Load all resource to memory

# PyInstaller

# Tkinter
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
# System
import yaml
import sys
import os
import traceback
# Process
import subprocess
# Shortcuts
import winshell
import win32com
# Search path
import sys

# Water wells studio code library
sys.path.append(r"..\LibWaterWellsStudio")
from LibPython import Environment as Env
# Installer code files
sys.path.append("TskInstTheWizard")
sys.path.append(r"TskInstTheWizard\TskInstWizardModules")
sys.path.append(r"TskInstTheWizard\LibTskInstWizardModules")

# GUI Bootstrap
import LibBootstrap as LibBoot
LibBoot.Wrapper()

# Start to initalize wizard
import TskInstTheWizard as TheWizard
TheWizard.Wrapper()