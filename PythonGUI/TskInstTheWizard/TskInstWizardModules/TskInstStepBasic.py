import TskInstTheWizard as Wizard
import LibTkinter as LibTk
import LibPython as LibPy
import LibInstallProfile as LibProfile

from tkinter import *
from LibPython import UnitConversion as unit

wizardCfg = LibProfile.Resources.Config.StringYaml['TskInstStepBasic']

class Widgets():
    # Local variable
    entryStorageTskInstallPath = StringVar()
    entryStorageTskTempPath = StringVar()
    radioStorageTskInstallType = IntVar()

    # Widgets
    labelDisplaySelectedAdvancedMode = None
    labelDisplayTskInstallPath = None

    radioDisplayNewInstall = None
    radioDisplayUpgrade = None

    entryDisplayTskInstallPath = None

    buttonDisplayBrowseTskInstallPath = None

    buttonTutorial = None
    buttonDisplayNextStep = None
    buttonDisplayExit = None
class Methods():
    def MarkAsDone():
        Wizard.WizardConditions.Modules.TskInstStepBasic = True
        return
    def CopyBack():
        from os.path import normpath

        LibProfile.InstallationProfile['Basic']['InstallPath'] = normpath(Widgets.entryStorageTskInstallPath.get())
        LibProfile.InstallationProfile['Basic']['TempPath'] = normpath(Widgets.entryStorageTskTempPath.get())
        LibProfile.InstallationProfile['Unattended']['UnattendedMode'] = Widgets.radioStorageTskInstallType.get()

        # Confirm install type.
        Wizard.WizardConditions.installType = Widgets.radioStorageTskInstallType.get()

        # if is upgrade mode, in upgrade mode don't need these steps.
        if(Widgets.radioStorageTskInstallType.get() == 2):
            doNothing = None
            #TODO
            Wizard.WizardConditions.Modules.TskInstStepUpgrade = False
        # if is new install, disable data import.
        else:
            Wizard.WizardConditions.Modules.TskInstStepUpgrade = True

        Methods.MarkAsDone()
        Wizard.TimeLine.BackFromAnyModule()

    def SaveSettings():
        tskPathBool = bool(Widgets.entryStorageTskInstallPath.get())
        tempPathBool = bool(Widgets.entryStorageTskTempPath.get())
        installTypeBool = bool(Widgets.radioStorageTskInstallType.get())
        installTypeInt = Widgets.radioStorageTskInstallType.get()
        
        if(tskPathBool is False):
            LibTk.Window.StrNotice(wizardCfg['errorInstallPathEmpty'])
        elif(tempPathBool is False):
            LibTk.Window.StrNotice(wizardCfg['errorTempPathEmpty'])
        elif(installTypeBool is False) :
            LibTk.Window.StrNotice(wizardCfg['errorInstallTypeNotSelected'])
        elif(installTypeInt == 2):
            LibTk.Window.StrNotice(wizardCfg['errorUpgradeNotAvailable'])
        else:
            Methods.CopyBack()
        return
    def RefreshInstallMode(window, result):
        # refresh selected install mode everytime
        # when click on the mode select radio
        Widgets.labelDisplaySelectedInstallMethod.place_forget()
        if result == 1 :
            Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                                  text = unit.StrAddNextLine(wizardCfg['labelTextSelectedNewInstall']),
                                                  justify = LEFT)
        elif result == 2 :
            Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                                  text = unit.StrAddNextLine(wizardCfg['labelTextSelectedUpgrade2']),
                                                  justify = LEFT)
        Widgets.labelDisplaySelectedInstallMethod.place(x = 25, y = 210)
        return
    def DisplayTutorial():
        LibTk.Window.ArrayNotice(wizardCfg['tutorialDialog'])
        return
    def GetDefaultTskTempPath():

        return LibPy.Environment.System.GetSysTempPath() + r'\TensokukanTemp'
    def AskTskInstallDirName():
        import traceback
        from LibPython import Process
        from LibPython import Environment as Env
        from os.path import normpath
        
        options = LibProfile.Resources.Config.TkinterYaml['BrowseTskInstallPath']
        result = LibTk.FileDialog.AskDirectoryName(options)

        if bool(result):
            try:
                Widgets.entryStorageTskInstallPath.set(
                    Env.Path.Complement.merge_system(
                        result, LibProfile.Resources.Methods.Structure.Program.Tsk.Bin.DefaultInstallFolder()
                        )
                    )
            except Exception as err:
                traceback.print_tb(err.__traceback__)
        return
    def ConfigureWidgets(window):
        # lables
        Widgets.labelDisplaySelectedAdvancedMode = Label(window,
                                     text = wizardCfg['labelTextSelectedAdvancedMode'])
        Widgets.labelDisplayTskInstallPath = Label(window,
                                        text = wizardCfg['labelTextTskInstallPath'])
    
        # radio
        Widgets.radioDisplayNewInstall = Radiobutton(window,
                                             variable = Widgets.radioStorageTskInstallType,
                                             value = 1,
                                             text = wizardCfg['radioTextNewInstall'],
                                             command = lambda : Methods.RefreshInstallMode(window, 1))
        Widgets.radioDisplayUpgrade = Radiobutton(window,
                                                 variable = Widgets.radioStorageTskInstallType,
                                                 value = 2,
                                                 text = wizardCfg['radioTextUpgrade'],
                                                 command = lambda : Methods.RefreshInstallMode(window, 2))
        # entry
        Widgets.entryDisplayTskInstallPath = Entry(window,
                                             textvariable = Widgets.entryStorageTskInstallPath,
                                             width = 50)
        Widgets.entryStorageTskTempPath.set(Methods.GetDefaultTskTempPath())
        # button, two browse
        Widgets.buttonDisplayBrowseTskInstallPath = Button(window,
                                               text = wizardCfg['buttonTextBrowseTskInstallPath'],
                                               command = lambda : Methods.AskTskInstallDirName())
        # button, next step and tutorial
        Widgets.buttonDisplayNextStep = Button(window,
                                text = wizardCfg['buttonTextNextStep'],
                                command = lambda : Methods.SaveSettings(),
                                width = 10)
        Widgets.buttonTutorial = Button(window,
                                        text = wizardCfg['buttonTutorial'],
                                        command = lambda : Methods.DisplayTutorial(),
                                        width = 10)
        # Generate this object but do not show immediately
        Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                              text = wizardCfg['labelTextSelectedNewInstall'])

        # Set default install type as new install, var 1.
        # But do not set right now, this is a foolproof - design
        # if someone forgot he is upgrading the product and the selected new,
        # he may lose his data.
        #wizard.WizardConditions.installType.set(1)

        # place GUI objects
        Widgets.labelDisplaySelectedAdvancedMode.place(x = 25, y = 25)

        Widgets.radioDisplayNewInstall.place(x = 25, y = 105)
        Widgets.radioDisplayUpgrade.place(x = 160, y = 105)

        Widgets.labelDisplayTskInstallPath.place(x = 25, y = 175)
        Widgets.entryDisplayTskInstallPath.place(x = 125, y = 175)
        Widgets.buttonDisplayBrowseTskInstallPath.place(x = 500, y = 175)

        LibTk.Window.UnivWizardController_Place(window, Widgets.buttonDisplayNextStep)
        LibTk.Window.UnivWizardHint_Place(window, Widgets.buttonTutorial)
        return

def Wrapper(window):
    Methods.ConfigureWidgets(window)
    # Detect if auto display tutorial is true
    if Wizard.WizardConditions.autoTutorial:
        LibTk.Window.ArrayNotice(wizardCfg['tutorialDialog'])
    LibTk.Window.ShowWindow(window)
    return