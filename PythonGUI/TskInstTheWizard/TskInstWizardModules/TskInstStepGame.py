import TskInstTheWizard as Wizard
import LibResources as LibRes
import LibTkinter as LibTk

from tkinter import *
from os.path import normpath

wizardCfg = LibRes.Resources.Config.StringYaml.get('TskInstStepGame')

GameTitles = LibRes.Resources.Config.GamesYaml.get('Titles')
GameSwrs = LibRes.Resources.Config.GamesYaml.get('SWRSAddr')

class Widgets:
    # Local variables
    entryStorageGameExePath = StringVar()
    comboboxStorageGameVersionResult = StringVar()
    comboboxStorageGameVersionList = GameTitles
    # Widgets
    labelDisplayGameExePath = None
    entryDisplayGameExePath = None
    buttonDisplayBrowseGameExePath = None

    labelDisplayGameVersion = None
    comboboxDisplayGameVersionList = None

    buttonDisplayNextStep = None
    buttonTutorial = None
class Methods:
    def MarkAsDone():
        Wizard.WizardConditions.Modules.TskInstStepGame = True
        return
    def CopyBack():
        from os.path import normpath

        LibRes.InstallationProfile['Basic']['GameExePath'] = normpath(Widgets.entryStorageGameExePath.get())
        LibRes.InstallationProfile['UserData']['SWRSAddr7z'] = GameSwrs.get(Widgets.comboboxStorageGameVersionResult.get())

        LibRes.InstallationProfile['Unattended']['ManageGameExePath'] = True
        LibRes.InstallationProfile['Unattended']['ManageSWRSAddr'] = True

        Methods.MarkAsDone()
        Wizard.TimeLine.BackFromAnyModule()
        return
    def SaveButton(gameExePath, gameVer):
        gameExePathBool = bool(gameExePath.get())
        gameVerBool = bool(gameVer.get())
        installType = Wizard.WizardConditions.installType

        if(gameExePathBool is False and installType == 1):
            LibTk.Window.StrNotice(wizardCfg.get('errorTextGameExecPathEmpty'))
        elif(gameVerBool is False):
            LibTk.Window.StrNotice(wizardCfg.get('errorTextGameVersionEmpty'))
        else:
            Methods.CopyBack()
        return
    def AskGameExecFileName():
        from os.path import normpath

        LibTk.InitializeLibTkinter()
        options = LibRes.Resources.Config.TkinterYaml.get('BrowseGameExec')
        result = LibTk.FileDialog.AskFileName(options)

        if bool(result):
            Widgets.entryStorageGameExePath.set(normpath(result))
        return
    def DisplayTutorial():
        LibTk.Window.ArrayNotice(wizardCfg.get('tutorialDialog'))
        return
    def ShowWidgets(window):
        stepMode = LibRes.InstallationProfile.get('Unattended').get('UnattendedMode')

        if(stepMode == 1):
            #place GUI objects as default layout
            Widgets.labelDisplayGameExePath.place(x = 25, y = 25)
            Widgets.entryDisplayGameExePath.place(x = 25, y = 55)
            Widgets.buttonDisplayBrowseGameExePath.place(x = 165, y = 55)
            Widgets.labelDisplayGameVersion.place(x = 25, y = 85)
            Widgets.comboboxDisplayGameVersionList.place(x = 25, y = 115)
            
            LibTk.Window.UnivWizardController_Place(window, Widgets.buttonDisplayNextStep)
            LibTk.Window.UnivWizardHint_Place(window, Widgets.buttonTutorial)

        elif(stepMode == 2):
            #place GUI objects as data import layout
            Widgets.labelDisplayGameVersion.place(x = 25, y = 25)
            Widgets.comboboxDisplayGameVersionList.place(x = 25, y = 55)

            LibTk.Window.UnivWizardController_Place(window, Widgets.buttonDisplayNextStep)
        return
    def ConfigureWidgets(window):
        #Label
        Widgets.labelDisplayGameExePath = Label(window,
                                    text = wizardCfg.get('entryTextGameInstalledPath'))
        Widgets.labelDisplayGameVersion = Label(window,
                                    text = wizardCfg.get('entryTextGameVersion'))
        #Entry
        Widgets.entryDisplayGameExePath = Entry(window,
                                      textvariable = Widgets.entryStorageGameExePath)
        #Button
        Widgets.buttonDisplayBrowseGameExePath = Button(window,
                                        text = wizardCfg.get('buttonTextBrowseGameExec'),
                                        command = lambda : Methods.AskGameExecFileName())
        Widgets.buttonDisplayNextStep = Button(window,
                                    text = wizardCfg.get('buttonTextNextStep'),
                                    command = lambda : Methods.SaveButton(Widgets.entryStorageGameExePath,
                                                                    Widgets.comboboxStorageGameVersionResult),
                                    width = 10)
        Widgets.buttonTutorial = Button(window,
                                        text = wizardCfg['buttonTutorial'],
                                        command = lambda : Methods.DisplayTutorial(),
                                        width = 10)
        #combobox
        Widgets.comboboxDisplayGameVersionList = ttk.Combobox(window,
                                               state = 'readonly',
                                               textvariable = Widgets.comboboxStorageGameVersionResult,
                                               values = Widgets.comboboxStorageGameVersionList,
                                               width = 80)


        #place GUI objects
        # Use config dump
        #Widgets.labelDisplayGameExePath.place(x = 25, y = 25)
        #Widgets.entryDisplayGameExePath.place(x = 25, y = 55)
        #Widgets.buttonDisplayBrowseGameExePath.place(x = 165, y =55)
        #Widgets.labelDisplayGameVersion.place(x = 25, y = 85)
        #Widgets.comboboxDisplayGameVersionList.place(x = 25, y = 115)
        #Widgets.buttonDisplayNextStep.place(x = 530, y = 25)
    
        return
def Wrapper(window):
    Methods.ConfigureWidgets(window)
    Methods.ShowWidgets(window)
    # Detect if auto display tutorial is true
    if Wizard.WizardConditions.autoTutorial:
        LibTk.Window.ArrayNotice(wizardCfg.get('tutorialDialog'))
    LibTk.Window.ShowWindow(window)
    return