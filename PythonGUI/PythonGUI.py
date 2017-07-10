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
# Process
import subprocess
# Shortcuts
import winshell
import win32com
# Water wells studio code library
from LibPython import Environment


# This method has another copy in LibPython.
# It used to add search path for startup script.

def AddSearchPaths2():
    Environment.Path.merge_path_with_work_dir
def AddSearchPaths():
    from os import path
    # pwd come from a Linux CLI command.
    pwd = os.getcwd()
    # define some library path and add them to system.path.
    pathImport = {}
    pathImport['pathTheInstallWizard'] = OsPathJoinSimulator(pwd, 'TskInstTheWizard')
    pathImport['pathTskInstModules'] = OsPathJoinSimulator(pathImport.get('pathTheInstallWizard'), 'TskInstWizardModules')
    pathImport['pathLibModules'] = OsPathJoinSimulator(pathImport.get('pathTheInstallWizard'), 'LibWizardModules')
    pathImport['pathLib'] = OsPathJoinSimulator(pwd, 'Lib')

    sys.path.append(pathImport.get('pathTheInstallWizard'))
    sys.path.append(pathImport.get('pathTskInstModules'))
    sys.path.append(pathImport.get('pathLibModules'))
    sys.path.append(pathImport.get('pathLib'))

    #for p in sys.path:
    #    print(p)
    return

# Add search path and start installer disk I/O.
AddSearchPaths()



# GUI Bootstrap
import LibBootstrap as LibBoot
LibBoot.Wrapper()

# Start to initalize wizard
import TskInstTheWizard as TheWizard
TheWizard.Wrapper()