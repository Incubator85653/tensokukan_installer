from LibOperate import Zip
from LibOperate import Shortcut
from LibPython import Environment as Env
from LibOperate import WaterWellsYaml as wwYaml
from LibInstallProfile import DecodedProfile as wizardCfg
from LibPython import Process
from LibPython import Console

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
            # that means user selected "Skip" or this version not need to
            # unpack SWRSAddr.

            # If archiveName is not False(added an archive name),
            # Unpack that archive to install folder.
            if bool(archiveName) != False:
                Zip.wrapper_do_unpack(archiveName, installPath)

        def wrapper_do_copy():
            Methods.CopyFiles.UnpackArchives()
            Methods.CopyFiles.UnpackSWRSAddr()

    class EditConfigs:
        # mbcs means windows system default ANSI encode, in notepad.exe .
        # The situation is some of Tensokukan config files support only ANSI
        # format.
        # They need a convert from Template(UTF-8) to Target(Local ANSI).
        def update_batching_editor_config():
            """Return edited editor config.
            This crazy method will tell you sometimes ugly access path is faster than nest loop."""
            # Sumeragi Shion - Gujjo bu
            # A tempoary variable to hold edited dictionary
            shion = wizardCfg.Config.BatchEditorYaml
            
            # File: Tsk_MainConfig
            try:
                inst_path = wizardCfg.Methods.Basic.InstallPath()
                # Fill installed path
                source = shion['Tsk_MainConfig']['Source'].format(inst_path)
                shion['Tsk_MainConfig']['Source'] = source
                target = shion['Tsk_MainConfig']['Target'].format(inst_path)
                shion['Tsk_MainConfig']['Target'] = target

                # Modify GameExePath
                shion['Tsk_MainConfig']['OptionArray'][0]['GameExePath']['Value'] = wizardCfg.Methods.Basic.GameExePath()
            
                # Modify TskNetExePath
                shion['Tsk_MainConfig']['OptionArray'][1]['TskNetExePath']['Value'] = wizardCfg.Methods.Optional.Structure.Program.TskNet.Bin.TskNetMainExe()
            except Exception as e:
                
                Process.handle_exception(e, False)
            
            # File: TskNet_Account
            try:
                inst_path = wizardCfg.Methods.Basic.InstallPath()
                # Fill installed path
                source = shion['TskNet_Account']['Source'].format(inst_path)
                shion['TskNet_Account']['Source'] = source
                target = shion['TskNet_Account']['Target'].format(inst_path)
                shion['TskNet_Account']['Target'] = target
            
                # Account and password condition
                if wizardCfg.Methods.Unattended.ManageId():
                    # Modify TencoAccount
                    shion['TskNet_Account']['OptionArray'][0]['TencoAccount']['Value'] = wizardCfg.Methods.UserData.TencoAccount()
                    # Modify TencoPassword
                    shion['TskNet_Account']['OptionArray'][1]['TencoPassword']['Value'] = wizardCfg.Methods.UserData.TencoPassword()
            except Exception as e:
                
                Process.handle_exception(e, False)

            return shion
        def get_saved_editor_config_path():
            try:
                inst_path = wizardCfg.Methods.Basic.InstallPath()
                edited_yaml = Methods.EditConfigs.update_batching_editor_config()
                saved_path = Env.Path.Complement.merge_system(inst_path, "Templates\BatchEditor.yaml")
            
                wwYaml.write_yaml_to_disk(edited_yaml, saved_path)
            except Exception as e:
                
                Process.handle_exception(e, False)

            return saved_path
        def run_batch_editor():
            inst_path = wizardCfg.Methods.Basic.InstallPath()
            editor_exe = wizardCfg.Methods.Installer.Bin.Editor()
            editor_config = Methods.EditConfigs.get_saved_editor_config_path()
            editor_resource = inst_path
            
            editor_command = [editor_exe, editor_config, editor_resource]
            Console.ansi_print(str(Process.get_command_exit_code(editor_command, False)))
        def wrapper_do_edit():
            Methods.EditConfigs.update_batching_editor_config()
            Methods.EditConfigs.run_batch_editor()
            #TODO
    class Shortcuts:
        def ShortcutRules(Action, FileName, Args):
            import winshell
            import os

            # These codes used python sequential execution characteristics.

            # Def a switch for base library, affect create shortcut or not
            # after fill information.
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
                targetFullPath = wizardCfg.Methods.Optional.Structure.Program.Tsk.Bin.TskMainExe()
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

                    # Use group name to receive final replace profile
                    # dictionary.
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
        #Methods.CopyFiles.wrapper_do_copy()
        Methods.EditConfigs.wrapper_do_edit()
        Methods.Shortcuts.wrapper_do_create()
        # Turn all install success var to True after all operation success.
        all_install_success = True
    except Exception as e:
        
        Process.handle_exception(e, False)

    return all_install_success