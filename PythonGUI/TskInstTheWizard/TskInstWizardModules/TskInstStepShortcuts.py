import TskInstTheWizard as Wizard
import LibTkinter as LibTk
from LibInstallProfile import RawProfileDict
from LibInstallProfile import DecodedProfile
from LibPython import Environment as Env
from tkinter import *

wizardStr = DecodedProfile.Config.StringYaml['TskInstStepShortcuts']

defaultTskStartMenuGroupName = DecodedProfile.Methods.Optional.Structure.Shortcuts.StartupMenuGroup()
defaultTskMainShortcutName = DecodedProfile.Methods.Optional.Structure.Shortcuts.TskMainLnk()

class Widgets:
    # local variables
    # name rule: entry+Verb + Startup menu/Desktop + Noun
    # dnt = Do not
    entryStorageStartMenuName = StringVar()
    entryStorageTskMainName = StringVar()

    checkbuttonStorageDntStartMenu = IntVar()
    checkbuttonStorageDntDesktop = IntVar()

    labelTitleCreateShortcuts = None
    labelTextCreateStartMenu = None
    labelTextCreateDesktop = None

    entryDisplayStartMenuName = None
    entryDisplayDesktopName = None

    checkbuttonDisplayDntstartMenu = None
    checkbuttonDisplayDntDesktop = None

    buttonSave = None
    buttonExit = None
    buttonResetDefaultNames = None
class Methods:
    def MarkAsDone():
        Wizard.WizardConditions.Modules.TskInstStepShortcuts = True
        return
    def ResetDefaultNamesButton():
        Widgets.entryStorageStartMenuName.set(defaultTskStartMenuGroupName)
        Widgets.entryStorageTskMainName.set(defaultTskMainShortcutName)
        return
    def CopyBack():
        from os import path

        sysStartMenuPath = Env.System.GetSysStartupMenuPath()
        sysDesktopPath = Env.System.GetSysDesktopPath()

        tskStartMenuGroupName = Widgets.entryStorageStartMenuName.get()
        tskDesktopName = Widgets.entryStorageTskMainName.get()

        RawProfileDict['Basic']['StartMenuGroup'] = tskStartMenuGroupName
        RawProfileDict['Basic']['DesktopShortcut'] = tskDesktopName + '.lnk'

        # GUI shows "Do not create", so use the not keyword.
        RawProfileDict['Unattended']['ManageStartMenuShortcut'] = not bool(Widgets.checkbuttonStorageDntStartMenu.get())
        RawProfileDict['Unattended']['ManageDesktopShortcut'] = not bool(Widgets.checkbuttonStorageDntDesktop.get())

        Methods.MarkAsDone()
        Wizard.TimeLine.BackFromAnyModule()
        return
    def SaveButton():
        # create some variable copy
        entryStorageStartMenuNameBool = bool(Widgets.entryStorageStartMenuName.get())
        entryStorageDesktopNameBool = bool(Widgets.entryStorageTskMainName.get())
        checkbuttonTextDntstartMenuBool = bool(Widgets.checkbuttonStorageDntStartMenu.get())
        checkbuttonTextDntDesktopBool = bool(Widgets.checkbuttonStorageDntDesktop.get())
        # check and force variable copy is True if needed
        # "needed" means if user selected "do not copy" check box,
        # corresponding variable copy is force to True.
        if(checkbuttonTextDntstartMenuBool):
            entryStorageStartMenuNameBool = True
        if(checkbuttonTextDntDesktopBool):
            entryStorageDesktopNameBool = True
        # passed entry not empty test.
        # This test is required, you never don't know what happen if a user delete the value in the entry.
        if(entryStorageStartMenuNameBool is False):
            LibTk.Window.StrNotice(wizardStr.get('errorStartMenuDirEmpty'))
        elif(entryStorageDesktopNameBool is False):
            LibTk.Window.StrNotice(wizardStr.get('errorDesktopNameEmpty'))
        else:
            Methods.CopyBack()
        return
    def ConfigureWidgets(window):
        #lable
        Widgets.labelTitleCreateShortcuts = Label(window,
                                                  text = wizardStr.get('labelTitleCreateShortcuts'))
        Widgets.labelTextCreateStartMenu = Label(window,
                                                 text = wizardStr.get('labelTextCreateStartMenu'))
        Widgets.labelTextCreateDesktop = Label(window,
                                               text = wizardStr.get('labelTextCreateDesktop'))
        #entry
        Widgets.entryDisplayStartMenuName = Entry(window,
                                                  textvariable = Widgets.entryStorageStartMenuName,
                                                  width = 40)
        Widgets.entryDisplayDesktopName = Entry(window,
                                                textvariable = Widgets.entryStorageTskMainName,
                                                width = 40)
        #default entry contents
        Widgets.entryStorageStartMenuName.set(defaultTskStartMenuGroupName)
        Widgets.entryStorageTskMainName.set(defaultTskMainShortcutName)
        #checkbutton
        Widgets.checkbuttonDisplayDntstartMenu = Checkbutton(window,
                                                            text = wizardStr.get('checkbuttonTextDntstartMenu'),
                                                            variable = Widgets.checkbuttonStorageDntStartMenu)
        Widgets.checkbuttonDisplayDntDesktop = Checkbutton(window,
                                                        text = wizardStr.get('checkbuttonTextDntDesktop'),
                                                        variable = Widgets.checkbuttonStorageDntDesktop)
        #button
        Widgets.buttonSave = Button(window,
                                    text = wizardStr.get('buttonSave'),
                                    command = lambda : Methods.SaveButton(),
                                    width = 10)
        Widgets.buttonResetDefaultNames = Button(window,
                                                 text = wizardStr.get('buttonResetDefaultNames'),
                                                 command = lambda : Methods.ResetDefaultNamesButton())

        # place GUI objects
        Widgets.labelTitleCreateShortcuts.place(x = 25, y = 25)
        Widgets.labelTextCreateStartMenu.place(x = 25, y = 85)
        Widgets.entryDisplayStartMenuName.place(x = 45, y = 115)

        Widgets.labelTextCreateDesktop.place(x = 25, y = 145)
        Widgets.entryDisplayDesktopName.place(x = 45, y = 175)

        Widgets.checkbuttonDisplayDntstartMenu.place(x = 25, y = 215)
        Widgets.checkbuttonDisplayDntDesktop.place(x = 25, y = 245)

        LibTk.Window.UnivWizardController_Place(window, Widgets.buttonSave)
        Widgets.buttonResetDefaultNames.place(x = 25, y = 285)
        return
def Wrapper(window):
    Methods.ConfigureWidgets(window)
    LibTk.Window.ShowWindow(window)
    return