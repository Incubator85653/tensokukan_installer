from LibOperate import Zip
from LibOperate import Shortcut
from LibPython import Environment as Env
from LibOperate import WaterWellsYaml as wwYaml
from LibInstallProfile import DecodedProfile as wizardCfg

class Methods:
    class CopyFiles:
        def UnpackArchives():
            archivesPath = wizardCfg.Methods.Installer.Archive.Source()
            archivesCollection = wizardCfg.Methods.Installer.Archive.Collection()

            installPath = wizardCfg.Methods.Basic.InstallPath()

            for archiveName in archivesCollection:
                archiveFullPath = Env.Path.Complement.merge_system(archivesPath, archiveName)
                Zip.wrapper_do_unpack(archiveFullPath, installPath)

        def UnpackSWRSAddr():
            archiveName = wizardCfg.Methods.UserData.SWRSAddr7z()
            installPath = wizardCfg.Methods.Basic.InstallPath()

            # If archiveName is False,
            # that means user selected "Skip" or this version not need to unpack SWRSAddr.

            # If archiveName is not False(added an archive name),
            # Unpack that archive to install folder.
            if bool(archiveName) != False:
                Zip.wrapper_do_unpack(archiveName, installPath)

        def wrapper_do_copy():
            Methods.CopyFiles.UnpackArchives()
            Methods.CopyFiles.UnpackSWRSAddr()
            return
    class EditConfigs:
        # mbcs means windows system default ANSI encode, in notepad.exe .
        # The situation is some of Tensokukan config files support only ANSI format.
        # They need a convert from Template(UTF-8) to Target(Local ANSI).
        def update_batching_editor_config():
            doNothing = None
            #TODO
        def wrapper_do_edit():
            doNothing = None
            #TODO
    class Shortcuts:
        def ShortcutRules(Action, FileName, Args):
            import winshell
            import os

            # These codes used python sequential execution characteristics.

            # Def a switch for base library, affect create shortcut or not after fill information.
            # Close it if create shortcut manually.
            createSwitch = True

            # Def env(desktop, startmenu, etc) and lnk name.
            environmentPath = None
            lnkName = None

            # Get user settings.
            manageDesktop = wizardCfg.Methods.Unattended.ManageDesktopShortcut()
            manageStartMenu = wizardCfg.Methods.Unattended.ManageStartMenuShortcut()

            # Def shortcut information
            lnkFileLocation = None
            targetFullPath = None
            targetWorkingDir = None

            if Action == 'TskMainLnk':
                lnkName = wizardCfg.Methods.Basic.MainShortcut()
                targetFullPath = wizardCfg.Methods.Installer.Optional.ProgramStructure.Tsk.Bin.TskMainExe()
                targetWorkingDir = wizardCfg.Methods.Basic.InstallPath()

                if manageDesktop:
                    environmentPath = winshell.desktop()
                    
                    lnkFileLocation = Env.Path.Complement.merge_system(environmentPath, lnkName)

                    createSwitch = False
                    Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)
                if manageStartMenu:
                    environmentPath = winshell.programs()

                    tskSmGroupName = wizardCfg.Methods.Basic.StartMenuGroup()
                    tskSmGroupPath = Env.Path.Complement.merge_system(environmentPath, tskSmGroupName)

                    lnkFileLocation = Env.Path.Complement.merge_system(tskSmGroupPath, lnkName)

                    # Create shortcut menu for base library.
                    if not os.path.exists(tskSmGroupPath):
                        os.makedirs(tskSmGroupPath)

                    createSwitch = False
                    Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)

            if Action == 'UploadNow':

                createSwitch = False
                doNothing = None#TODO

            if Action == 'DoNothing':

                createSwitch = False

            if createSwitch:
                Shortcut.CreateShortcut(lnkFileLocation, targetFullPath,targetWorkingDir)
            return
        def DoCreate_FillArguments():
            # Get batch shortcut config
            shortcutsProfile = wizardCfg.Methods.Optional.Structure.Shortcuts.Config()

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
        def wrapper_do_create():

            Methods.Shortcuts.DoCreate_FillArguments()

def Wrapper_NewInstall():
    """Start install and return success status.
    If all the operation were success, return True.
    Else, one of the operation was failed, return False."""
    all_install_success = False
    try:
        # Begin install.
        Methods.CopyFiles.wrapper_do_copy()
        Methods.EditConfigs.wrapper_do_edit()
        Methods.Shortcuts.wrapper_do_create()
        # Turn all install success var to True after all operation success.
        all_install_success = True
    except Exception as e:
        from LibPython import Process
        Process.handle_exception(e, False)

    return all_install_success