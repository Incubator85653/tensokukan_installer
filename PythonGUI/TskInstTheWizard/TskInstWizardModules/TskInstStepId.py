import TskInstTheWizard as Wizard
import LibTkinter as LibTk
import LibResources as LibRes
import LibPython as LibPy

from LibResources import Resources
from LibResources import InstallationProfile
from tkinter import *

wizardCfg = Resources.Config.StringYaml.get('TskInstStepId')
typeInStr = wizardCfg.get('TypeIn')

class Widgets:
    class TypeIn:
        # String
        stepStr = wizardCfg.get('TypeIn')
        # Local variables
        entryStorageTencoId = StringVar()
        entryStorageTencoPassword = StringVar()
        # Widgets
        labelDisplayTitle = None
        labelDisplayId = None
        labelDisplayPassword = None
        labelDisplaySuggest = None
        labelDisplaySuggest2 = None
        labelDisplaySuggest3 = None

        entryDisplayTencoId = None
        entryDisplayTencoPassword = None

        buttonDisplayCheck = None
        buttonDisplayNextStep = None
        buttonTutorial = None
class Methods:
    def MarkAsDone():
        Wizard.WizardConditions.Modules.TskInstStepId = True
        return

    class Manually:
        def OpenUrl(id):
            import webbrowser
            idBool = bool(id)
            if(idBool):
                url1 = 'https://tenco.info/account/'
                url2 = '/manage/profile/'
                url = url1 + str(id) + url2
                webbrowser.open_new_tab(url)
            else:
                LibTk.Window.StrNotice(typeInStr.get('idFirst'))
            return
        def CopyBack():
            # Copy data from local to conditions
            LibRes.InstallationProfile['UserData']['TencoID'] = Widgets.TypeIn.entryStorageTencoId.get()
            LibRes.InstallationProfile['UserData']['TencoPassword'] = Widgets.TypeIn.entryStorageTencoPassword.get()

            LibRes.InstallationProfile['Unattended']['ManageId'] = True

            Methods.MarkAsDone()
            # and I'm home
            Wizard.TimeLine.BackFromAnyModule()
            return
        def DisplayTutorial():
            LibTk.Window.ArrayNotice(typeInStr.get('tutorialDialog'))
            return
        def SaveButton():
            idBool = bool(Widgets.TypeIn.entryStorageTencoId.get())
            pwdBool = bool(Widgets.TypeIn.entryStorageTencoPassword.get())

            if(idBool and pwdBool):
                Methods.Manually.CopyBack()
            else:
                LibTk.Window.StrNotice(typeInStr.get('beforeSave'))
            return
        def ConfigureWidgets(window):
            # Labels
            Widgets.TypeIn.labelDisplayTitle = Label(window,
                                              text = typeInStr.get('labelTextTitle'))
            Widgets.TypeIn.labelDisplayId = Label(window,
                                          text = typeInStr.get('labelTextId'))
            Widgets.TypeIn.labelDisplayPassword = Label(window,
                                                text = typeInStr.get('labelTextPassword'))
            Widgets.TypeIn.labelDisplaySuggest = Label(window,
                                            text = LibPy.UnitConversion.FormatArray2String(typeInStr.get('labelTextSuggest')),
                                            justify = LEFT)

            # Entry
            Widgets.TypeIn.entryDisplayTencoId = Entry(window,
                                           textvariable = Widgets.TypeIn.entryStorageTencoId)
            Widgets.TypeIn.entryDisplayTencoPassword = Entry(window,
                                            textvariable = Widgets.TypeIn.entryStorageTencoPassword)
            # Button
            Widgets.TypeIn.buttonDisplayCheck = Button(window,
                                                text = typeInStr.get('buttonTextCheck'),
                                                command = lambda : Methods.Manually.OpenUrl(Widgets.TypeIn.entryStorageTencoId.get()),
                                                width = 10)
            Widgets.TypeIn.buttonDisplayNextStep = Button(window,
                                               text = typeInStr.get('buttonTextNextStep'),
                                               command = lambda : Methods.Manually.SaveButton(),
                                               width = 10)
            Widgets.TypeIn.buttonTutorial = Button(window,
                                            text = typeInStr['buttonTutorial'],
                                            command = lambda : Methods.Manually.DisplayTutorial(),
                                            width = 10)

            # place GUI objects
            Widgets.TypeIn.labelDisplayTitle.place(x = 25, y = 25)
            Widgets.TypeIn.labelDisplayId.place(x = 25, y = 55)
            Widgets.TypeIn.entryDisplayTencoId.place(x = 25, y = 85)
            Widgets.TypeIn.labelDisplayPassword.place(x = 25, y = 115)
            Widgets.TypeIn.entryDisplayTencoPassword.place(x = 25, y = 145)
            Widgets.TypeIn.labelDisplaySuggest.place(x = 25, y = 205)
            Widgets.TypeIn.buttonDisplayCheck.place(x = 200, y = 81)

            LibTk.Window.UnivWizardController_Place(window, Widgets.TypeIn.buttonDisplayNextStep)
            LibTk.Window.UnivWizardHint_Place(window, Widgets.TypeIn.buttonTutorial)
            return
    def DetectIdReference(window):
        if(InstallationProfile.get('Unattended').get('ManageId') is False):
            Methods.MarkAsDone()
            Wizard.TimeLine.BackFromAnyModule()

        idInstallMode = Wizard.WizardConditions.idInstallMode
        if(idInstallMode == 1):
            Methods.Manually.ConfigureWidgets(window)
        #elif(idInstallMode == 3):
            #RegisterNew(window)
            #TODO
    
        else:
            LibTk.Window.StrNotice('Error TskInstStepId selected a unsupported option.')
        return
def Wrapper(window):
    # This step require a reference step the following.
    # Once all the reference step were ture,
    #   the step will run. Ohterwize just move to the reference step.
    if(Wizard.WizardConditions.Modules.LibStepId is not True):
        from TskInstTheWizard import WizardSteps

        WizardSteps.LibStepId(window)
    else:
        Methods.DetectIdReference(window)
        idInstallMode = Wizard.WizardConditions.idInstallMode
        if(idInstallMode == 1):
            # Detect if auto display tutorial is true
            if Wizard.WizardConditions.autoTutorial:
                LibTk.Window.ArrayNotice(typeInStr.get('tutorialDialog'))

        LibTk.Window.ShowWindow(window)
    return