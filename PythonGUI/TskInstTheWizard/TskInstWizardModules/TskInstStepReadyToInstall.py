import TskInstTheWizard as Wizard
import LibTkinter as LibTk
from LibInstallProfile import DecodedProfile
from tkinter import *

wizardCfg = DecodedProfile.Config.StringYaml['TskInstStepInstall']

class Widgets:
    # local variables
    updateLoopSwitch = True
    labelStorageInstalling = StringVar()
    # widgets
    labelReadyToInstall = None
    buttonStartInstall = None

    labelStatus = None
    buttonDisplayExit = None
class Methods:
    def dump_current_install_profile():
        """Copy user settings to disk.
        This method will write whole dictionary to disk for future debug.
        """
        import winshell
        from LibInstallProfile import RawProfileDict
        from LibOperate import WaterWellsYaml as wwYaml
        from LibPython import Environment as Env

        # Set dump location
        desktop = winshell.desktop()
        # Get yaml file name
        yamlName = DecodedProfile.Config.StringYaml['TskInstTheWizard']['Debug_InstProfileDump']
        # Generate file full path
        writeOutPath = Env.Path.Complement.merge_system(desktop, yamlName)
        # Dump settings to disk
        try:
            wwYaml.write_yaml_to_disk(RawProfileDict, writeOutPath)
        except Exception as e:
            from LibPython import Process
            from LibPython import Console
            Process.handle_exception(e, False)
            Console.ansi_print("Write yaml to desktop/disk failed.")

    def ExitButton():
        LibTk.Window.ExitWizard()
        return
    def StartInstall(window):
        import LibSetup
        
        # Display Installing hint.
        Widgets.labelStorageInstalling.set(wizardCfg['labelTextInstalling'])

        # Hide Start Button and Do install.
        LibTk.Window.UnivWizardController_Hide(window, Widgets.buttonStartInstall)
        # Do install.
        all_operate_success = LibSetup.Wrapper_NewInstall()
        
        # Show a short hint after install completed.
        if all_operate_success:
            Widgets.labelStorageInstalling.set(wizardCfg['labelTextDone'])
        else:
            Widgets.labelStorageInstalling.set(wizardCfg['labelTextDoneButError'])
        Widgets.buttonDisplayExit.place(x = 25, y = 55)
        window.update()
        return
    def ConfigureWidgets(window):
        # Label on top.
        Widgets.labelStatus = Label(window,
                                               textvariable = Widgets.labelStorageInstalling)
        Widgets.labelStorageInstalling.set(wizardCfg['readyToInstallHint'])

        # Set but do not show button.
        # The design is create two button on same place,
        # show / hide to display different status.

        # Place Start button first.
        Widgets.buttonStartInstall = Button(window,
                                            text = wizardCfg['buttonStartInstall'],
                                            command = lambda : Methods.StartInstall(window),
                                            width = 10)
        Widgets.buttonDisplayExit = Button(window,
                                           text = wizardCfg.get('buttonTextExit'),
                                           command = lambda : Methods.ExitButton())

        Widgets.labelStatus.place(x = 25, y = 25)
        LibTk.Window.UnivWizardController_Place(window, Widgets.buttonStartInstall)


def Wrapper(window):
    Methods.dump_current_install_profile()
    Methods.ConfigureWidgets(window)
    LibTk.Window.ShowWindow(window)