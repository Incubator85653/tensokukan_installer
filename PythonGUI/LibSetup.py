from LibPython import InputOutput
from LibPython import Environment
from LibInstallProfile import Methods as wizardCfg
from LibInstallProfile import Profile

class Methods:
    class CopyFiles:
        def UnpackArchives():
            import os
            from LibPython import Environment

            archivesPath = wizardCfg.Installer.Archive.Source()
            archivesCollection = wizardCfg.Installer.Archive.Collection()

            installPath = wizardCfg.Basic.InstallPath()

            for archiveName in archivesCollection:
                archiveFullPath = Environment.Path.Complement.merge(archivesPath, archiveName)
                InputOutput.Zip.DoUnpack(archiveFullPath, installPath)

            return
        def UnpackSWRSAddr():
            from os import path
            archiveName = wizardCfg.UserData.SWRSAddr7z()
            installPath = wizardCfg.Basic.InstallPath()

            # If archiveName is False,
            # that means user selected "Skip" or this version not need to unpack SWRSAddr.

            # If archiveName is not False(added an archive name),
            # Unpack that archive to install folder.

            if bool(archiveName) != False:
                InputOutput.Zip.DoUnpack(archiveName, installPath)
            return

        def DoCopy():
            Methods.CopyFiles.UnpackArchives()
            Methods.CopyFiles.UnpackSWRSAddr()
            return
    class EditConfigs:
        # mbcs means windows system default ANSI encode, in notepad.exe .
        # The situation is some of Tensokukan config files support only ANSI format.
        # They need a convert from Template(UTF-8) to Target(Local ANSI).
        def DoEdit_FillArguments():
            editorDict = wizardCfg.Installer.Optional.Templates()

            for fileName in editorDict:
                perFileDict = editorDict[fileName]
                InputOutput.Templates.DoModify(perFileDict)
            return
    class Shortcuts:
        def ShortcutRules(Action, FileName, Args):
            import winshell
            import os
            from LibPython import Environment

            # These codes used python sequential execution characteristics.

            # Def a switch for base library, affect create shortcut or not after fill information.
            # Close it if create shortcut manually.
            createSwitch = True

            # Def env(desktop, startmenu, etc) and lnk name.
            environmentPath = None
            lnkName = None

            # Get user settings.
            manageDesktop = wizardCfg.Unattended.ManageDesktopShortcut()
            manageStartMenu = wizardCfg.Unattended.ManageStartMenuShortcut()

            # Def shortcut information
            lnkFileLocation = None
            targetFullPath = None
            targetWorkingDir = None

            if Action == 'TskMainLnk':
                lnkName = wizardCfg.Basic.MainShortcut()
                targetFullPath = wizardCfg.Installer.Optional.ProgramStructure.Tsk.Bin.TskMainExe()
                targetWorkingDir = wizardCfg.Basic.InstallPath()

                if manageDesktop:
                    environmentPath = winshell.desktop()
                    
                    lnkFileLocation = Environment.Path.Complement.merge(environmentPath, lnkName)

                    createSwitch = False
                    InputOutput.Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)
                if manageStartMenu:
                    environmentPath = winshell.programs()

                    tskSmGroupName = wizardCfg.Basic.StartMenuGroup()
                    tskSmGroupPath = Environment.Path.Complement.merge(environmentPath, tskSmGroupName)

                    lnkFileLocation = Environment.Path.Complement.merge(tskSmGroupPath, lnkName)

                    # Create shortcut menu for base library.
                    if not os.path.exists(tskSmGroupPath):
                        os.makedirs(tskSmGroupPath)

                    createSwitch = False
                    InputOutput.Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)

            if Action == 'UploadNow':

                createSwitch = False
                doNothing = None#TODO

            if Action == 'DoNothing':

                createSwitch = False

            if createSwitch:
                InputOutput.Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)
            return
        def DoCreate_FillArguments():
            # Get batch shortcut config
            shortcutsProfile = Profile.Methods.Structure.Shortcuts.Config()

            # Get per shortcut config group dictionary.
            for perLnkDict in shortcutsProfile:

                # Get the group name, it can't be directly read.
                for perLnkDictName in perLnkDict:

                    # Use group name to receive final replace profile dictionary.
                    createShortcutDict = perLnkDict[perLnkDictName]

                    Action = createShortcutDict['Action']
                    FileName = createShortcutDict['FileName']
                    Args = createShortcutDict['Args']

                    Methods.Shortcuts.ShortcutRules(Action, FileName, Args)
            return

def Wrapper_NewInstall():
    Methods.CopyFiles.DoCopy()
    Methods.EditConfigs.DoEdit_FillArguments()
    Methods.Shortcuts.DoCreate_FillArguments()
    return