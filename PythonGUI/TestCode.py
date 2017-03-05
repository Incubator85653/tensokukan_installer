# Load all resource to memory

# PyInstaller
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
# System
import yaml
import sys
import os
# Shortcuts
import winshell
import win32com

# pwd come from a Linux CLI command.
pwd = os.getcwd()
# define some library path and add them to system.path.
pathImport = {}
pathImport['pathTheInstallWizard'] = r'{0}\TskInstTheWizard'.format(pwd)
pathImport['pathTskInstModules'] = r'{0}\TskInstWizardModules'.format(pathImport.get('pathTheInstallWizard'))
pathImport['pathLibTskInstModules'] = r'{0}\LibTskInstWizardModules'.format(pathImport.get('pathTheInstallWizard'))
pathImport['pathLibTskInst'] = r'{0}\LibTskInst'.format(pwd)
pathImport['pathResource'] = r'{0}\Bin'.format(pathImport.get('pathResource'))

sys.path.append(pathImport.get('pathTheInstallWizard'))
sys.path.append(pathImport.get('pathTskInstModules'))
sys.path.append(pathImport.get('pathLibTskInstModules'))
sys.path.append(pathImport.get('pathLibTskInst'))

#######################################################