from tkinter import *
from LibTskInstString import TskInstStringStepInstalling as wizardCfg
import TskInstTheWizard as wizard

class Widgets:
    #local variable
    entryStorageCurrentStatusBar = StringVar()
    entryStorageTotalStatusBar = StringVar()
    # a bool value used to disable running update loop
    # the loop running per 0.25 second
    updateLoopSwitch = True

    # widgets
    labelDisplayInstallingTensokukan = None

    labelDisplayCurrentStatus = None
    #labelTextCurrentOperate = None

    labelDisplayTotalStatus = None
    #labelTextTotalOperate = None

    entryDisplayCurrentStatusBar = None
    entryDisplayTotalStatusBar = None
class Methods:
    def Add1S(life, progress):
        if progress == 0.0:
            life.set('')
        elif progress == 0.1:
            life.set('+1S')
        elif progress == 0.2:
            life.set('+1S+1S')
        elif progress == 0.3:
            life.set('+1S+1S+1S')
        elif progress == 0.4:
            life.set('+1S+1S+1S+1S')
        elif progress == 0.5:
            life.set('+1S+1S+1S+1S+1S')
        elif progress == 0.6:
            life.set('+1S+1S+1S+1S+1S+1S')
        elif progress == 0.7:
            life.set('+1S+1S+1S+1S+1S+1S+1S')
        elif progress == 0.8:
            life.set('+1S+1S+1S+1S+1S+1S+1S+1S')
        elif progress == 0.9:
            life.set('+1S+1S+1S+1S+1S+1S+1S+1S+1S')
        elif progress == 1.0:
            life.set('+1S+1S+1S+1S+1S+1S+1S+1S+1S+1S')
        return
    def UpdateLoop(window):
        def Fuse(window):
            if(Widgets.updateLoopSwitch):
                window.update()
            return

        if(Widgets.updateLoopSwitch):
            window.after(100, lambda : Fuse(window))
        return
    def StartInstall(window):
        def UpdateLabel(object, input):
            object['text'] = input
            return

        from LibTskInstPython import Second2Millisecond as s2s
        window.after(s2s(0),
                     lambda : UpdateLabel(Widgets.labelDisplayTotalOperate,
                                 wizardCfg.labelTotalOperationCheckDir))
        window.after(s2s(0),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationPreprocessing))
        window.after(s2s(2),
                     lambda : UpdateLabel(Widgets.labelDisplayTotalOperate,
                                          wizardCfg.labelTotalOperationInstalling))
        window.after(s2s(2),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationUnpackingProgram))
        window.after(s2s(2),
                      lambda : Methods.Add1S(Widgets.entryStorageTotalStatusBar, 0.1))
        window.after(s2s(4),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationInstallUpdate))
        window.after(s2s(4),
                     lambda : Methods.Add1S(Widgets.entryStorageTotalStatusBar, 0.2))
        window.after(s2s(6),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationSaveSettings))
        window.after(s2s(6),
                     lambda : Methods.Add1S(Widgets.entryStorageTotalStatusBar, 0.4))
        window.after(s2s(8),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationSetProgramVer))
        window.after(s2s(8),
                     lambda : Methods.Add1S(Widgets.entryStorageTotalStatusBar, 0.6))
        window.after(s2s(10),
                     lambda : UpdateLabel(Widgets.labelDisplayCurrentOperate,
                                          wizardCfg.labelOperationDone))
        window.after(s2s(10),
                     lambda : UpdateLabel(Widgets.labelDisplayTotalOperate,
                                          wizardCfg.labelOperationDone))
        window.after(s2s(10),
                     lambda : Methods.Add1S(Widgets.entryStorageTotalStatusBar, 1.0))
        window.after(s2s(10),
                     lambda : Widgets.entryStorageCurrentStatusBar.set(wizardCfg.readPoetry))

        return
def ConfigureWidgets(window):
    #TODO
    #label
    Widgets.labelDisplayInstallingTensokukan = Label(window,
                                         text = wizardCfg.labelTitleInstalling)
    Widgets.labelDisplayCurrentStatus = Label(window,
                                           text = wizardCfg.labelTitleCurrentStatus)
    Widgets.labelDisplayCurrentOperate = Label(window,
                                            text = '')
    Widgets.labelDisplayTotalStatus = Label(window,
                                          text = wizardCfg.labelTitleTotalStatus)
    Widgets.labelDisplayTotalOperate = Label(window,
                                          text = '')
    #entry
    Widgets.entryDisplayCurrentStatusBar = Entry(window,
                                                 textvariable = Widgets.entryStorageCurrentStatusBar,
                                                 state = DISABLED,
                                                 width = 34)
    Widgets.entryDisplayTotalStatusBar = Entry(window,
                                               textvariable = Widgets.entryStorageTotalStatusBar,
                                               state = DISABLED,
                                               width = 34)
    # place GUI object
    # TODO
    # add x and y.
    Widgets.labelDisplayInstallingTensokukan.place(x = 25, y = 25)
    Widgets.labelDisplayCurrentStatus.place(x = 45, y = 55)
    Widgets.labelDisplayCurrentOperate.place(x = 45, y = 85)
    Widgets.entryDisplayCurrentStatusBar.place(x = 55, y = 115)

    Widgets.labelDisplayTotalStatus.place(x = 45, y = 145)
    Widgets.labelDisplayTotalOperate.place(x = 45, y = 175)
    Widgets.entryDisplayTotalStatusBar.place(x = 55, y = 205)
    return
def Wrapper(window):
    ConfigureWidgets(window)
    Methods.UpdateLoop(window)
    Methods.StartInstall(window)
    window.mainloop()
    #wizard.TimeLine.BackFromAnyModule()
    return