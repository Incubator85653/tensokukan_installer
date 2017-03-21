import TskInstTheWizard as Wizard
import LibTskInstTkinter as LibTk
import LibTskInstPython as LibPy
import LibTskInstResources as LibRes
import LibTskInstDebug as LibBug
from tkinter import *

wizardCfg = LibRes.Resources.Config.StringYaml.get('TskInstStepBasic')

class Widgets():
    # Local variable
    entryStorageTskInstallPath = StringVar()
    entryStorageTskTempPath = StringVar()
    radioStorageTskInstallType = IntVar()

    # Widgets
    labelDisplaySelectedAdvancedMode = None
    labelDisplayTskInstallPath = None
    labelDisplayTskTempPath = None

    radioDisplayNewInstall = None
    radioDisplayUpgrade = None

    entryDisplayTskInstallPath = None
    entryDisplayTskTempPath = None

    buttonDisplayBrowseTskInstallPath = None
    buttonDisplayBrowseTskTempPath = None

    buttonTutorial = None
    buttonDisplayNextStep = None
    buttonDisplayExit = None
class Methods():
    def MarkAsDone():
        Wizard.WizardConditions.Modules.TskInstStepBasic = True
        return
    def CopyBack():
        from os.path import normpath

        LibRes.InstallationProfile['Basic']['InstallPath'] = normpath(Widgets.entryStorageTskInstallPath.get())
        LibRes.InstallationProfile['Basic']['TempPath'] = normpath(Widgets.entryStorageTskTempPath.get())
        LibRes.InstallationProfile['Unattended']['UnattendedMode'] = Widgets.radioStorageTskInstallType.get()

        # Confirm install type.
        Wizard.WizardConditions.installType = Widgets.radioStorageTskInstallType.get()

        # if is upgrade mode, in upgrade mode don't need these steps.
        if(Widgets.radioStorageTskInstallType.get() == 2):
            LibTk.Window.StrNotice('Feature not available.')
            #TODO
        # if is new install, disable data import.
        else:
            Wizard.WizardConditions.Modules.TskInstStepDataImport = True

        Methods.MarkAsDone()
        Wizard.TimeLine.BackFromAnyModule()
        return
    def SaveSettings():
        tskPathBool = bool(Widgets.entryStorageTskInstallPath.get())
        tempPathBool = bool(Widgets.entryStorageTskTempPath.get())
        installTypeBool = bool(Widgets.radioStorageTskInstallType.get())
        installTypeInt = Widgets.radioStorageTskInstallType.get()
        
        if(tskPathBool is False):
            LibTk.Window.StrNotice(wizardCfg.get('errorInstallPathEmpty'))
        elif(tempPathBool is False):
            LibTk.Window.StrNotice(wizardCfg.get('errorTempPathEmpty'))
        elif(installTypeBool is False) :
            LibTk.Window.StrNotice(wizardCfg.get('errorInstallTypeNotSelected'))
        elif(Widgets.radioStorageTskInstallType.get() == 2):
            LibTk.Window.StrNotice(wizardCfg.get('errorUpgradeNotAvailable'))
        else:
            Methods.CopyBack()
        return
    def RefreshInstallMode(window, result):
        # refresh selected install mode everytime
        # when click on the mode select radio
        Widgets.labelDisplaySelectedInstallMethod.place_forget()
        if result == 1 :
            Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                                  text = wizardCfg.get('labelTextSelectedNewInstall'))
        elif result == 2 :
            Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                                  text = wizardCfg.get('labelTextSelectedUpgrade2'))
        Widgets.labelDisplaySelectedInstallMethod.place(x = 25, y = 210)
        return
    def DisplayTutorial():
        LibTk.Window.ArrayNotice(wizardCfg.get('tutorialDialog'))
        return
    def GetDefaultTskTempPath():

        return LibPy.Environment.System.GetSysTempPath() + r'\TensokukanTemp'
    def AskTskInstallDirName():
        from os.path import normpath
        
        options = LibRes.Resources.Config.TkinterYaml.get('BrowseTskInstallPath')
        result = LibTk.FileDialog.AskDirectoryName(options)

        if bool(result):
            Widgets.entryStorageTskInstallPath.set(normpath(result + '/TensokukanI18N'))
        return
    def AskTempDirName():
        from os.path import normpath

        options = LibRes.Resources.Config.TkinterYaml.get('BrowseTskTempPath')
        result = LibTk.FileDialog.AskDirectoryName(options)

        if bool(result):
            Widgets.entryStorageTskTempPath.set(normpath(result + '/TensokukanTemp'))
        else:
            LibTk.Window.StrNotice(LibPy.UnitConversion.FormatArray2String(wizardCfg.get('errorCancelledSelectTemp')))
            Widgets.entryStorageTskTempPath.set(Methods.GetDefaultTskTempPath())
        return
    def ConfigureWidgets(window):
        # lables
        Widgets.labelDisplaySelectedAdvancedMode = Label(window,
                                     text = wizardCfg.get('labelTextSelectedAdvancedMode'))
        Widgets.labelDisplayTskInstallPath = Label(window,
                                        text = wizardCfg.get('labelTextTskInstallPath'))
        Widgets.labelDisplayTskTempPath = Label(window,
                                     text = wizardCfg.get('labelTextTskTempPath'))
    
        # radio
        Widgets.radioDisplayNewInstall = Radiobutton(window,
                                             variable = Widgets.radioStorageTskInstallType,
                                             value = 1,
                                             text = wizardCfg.get('radioTextNewInstall'),
                                             command = lambda : Methods.RefreshInstallMode(window, 1))
        Widgets.radioDisplayUpgrade = Radiobutton(window,
                                                 variable = Widgets.radioStorageTskInstallType,
                                                 value = 2,
                                                 text = wizardCfg.get('radioTextUpgrade'),
                                                 command = lambda : Methods.RefreshInstallMode(window, 2))
        # entry
        Widgets.entryDisplayTskInstallPath = Entry(window,
                                             textvariable = Widgets.entryStorageTskInstallPath,
                                             width = 50)
        Widgets.entryDisplayTskTempPath = Entry(window,
                                          textvariable = Widgets.entryStorageTskTempPath,
                                          width = 50)
        Widgets.entryStorageTskTempPath.set(Methods.GetDefaultTskTempPath())
        # button, two browse
        Widgets.buttonDisplayBrowseTskInstallPath = Button(window,
                                               text = wizardCfg.get('buttonTextBrowseTskInstallPath'),
                                               command = lambda : Methods.AskTskInstallDirName())
        Widgets.buttonDisplayBrowseTskTempPath = Button(window,
                                            text = wizardCfg.get('buttonTextBrowseTskTempPath'),
                                            command = lambda : Methods.AskTempDirName())
        # button, next step and tutorial
        Widgets.buttonDisplayNextStep = Button(window,
                                text = wizardCfg.get('buttonTextNextStep'),
                                command = lambda : Methods.SaveSettings(),
                                width = 10)
        Widgets.buttonTutorial = Button(window,
                                        text = wizardCfg['buttonTutorial'],
                                        command = lambda : Methods.DisplayTutorial(),
                                        width = 10)
        # Generate this object but do not show immediately
        Widgets.labelDisplaySelectedInstallMethod = Label(window,
                                              text = wizardCfg.get('labelTextSelectedNewInstall'))

        # Set default install type as new install, var 1.
        # But do not set right now, this is a foolproof - design
        # if someone forgot he is upgrading the product and the selected new,
        # he may lose his data.
        #wizard.WizardConditions.installType.set(1)

        # place GUI objects
        Widgets.labelDisplaySelectedAdvancedMode.place(x = 25, y = 25)

        Widgets.labelDisplayTskInstallPath.place(x = 25, y = 105)
        Widgets.entryDisplayTskInstallPath.place(x = 125, y = 105)
        Widgets.buttonDisplayBrowseTskInstallPath.place(x = 500, y = 105)

        # Do not show the Temp option unless the user specified.
        # After Tsk Network 2017 Build2, ANSI-only-characters temp path is not required anymore.

        if LibBug.StepBasic_ShowTempOption:
            Widgets.labelDisplayTskTempPath.place(x = 25, y = 140)
            Widgets.entryDisplayTskTempPath.place(x = 125, y = 140)
            Widgets.buttonDisplayBrowseTskTempPath.place(x = 500, y = 140)

        Widgets.radioDisplayNewInstall.place(x = 25, y = 175)
        Widgets.radioDisplayUpgrade.place(x = 160, y = 175)

        LibTk.Window.UnivWizardController_Place(window, Widgets.buttonDisplayNextStep)
        LibTk.Window.UnivWizardHint_Place(window, Widgets.buttonTutorial)
        return

def Wrapper(window):
    Methods.ConfigureWidgets(window)
    # Detect if auto display tutorial is true
    if Wizard.WizardConditions.autoTutorial:
        LibTk.Window.ArrayNotice(wizardCfg.get('tutorialDialog'))
    LibTk.Window.ShowWindow(window)
    return