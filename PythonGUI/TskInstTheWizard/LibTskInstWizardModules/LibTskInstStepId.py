import TskInstTheWizard as Wizard
import LibTkinter as LibTk
import LibPython as LibPy
from LibInstallProfile import RawProfileDict
from LibInstallProfile import DecodedProfile
from tkinter import *

wizardCfg = DecodedProfile.Config.StringYaml['LibStringStepId']

class Widgets:
    # local variable
    entryStorageIdYamlPath = StringVar()
    radioStorageIdInstallType = IntVar()
    # label
    labelTitleTencoID = None

    # radio
    radioDisplayTypeIn = None
    radioDisplayFromYaml = None
    radioDisplayRegister = None
    radioDisplaySkipId = None
    # entry
    entryDisplayIdYamlPath = None
    # button
    buttonDisplayNextStep = None
    buttonBrowseIdYamlPath = None
    buttonTutorial = None
class Methods:
    def BrowseIdYaml(window):
        from os.path import normpath

        LibTk.InitializeLibTkinter()
        options = DecodedProfile.Config.TkinterYaml.get('BrowseIdYaml')
        result = LibTk.FileDialog.AskFileName(options)
        if bool(result):
            Widgets.entryStorageIdYamlPath.set(normpath(result))
        return
    # Tell processor this module has been done
    def MarkAsDone():
        Wizard.WizardConditions.Modules.LibStepId = True
        return
    def PassedCheck(case):
        # 1 means type in manually.
        if case == 1:
            Wizard.WizardConditions.idInstallMode = Widgets.radioStorageIdInstallType.get()

            RawProfileDict['Unattended']['ManageId'] = True

            Methods.MarkAsDone()
            Wizard.TimeLine.BackFromAnyModule()

        # 4 means skip id settings.
        elif case == 4:
            # Not sure if this is actually needs to be set to zero.
            Wizard.WizardConditions.idInstallMode = 0
            RawProfileDict['Unattended']['ManageId'] = False
            Methods.MarkAsDone()
            Wizard.WizardConditions.Modules.TskInstStepId = True
            Wizard.TimeLine.BackFromAnyModule()
        return
    def DisplayTutorial():
        LibTk.Window.ArrayNotice(wizardCfg.get('tutorialDialog'))
        return
    def SaveButton():
        # Bool data for fill check
        idInstallTypeBool = bool(Widgets.radioStorageIdInstallType.get())
        idYamlLocationBool = bool(Widgets.entryStorageIdYamlPath.get())
        # Raw data for yaml check
        idInstallType = Widgets.radioStorageIdInstallType.get()
        
        if(idInstallTypeBool is not True):
            LibTk.Window.ArrayNotice(wizardCfg.get('errorIdTypeNotSelected'))

        # 4 means skip id settings.
        elif(idInstallType == 4):
            Methods.PassedCheck(4)

        else:
            # 3 means register new id.
            if(idInstallType == 3) :
                LibTk.Window.ArrayNotice(wizardCfg.get('errorRegisterUnavailable'))

            elif(idInstallType == 2 and idYamlLocationBool is not True) :
                #TODO
                # This decision is prevent user select a not implement feature
                # remove it once the feature is implemented.
                LibTk.Window.ArrayNotice(wizardCfg.get('errorIdInstallYamlEmpty'))

            elif(idInstallType == 2 and idYamlLocationBool):
                #TODO
                LibTk.Window.ArrayNotice(wizardCfg.get('errorImportYamlUnavailable'))

            else:
                # Should be "1" this time.
                # 1 means type in manually.
                Methods.PassedCheck(1)
        return
    def ConfigureWidgets(window):
        # lables
        Widgets.labelTitleTencoID = Label(window, text = wizardCfg.get('labelTextTencoID'))

        # radios
        Widgets.radioDisplayTypeIn = Radiobutton(window,
                                                  variable = Widgets.radioStorageIdInstallType,
                                                  value = 1,
                                                  text = wizardCfg.get('radioTextTypeIn'))
        Widgets.radioDisplayFromYaml = Radiobutton(window,
                                              variable = Widgets.radioStorageIdInstallType,
                                              value = 2,
                                              text = wizardCfg.get('radioTextFromYaml'))
        Widgets.radioDisplayRegister = Radiobutton(window,
                                             variable = Widgets.radioStorageIdInstallType,
                                             value = 3,
                                             text = wizardCfg.get('radioTextRegister'))
        Widgets.radioDisplaySkipId = Radiobutton(window,
                                              variable = Widgets.radioStorageIdInstallType,
                                              value = 4,
                                              text = wizardCfg.get('radioTextSkipId'))
        # entry
        Widgets.entryDisplayIdYamlPath = Entry(window,
                                               textvariable = Widgets.entryStorageIdYamlPath)
        # button
        Widgets.buttonDisplayNextStep = Button(window,
                                        text = wizardCfg.get('buttonTextNextStep'),
                                        command = lambda : Methods.SaveButton(),
                                        width = 10)
        Widgets.buttonBrowseIdYamlPath = Button(window,
                                                text = wizardCfg.get('buttonTextBrowseYaml'),
                                                command = lambda : Methods.BrowseIdYaml(window))
        Widgets.buttonTutorial = Button(window,
                                        text = wizardCfg.get('buttonTutorial'),
                                        command = lambda : Methods.DisplayTutorial(),
                                        width = 10)

        # place GUI objects
        Widgets.labelTitleTencoID.place(x = 25, y = 25)
        Widgets.radioDisplayTypeIn.place(x = 160, y = 25)
        Widgets.radioDisplayFromYaml.place(x = 160, y = 55)
        Widgets.radioDisplayRegister.place(x = 160, y = 115)
        Widgets.radioDisplaySkipId.place(x = 160, y = 145)
        Widgets.entryDisplayIdYamlPath.place(x = 160, y = 85)
        Widgets.buttonBrowseIdYamlPath.place(x = 400, y = 85)

        #Widgets.buttonDisplayNextStep.place(x = 530, y = 25)
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