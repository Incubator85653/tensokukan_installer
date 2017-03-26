from tkinter import *
from LibTskInstString import TskInstStringStepDataImport as wizardCfg
import LibTskInstResources as LibRes
import TskInstTheWizard as wizard

DataImportYaml = LibRes.GuiYaml.get('TskInstStepUpgrade')
Part1Yaml = DataImportYaml.get('Part1')
Part2Yaml = DataImportYaml.get('Part2')
class ConstVars:
    installedPath = LibRes.Methods.Basic.InstallPath()

class Widgets:
    # Local variable
    entryStorageTskDbPath = StringVar()
    entryStorageIdYamlPath = StringVar()
    entryStorageSWRSAddrPath = StringVar()
    entryStorageTskIniPath = StringVar()

    checkbuttonStorageDntManageDb = IntVar()
    checkbuttonStorageDntManageId = IntVar()
    checkbuttonStorageDntManageSWRSAddr = IntVar()
    checkbuttonStorageChooseFromGameList = IntVar()
    # Widgets
    labelDisplayImportDataPart1 = None
    labelDisplayImportDataPart2 = None

    labelDisplayTskDbPath = None
    entryDisplayTskDbPath = None
    buttonDisplayBrowseDb = None
    checkbuttonDisplayDntManageDb = None

    labelDisplayIdYamlPath = None
    entryDisplayIdYamlPath = None
    buttonDisplayBrowseYaml = None
    checkbuttonDisplayDntManageId = None
    
    labelDisplaySWRSAddrPath = None
    entryDisplaySWRSAddrPath = None
    buttonDisplayBrowseSWRSAddr = None
    checkbuttonDisplayDntManageSWRSAddr = None
    checkbuttonDisplayChooseFromGameList = None

    labelDisplayTskIniPath = None
    entryDisplayTskIniPath = None
    buttonDisplayBrowseTskIni = None
    checkbuttonDisplayDntManageTskIni = None

    buttonDisplayNextStep = None
    buttonDisplayExit = None
class Methods:
    def InitialzieUpgradeProcess():

        return
    def MarkAsDone():
        wizard.WizardConditions.Modules.TskInstStepUpgrade = True
        return

    def PlaceWidgetsPart1():
        Widgets.labelDisplayImportDataPart1.place(x = Part1Yaml.get('labelDisplayImportDataPart1').get('x'),
                                                  y = Part1Yaml.get('labelDisplayImportDataPart1').get('y'))
        Widgets.labelDisplayTskIniPath.place(x = Part1Yaml.get('labelDisplayTskIniPath').get('x'),
                                                  y = Part1Yaml.get('labelDisplayTskIniPath').get('y'))
        Widgets.entryDisplayTskIniPath.place(x = Part1Yaml.get('entryDisplayTskIniPath').get('x'),
                                                  y = Part1Yaml.get('entryDisplayTskIniPath').get('y'))
        Widgets.buttonDisplayBrowseTskIni.place(x = Part1Yaml.get('buttonDisplayBrowseTskIni').get('x'),
                                                  y = Part1Yaml.get('buttonDisplayBrowseTskIni').get('y'))



        Widgets.buttonDisplayNextStep.place(x = Part1Yaml.get('buttonDisplayNextStep').get('x'),
                                            y = Part1Yaml.get('buttonDisplayNextStep').get('y'))
        Widgets.buttonDisplayExit.place(x = Part1Yaml.get('buttonDisplayExit').get('x'),
                                        y = Part1Yaml.get('buttonDisplayExit').get('y'))
        return
    def SaveButtonPart1(window):
        from LibTskInstString import TskInstStringErrors as errors
        def CopyBack():
            wizard.WizardConditions.Upgrade.TskIniPath = Widgets.entryStorageTskIniPath.get()
            wizard.WizardConditions.Unattended.UpgradeTskIni = True

            wizard.RootWindow.CleanWidgets(window)
            ConfigureWidgetsPart2(window)
            Methods.PlaceWidgetsPart2()
            window.mainloop()
            return

        tskIniPathBool = bool(Widgets.entryStorageTskIniPath.get())
        if(tskIniPathBool is False):
            LibTk.Window.PopupNotifaction(errors.errorTextTskIniEmpty)
        else:
            CopyBack()
        return

    def PlaceWidgetsPart2():
        import LibRes as cfg
        Widgets.labelDisplayImportDataPart2.place(x = Part2Yaml.get('labelDisplayImportData').get('x'),
                                             y = Part2Yaml.get('labelDisplayImportData').get('y'))

        Widgets.labelDisplayTskDbPath.place(x = Part2Yaml.get('labelDisplayTskDatabase').get('x'),
                                              y = Part2Yaml.get('labelDisplayTskDatabase').get('y'))
        Widgets.entryDisplayTskDbPath.place(x = Part2Yaml.get('entryDisplayTskDbPath').get('x'),
                                            y = Part2Yaml.get('entryDisplayTskDbPath').get('y'))
        Widgets.buttonDisplayBrowseDb.place(x = Part2Yaml.get('buttonDisplayBrowseDb').get('x'),
                                            y = Part2Yaml.get('buttonDisplayBrowseDb').get('y'))
        Widgets.checkbuttonDisplayDntManageDb.place(x = Part2Yaml.get('checkbuttonDisplayDntManageDb').get('x'),
                                                    y = Part2Yaml.get('checkbuttonDisplayDntManageDb').get('y'))

        Widgets.labelDisplayIdYamlPath.place(x = Part2Yaml.get('labelDisplayIdYaml').get('x'),
                                         y = Part2Yaml.get('labelDisplayIdYaml').get('y'))
        Widgets.entryDisplayIdYamlPath.place(x = Part2Yaml.get('entryDisplayIdYaml').get('x'),
                                         y = Part2Yaml.get('entryDisplayIdYaml').get('y'))
        Widgets.buttonDisplayBrowseYaml.place(x = Part2Yaml.get('buttonDisplayBrowseYaml').get('x'), 
                                              y = Part2Yaml.get('buttonDisplayBrowseYaml').get('y'))
        Widgets.checkbuttonDisplayDntManageId.place(x = Part2Yaml.get('checkbuttonDisplayDntManageId').get('x'), 
                                                    y = Part2Yaml.get('checkbuttonDisplayDntManageId').get('y'))
    
        Widgets.labelDisplaySWRSAddrPath.place(x = Part2Yaml.get('labelDisplaySWRSAddr').get('x'),
                                           y = Part2Yaml.get('labelDisplaySWRSAddr').get('y'))
        Widgets.entryDisplaySWRSAddrPath.place(x = Part2Yaml.get('entryDisplaySWRSAddrPath').get('x'), 
                                               y = Part2Yaml.get('entryDisplaySWRSAddrPath').get('y'))
        Widgets.buttonDisplayBrowseSWRSAddr.place(x = Part2Yaml.get('buttonDisplayBrowseSWRSAddr').get('x'), 
                                                  y = Part2Yaml.get('buttonDisplayBrowseSWRSAddr').get('y'))
        Widgets.checkbuttonDisplayDntManageSWRSAddr.place(x = Part2Yaml.get('checkbuttonDisplayDntManageSWRSAddr').get('x'), 
                                                          y = Part2Yaml.get('checkbuttonDisplayDntManageSWRSAddr').get('y'))
        Widgets.checkbuttonDisplayChooseFromGameList.place(x = Part2Yaml.get('checkbuttonDisplayChooseFromGameList').get('x'), 
                                                           y = Part2Yaml.get('checkbuttonDisplayChooseFromGameList').get('y'))
        # Next step and exit
        Widgets.buttonDisplayNextStep.place(x = Part2Yaml.get('buttonDisplayNextStep').get('x'),
                                            y = Part2Yaml.get('buttonDisplayNextStep').get('y'))
        Widgets.buttonDisplayExit.place(x = Part2Yaml.get('buttonDisplayExit').get('x'),
                                        y = Part2Yaml.get('buttonDisplayExit').get('y'))


        return
    def SaveButtonPart2():
        from LibTskInstString import TskInstStringErrors as errors
        def CopyBack(SwrsUpgradeMode):
            if(bool(Widgets.checkbuttonStorageDntManageDb.get()) is False):
                wizard.WizardConditions.Unattended.UpgradeDatabase = True
            if(bool(Widgets.checkbuttonStorageDntManageId.get()) is False):
                wizard.WizardConditions.Unattended.UpgradeIdYaml = True
            if(bool(Widgets.checkbuttonStorageDntManageSWRSAddr.get()) is False):
                wizard.WizardConditions.Unattended.UpgradeSWRSAddr = True
            if(SwrsUpgradeMode == 2):
                wizard.WizardConditions.Upgrade.SwrsUpgradeMode = 2
            else:
                wizard.WizardConditions.Upgrade.SwrsUpgradeMode = 1

            wizard.WizardConditions.Upgrade.DatabasePath = Widgets.entryStorageTskDbPath.get()
            wizard.WizardConditions.Upgrade.ReportYamlPath = Widgets.entryStorageIdYamlPath.get()
            wizard.WizardConditions.Upgrade.SwrsPath = Widgets.entryStorageSWRSAddrPath.get()
            return
        def SwrsUpgradeMode():
            # Upgrade by copy
            mode = 1
            # Upgrade by unpack from list
            if(bool(Widgets.checkbuttonStorageChooseFromGameList.get())):
                mode = 2
            return mode

        databasePathBool = bool(Widgets.entryStorageTskDbPath.get())
        idYamlPathBool = bool(Widgets.entryStorageIdYamlPath.get())
        swrsBool = bool(Widgets.entryStorageSWRSAddrPath.get())

        swrsFromListBool = bool(Widgets.checkbuttonStorageChooseFromGameList.get())
        dntDatabase = bool(Widgets.checkbuttonStorageDntManageDb.get())
        dntIdYaml = bool(Widgets.checkbuttonStorageDntManageId.get())
        dntSwrs = bool(Widgets.checkbuttonStorageDntManageSWRSAddr.get())

        upgradeDatabase = not bool(Widgets.checkbuttonStorageDntManageDb.get())
        upgradeIdYaml = not bool(Widgets.checkbuttonStorageDntManageId.get())
        upgradeSwrsaddr = not bool(Widgets.checkbuttonStorageDntManageSWRSAddr.get())
        # Tell installer if user selected skip, then skip those settings
        if(dntDatabase):
            databasePathBool = True
            wizard.WizardConditions.Unattended.ManageDatabase = False
        if(dntIdYaml):
            idYamlPathBool = True
            wizard.WizardConditions.Unattended.ManageId = False
        if(dntSwrs):
            swrsBool = True
            wizard.WizardConditions.Unattended.ManageSWRSAddr = False
        # Otherwize, save settings.
        if(upgradeDatabase and databasePathBool is False):
            LibTk.Window.PopupNotifaction(errors.errorTextDatabasePathEmpty)
        elif(upgradeIdYaml and idYamlPathBool is False):
            LibTk.Window.PopupNotifaction(errors.errorTextIdUpgradeYamlEmpty)
        elif(upgradeSwrsaddr and swrsBool is False and swrsFromListBool is False):
            LibTk.Window.PopupNotifaction(errors.errorTextSWRSAddrPathEmpty)
        elif(upgradeSwrsaddr and swrsFromListBool):
            wizard.WizardConditions.Modules.TskInstStepGame = False
            CopyBack(SwrsUpgradeMode())
            Methods.MarkAsDone()
            wizard.TimeLine.BackFromAnyModule()
        else:
            CopyBack(SwrsUpgradeMode())
            Methods.MarkAsDone()
            wizard.TimeLine.BackFromAnyModule()
        return

def ConfigureWidgetsPart1(window):
    # part 4 import tsk.ini
    Widgets.labelDisplayImportDataPart1 = Label(window,
                                                text = wizardCfg.labelTextImportDataPart1)
    Widgets.labelDisplayTskIniPath = Label(window,
                                           text = wizardCfg.labelTextTskIni)
    Widgets.entryDisplayTskIniPath = Entry(window,
                                           textvariable = Widgets.entryStorageTskIniPath)
    Widgets.buttonDisplayBrowseTskIni = Button(window,
                                               text = wizardCfg.buttonTextBrowseTskIni,
                                               command = '')
    # Control widgets
    Widgets.buttonDisplayNextStep = Button(window,
                                               text = wizardCfg.buttonTextNextStep,
                                               command = lambda : Methods.SaveButtonPart1(window))
    Widgets.buttonDisplayExit = Button(window,
                                           text = wizardCfg.buttonTextExit,
                                           command = lambda : wizard.RootWindow.ExitWizard())
    return
def ConfigureWidgetsPart2(window):
    #part1 Title and Database
    Widgets.labelDisplayImportDataPart2 = Label(window,
                                           text = wizardCfg.labelTextImportDataPart2)
    Widgets.labelDisplayTskDbPath = Label(window,
                                            text = wizardCfg.labelTextTskDatabase)
    Widgets.entryDisplayTskDbPath = Entry(window,
                                          textvariable = Widgets.entryStorageTskDbPath)
    Widgets.buttonDisplayBrowseDb = Button(window,
                                           text = wizardCfg.buttonTextBrowseDb,
                                           command = '')#TODO
    Widgets.checkbuttonDisplayDntManageDb = Checkbutton(window,
                                                        text = wizardCfg.checkbuttonTextDntManageDb,
                                                        variable = Widgets.checkbuttonStorageDntManageDb)
    #part2 ID yaml
    Widgets.labelDisplayIdYamlPath = Label(window,
                                       text = wizardCfg.labelTextIdYaml)
    Widgets.entryDisplayIdYamlPath = Entry(window,
                                       textvariable = Widgets.entryStorageIdYamlPath)
    Widgets.buttonDisplayBrowseYaml = Button(window,
                                             text = wizardCfg.buttonTextBrowseYaml,
                                             command = '')#TODO
    Widgets.checkbuttonDisplayDntManageId = Checkbutton(window,
                                                        text = wizardCfg.checkbuttonTextDntManageId,
                                                        variable = Widgets.checkbuttonStorageDntManageId)
    #part3 Game support
    Widgets.labelDisplaySWRSAddrPath = Label(window,
                                         text = wizardCfg.labelTextSWRSAddr)
    Widgets.entryDisplaySWRSAddrPath = Entry(window,
                                             textvariable = Widgets.entryStorageSWRSAddrPath)
    Widgets.buttonDisplayBrowseSWRSAddr = Button(window,
                                                 text = wizardCfg.buttonTextBrowseSWRSAddr,
                                                 command = '')#TODO
    Widgets.checkbuttonDisplayDntManageSWRSAddr = Checkbutton(window,
                                                              text = wizardCfg.checkbuttonTextDntSWRSAddr,
                                                              variable = Widgets.checkbuttonStorageDntManageSWRSAddr)
    Widgets.checkbuttonDisplayChooseFromGameList = Checkbutton(window,
                                                               text = wizardCfg.checkbuttonTextChooseFromGameList,
                                                               variable = Widgets.checkbuttonStorageChooseFromGameList)


    Widgets.buttonDisplayNextStep = Button(window,
                                               text = wizardCfg.buttonTextSave,
                                               command = lambda : Methods.SaveButtonPart2())
    Widgets.buttonDisplayExit = Button(window,
                                           text = wizardCfg.buttonTextExit,
                                           command = lambda : wizard.RootWindow.ExitWizard())


    return

def Wrapper(window):
    ConfigureWidgetsPart1(window)
    Methods.PlaceWidgetsPart1()
    #ConfigureWidgetsPart2(window)
    #Methods.PlaceWidgetsPart2()
    window.mainloop()
    return