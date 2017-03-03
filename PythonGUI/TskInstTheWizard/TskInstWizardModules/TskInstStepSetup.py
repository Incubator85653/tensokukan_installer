import TskInstTheWizard as Wizard
import LibTskInstResources as LibRes
import LibTskInstTkinter as LibTk
from tkinter import *

wizardCfg = LibRes.Resources.Config.StringYaml.get('TskInstStepInstall')

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
    def ExitButton():
        LibTk.Window.ExitWizard()
        return
    def StartInstall(window):
        import LibTskInstSetup as LibSetup
        
        # Display Installing hint.
        Widgets.labelStorageInstalling.set(wizardCfg['labelTextInstalling'])

        # Hide Start Button and Do install.
        LibTk.Window.UnivWizardController_Hide(window, Widgets.buttonStartInstall)

        LibSetup.Wrapper_NewInstall()
        
        # Show a short hint after install completed.
        Widgets.labelStorageInstalling.set(wizardCfg['labelTextDone'])
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
        return


def Wrapper(window):
    Methods.ConfigureWidgets(window)
    LibTk.Window.ShowWindow(window)
    return