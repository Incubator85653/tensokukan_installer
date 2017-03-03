import LibTskInstTkinter as LibTk
import LibTskInstPython as LibPy
import LibTskInstResources as LibRes
import TskInstTheWizard as Wizard

from tkinter import *

wizardCfg = LibRes.Resources.Config.StringYaml['LibTskInstStepWizardMode']

class Widgets:
    # Local variables
    radioStorageWizardMode = IntVar()
    checkbuttonStorageAutoHint = IntVar()

    installHint = None
    whoAmI = None
    warn1 = None
    warn2 = None

    wizardModeNovice = None
    wizardModeDebug = None

    checkbuttonAutoHint = None

    nextButton = None
    exitButton = None
class Methods:
    def MarkAsDone():
        Wizard.WizardConditions.Modules.LibTskInstStepModeDecision = True
        return
    def CopyBack():
        Wizard.WizardConditions.wizardMode = Widgets.radioStorageWizardMode.get()
        if bool(Widgets.checkbuttonStorageAutoHint.get()):
            Wizard.WizardConditions.autoTutorial = True

        Methods.MarkAsDone()
        Wizard.TimeLine.BackFromAnyModule()
        return
    def SaveButton():
        if(Widgets.radioStorageWizardMode.get() != 2):
            LibTk.Window.ArrayNotice(wizardCfg.get('errorUseDebugMode'))
        else:
            Methods.CopyBack()
        return
    def ConfigWidgets(window):
        # lables
        Widgets.installHint = Label(window,
                      text = wizardCfg.get('labelTextStartInstall'))
        Widgets.whoAmI = Label(window,
                      text = wizardCfg.get('labelTextWizardModeSelect'))
        Widgets.warn1 = Label(window,
                      text = LibPy.UnitConversion.FormatArray2String(wizardCfg.get('labelTextDebugWarn')),
                      justify = LEFT)

        # radio and radio variable
        Widgets.wizardModeNovice = Radiobutton(window,
                            variable = Widgets.radioStorageWizardMode,
                            value = 1,
                            text = wizardCfg.get('labelTextNovice'))
        Widgets.wizardModeDebug = Radiobutton(window,
                            variable = Widgets.radioStorageWizardMode,
                            value = 2,
                            text = wizardCfg.get('labelTextAdvanced'))
        Widgets.checkbuttonAutoHint = Checkbutton(window,
                                                  text = wizardCfg['checkbuttonAutoHint'],
                                                  variable = Widgets.checkbuttonStorageAutoHint)

        # buttons
        Widgets.nextButton = Button(window,
                            text = wizardCfg.get('buttonTextNextStep'),
                            command = lambda : Methods.SaveButton(),
                            width = 10)

        # place GUI object
        Widgets.installHint.place(x = 25, y = 25)
        Widgets.whoAmI.place(x = 25, y = 85)
        Widgets.wizardModeNovice.place(x = 100, y = 85)
        Widgets.wizardModeDebug.place(x = 100, y = 110)
        Widgets.warn1.place(x = 120, y = 140)
        Widgets.checkbuttonAutoHint.place(x = 25, y = 210)
        #Widgets.nextButton.place(x = 530, y = 25)
        #Widgets.exitButton.place(x = 530, y = 60)
        LibTk.Window.UnivWizardController_Place(window, Widgets.nextButton)

        # initalize default options
        # default radio button:
        Widgets.radioStorageWizardMode.set(2)

        # Check auto hint by default:
        Widgets.checkbuttonStorageAutoHint.set(1)
        return


def Wrapper(window):
    Methods.ConfigWidgets(window)
    LibTk.Window.ShowWindow(window)
    return