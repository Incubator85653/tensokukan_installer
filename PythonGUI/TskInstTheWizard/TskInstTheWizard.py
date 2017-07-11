import LibTkinter as LibTk

from tkinter import *
from LibTkinter import Window as LibTkWin

class RootVar:
    # Define the default window (root window) of entire installer
    TheInstaller = None
    wizardCfg = None

# Step means methods to control each step's interface
class WizardSteps():
    def LibStepWizardMode(window):
        LibTkWin.CleanWidgets(window)
        import LibTskInstStepWizardMode as TheStep
        TheStep.Wrapper(window)
        return
    def LibStepId(window):
        LibTkWin.CleanWidgets(window)
        import LibTskInstStepId as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepBasic(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepBasic as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepId(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepId as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepGame(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepGame as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepUpgrade(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepUpgrade as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepShortcuts(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepShortcuts as TheStep
        TheStep.Wrapper(window)
        return
    def TskInstStepSetup(window):
        LibTkWin.CleanWidgets(window)
        import TskInstStepSetup as TheStep
        TheStep.Wrapper(window)
        return

# Imagine you're playing a video.
# I'm in chapter select, do I have watched one of the videos?
class TimeLine():
    def BackFromAnyModule():
        if(WizardConditions.Modules.LibStepModeDecision is False):
            WizardSteps.LibStepWizardMode(RootVar.TheInstaller)
        elif(WizardConditions.Modules.TskInstStepBasic is False):
            WizardSteps.TskInstStepBasic(RootVar.TheInstaller)
        elif(WizardConditions.Modules.TskInstStepUpgrade is False):
            WizardSteps.TskInstStepUpgrade(RootVar.TheInstaller)
        elif(WizardConditions.Modules.TskInstStepId is False):
            WizardSteps.TskInstStepId(RootVar.TheInstaller)
        elif(WizardConditions.Modules.TskInstStepGame is False):
            WizardSteps.TskInstStepGame(RootVar.TheInstaller)
        elif(WizardConditions.Modules.TskInstStepShortcuts is False):
            WizardSteps.TskInstStepShortcuts(RootVar.TheInstaller)
        else:
            # Dump settings to desktop for debug.
            import winshell
            import os
            from LibResources import InstallationProfile
            from LibOperate import WaterWellsYaml as wwYaml
            from LibPython import Environment

            desktop = winshell.desktop()
            yamlName = RootVar.wizardCfg['Debug_InstProfileDump']

            writeOutPath = Environment.Path.Complement.merge_system(desktop, yamlName)
            wwYaml.write_yaml_to_disk(InstallationProfile, writeOutPath)

            # Display ReadyToInstall interface.
            # Debugging, don't actually run installer.
            #WizardSteps.TskInstStepSetup(RootVar.TheInstaller)
        return

# Conditions means the variables should be changed by GUI,
# and decide what to do by use other methods.
class WizardConditions():
    # The following class Modules.
    # Each boolean variable means a wizard step
    # Once a variable is "mark as done" (True)
    #   the step process method will skip that step.
    # Otherwize if it is false, run that step.
    # Each step will mark them as done when user
    #   click on "Save" or "Next step".

    # Lib steps means they are step reference.
    # Some step require to do a specify step first
    #   before actual execute that step.

    # Step process method do not do the reference,
    #   the reference process by sub step itself.

    # Example:
    # Step B require Step LibA already mark as done,
    # step process method do not run Step LibA,
    # just call Step B directly. Step B check LibA,
    # if LibA is False, run LibA instead of run B.
    # When LibA is done, endpoint not return to Step B,
    # and back to step process method again.
    # Step process method will find that Step B still is False,
    # then run Step B again, but at this time,
    # Step B will find that LibA is True, so Step B is run.
    # In this case after Step B is True, step process method will
    # find that Step C is False, then call Step C, etc.
    class Modules:
        LibStepModeDecision = False
        LibStepId = False

        TskInstStepBasic = False
        TskInstStepId = False
        TskInstStepGame = False
        TskInstStepUpgrade = False
        TskInstStepShortcuts = False
        TskInstStepInstall = False
    # Witch mode to install, novice mode = 1, debug mode = 2
    wizardMode = None
    # Witch mode to upgrade, new install = 1, upgrade = 2
    installType = None
    # How to import username and password, type manually = 1, from file = 2, new register = 3, skip = 0
    idInstallMode = None
    # Automatically display tutorial, enable = True, disable = False
    autoTutorial = None

def InitializeSelf():
    import LibTkinter as LibTk
    import LibResources as LibRes

    # Create a tkinter root window.
    RootVar.wizardCfg = LibRes.Resources.Config.StringYaml['TskInstTheWizard']
    RootVar.TheInstaller = Tk()
    LibTk.Window.InitializeWindow(RootVar.TheInstaller, RootVar.wizardCfg)

    # Set Wizard conditions after created tkinter root window.
    # Wait, why we can't directly use int? Let's give it a try.

    #WizardConditions.wizardMode = IntVar()
    #WizardConditions.installType = IntVar()
    #WizardConditions.idInstallMode = IntVar()
    WizardConditions.autoTutorial = False
    return

# The method is available for the startup script.
# Faster initialize entire installer.
def Wrapper():
    InitializeSelf()
    TimeLine.BackFromAnyModule()
    return