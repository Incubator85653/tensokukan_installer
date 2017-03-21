#!/usr/bin/python3

# You can cd to solution path and
# have some fun with the powershell!
# (gci -include *py -recurse | select-string .).Count

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

# This method has another copy in LibTskInstPython.
# It used to add search path for startup script.
def OsPathJoinSimulator(first, second):
    # This method is prevent a crash on some Ghost systems.
    # On these systems, os.path.join will fail.

    # It almost do the same thing just like os.path.join, but Windows platform specified.

    # first path must be "slash removed" path.
    # the second one can be a folder or a file with extension.
    result = r"{0}\{1}".format(first, second)
    return result
def AddSearchPaths():
    from os import path
    # pwd come from a Linux CLI command.
    pwd = os.getcwd()
    # define some library path and add them to system.path.
    pathImport = {}
    pathImport['pathTheInstallWizard'] = OsPathJoinSimulator(pwd, 'TskInstTheWizard')
    pathImport['pathTskInstModules'] = OsPathJoinSimulator(pathImport.get('pathTheInstallWizard'), 'TskInstWizardModules')
    pathImport['pathLibTskInstModules'] = OsPathJoinSimulator(pathImport.get('pathTheInstallWizard'), 'LibTskInstWizardModules')
    pathImport['pathLibTskInst'] = OsPathJoinSimulator(pwd, 'LibTskInst')

    sys.path.append(pathImport.get('pathTheInstallWizard'))
    sys.path.append(pathImport.get('pathTskInstModules'))
    sys.path.append(pathImport.get('pathLibTskInstModules'))
    sys.path.append(pathImport.get('pathLibTskInst'))

    #for p in sys.path:
    #    print(p)
    return

# Add search path and start installer disk I/O.
AddSearchPaths()



# GUI Bootstrap
import LibTskInstBootstrap as LibBoot
LibBoot.Wrapper()

# Start to initalize wizard
import TskInstTheWizard as TheWizard
TheWizard.Wrapper()