import LibTkinter as LibTk
import LibInstallProfile as LibProfile

from tkinter import *
from tkinter import ttk
from LibPython import Environment as Env
from LibPython import UnitConversion as Unit
from LibOperate import WaterWellsYaml as wwYaml
from LibInstallProfile import DecodedProfile

class RootVar:
    # Tk()
    bootstrapGui = None
    bootstrapGuiProp = None
    # String dictionary based on system language.
    bootStringDict = None

class Widgets:
    # Local variables, fill by InitalizeWidgetsProp
    comboboxStorageWizardLang = None
    comboboxStorageWizardLangList = None

    comboboxStorageTskLang = None
    comboboxStorageTskLangList = None
    # Widgets
    labelWizardLang = None
    labelWizardLangIntro = None
    logoWizardLang = None
    comboboxWizardLang = None

    labelTskLang = None
    labelTskLangIntro = None
    logoTskLang = None
    comboboxWizardLang = None

    buttonNext = None
    buttonExit = None

class Methods:
    class Initialize:
        # Return a language specified string dictionary for the bootstrap
        # interface.
        # If the system language is not supported by project, return en-US
        # as default language dictionary.
        def GetBootString():
            sysLang = Env.System.GetSysShortLang()
            supportedLangArray = LibProfile.BootstrapLanguage['SupportedLanguages']

            if sysLang in supportedLangArray:
                bootString = LibProfile.BootstrapString.get(sysLang)
            else:
                bootString = LibProfile.BootstrapString.get('en_US')

            return bootString

        def InitalizeBootRes():
            try:
                LibProfile.BootstrapLanguage = wwYaml.read_yaml_from_disk('BootstrapLanguage.yaml')
                LibProfile.BootstrapLocale = wwYaml.read_yaml_from_disk('BootstrapLocale.yaml')
                LibProfile.BootstrapPath = wwYaml.read_yaml_from_disk('BootstrapPath.yaml')
                LibProfile.BootstrapString = wwYaml.read_yaml_from_disk('BootstrapString.yaml')
                LibProfile.RawProfileDict = wwYaml.read_yaml_from_disk('BootstrapBlankProfile.yaml')
            except Exception as e:
                from LibPython import Process
                Process.handle_exception(e, True)
                sys.exit(-5)

        def InitalizeSelf():
            # Set bootstrap gui string dictionary, based on language.
            RootVar.bootStringDict = Methods.Initialize.GetBootString()

            # Create a window for bootstrap interface.
            RootVar.bootstrapGui = Tk()
            # Hide.
            # Display again after initialize.
            # Well, show this window when it is needed.
            #Methods.LoadingScreen.bootstrapGui.deiconify()
            RootVar.bootstrapGui.withdraw()

            # Initalize window properties.
            RootVar.bootstrapGuiProp = LibProfile.BootstrapString['Universal']
            LibTk.Window.InitializeWindow(RootVar.bootstrapGui, RootVar.bootstrapGuiProp)

        def ConfigureWidgets():
            Widgets.comboboxStorageWizardLang = StringVar()
            Widgets.comboboxStorageWizardLangList = LibProfile.BootstrapLanguage['WizardLanguages']

            Widgets.comboboxStorageTskLang = StringVar()
            Widgets.comboboxStorageTskLangList = LibProfile.BootstrapLanguage['TskLanguages']

        def Wrapper():
            Methods.Initialize.InitalizeBootRes()
            Methods.Initialize.InitalizeSelf()
            Methods.Initialize.ConfigureWidgets()

    class LanguageSelect:
        def FillPathsBackToLibProfile():
            # This method in bootstrap, it fill a language based resource path for installer.
            foldersDict = LibProfile.BootstrapPath['Folders']
            filesDict = LibProfile.BootstrapPath['Files']

            # Get root resources directory name.
            resourcesDirName = foldersDict['Resources']
            workingResourcesPath = Env.Path.merge_path_with_work_dir(resourcesDirName)

            # Generage language based root resource path(full path).
            langBasedRootResourcesPath = Env.Path.merge_system(workingResourcesPath, LibProfile.Language.WizardDevLanguage)

            langBasedWizardResPath = Env.Path.merge_system(workingResourcesPath, LibProfile.Language.WizardDevLanguage)
            langBasedWizardBinPath = Env.Path.merge_system(workingResourcesPath, LibProfile.Language.WizardBinLanguage)
            langBasedTskResPath = Env.Path.merge_system(workingResourcesPath, LibProfile.Language.TskDevLanguage)

            # Generate language based sub resource folder name and path by root resource path(full path).
            archiveDirName = foldersDict['Archive']
            binDirName = foldersDict['Bin']
            configDirName = foldersDict['Config']
        
            langBasedArchiveDirPath = Env.Path.merge_system(langBasedTskResPath, archiveDirName)
            langBasedBinDirPath = Env.Path.merge_system(langBasedWizardBinPath, binDirName)
            langBasedConfigDirPath = Env.Path.merge_system(langBasedWizardResPath, configDirName)

            # Generate binary file path by language based sub resource path(full path).
            zipBinName = filesDict['Bin']['7za']
            editorBinName = filesDict['Bin']['BatchEditor']
            
            langBasedzipBinName = Env.Path.merge_system(langBasedBinDirPath, zipBinName)
            langBasedEditorBinName = Env.Path.merge_system(langBasedBinDirPath, editorBinName)

            # Generate installer configs file path by language based...
            debugOptionsName = filesDict['Config']['DebugOptions']
            archiveYamlName = filesDict['Config']['Archive']
            gamesYamlName = filesDict['Config']['Games']
            BatchEditorYamlName = filesDict['Config']['BatchEditor']
            structureYamlName = filesDict['Config']['Structure']
            stringYamlName = filesDict['Config']['String']
            tkinterYamlName = filesDict['Config']['Tkinter']

            langBasedDebugOptionsYamlPath = Env.Path.merge_system(langBasedConfigDirPath, debugOptionsName)
            langBasedArchiveYamlPath = Env.Path.merge_system(langBasedConfigDirPath, archiveYamlName)
            langBasedGamesYamlPath = Env.Path.merge_system(langBasedConfigDirPath, gamesYamlName)
            langBasedBatchEditorYamlPath = Env.Path.merge_system(langBasedConfigDirPath, BatchEditorYamlName)
            langBasedStructureYamlPath = Env.Path.merge_system(langBasedConfigDirPath, structureYamlName)
            langBasedStringYamlPath = Env.Path.merge_system(langBasedConfigDirPath, stringYamlName)
            langBasedTkinterYamlPath = Env.Path.merge_system(langBasedConfigDirPath, tkinterYamlName)

            # Fill final results back to LibProfile.

            LibProfile.RawProfileDict['Installer']['Archive']['Source'] = langBasedArchiveDirPath

            LibProfile.RawProfileDict['Installer']['Bin']['7-zip'] = langBasedzipBinName
            LibProfile.RawProfileDict['Installer']['Bin']['BatchEditor'] = langBasedEditorBinName
            
            LibProfile.RawProfileDict['Installer']['ConfigPath']['DebugOptions'] = langBasedDebugOptionsYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['Archive'] = langBasedArchiveYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['Games'] = langBasedGamesYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['BatchEditor'] = langBasedBatchEditorYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['Structure'] = langBasedStructureYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['String'] = langBasedStringYamlPath
            LibProfile.RawProfileDict['Installer']['ConfigPath']['Tkinter'] = langBasedTkinterYamlPath
            # Plz run Yaml loader(loading screen) after fill language based resources path.
         
        def DetectSupportedLang():
            from LibPython import Environment as Env

            supportedLangArray = LibProfile.BootstrapLanguage['SupportedLanguages']
            sysDevLang = Env.System.GetSysShortLang()
        
            if sysDevLang in supportedLangArray:
                LibTk.Window.SafeDestroy(RootVar.bootstrapGui)
                LibProfile.Language.WizardDevLanguage = sysDevLang
                LibProfile.Language.TskDevLanguage = sysDevLang

                # Code to force enable such language, for debug use.
                #LibProfile.Language.WizardDevLanguage = 'zh-CN'
                #LibProfile.Language.TskDevLanguage = 'zh-CN'
                
                Methods.LanguageSelect.FillPathsBackToLibProfile()
            else:
                Methods.LanguageSelect.ConfigureWidgets(RootVar.bootstrapGui)
                RootVar.bootstrapGui.deiconify()
                LibTk.Window.ShowWindow(RootVar.bootstrapGui)

        def ConfigureWidgets(window):
            Widgets.labelWizardLang = Label(window,
                                            justify = LEFT,
                                            text = RootVar.bootStringDict['labelWizardLang'])
            Widgets.labelWizardLangIntro = Label(window,
                                                 justify = LEFT,
                                                 text = Unit.FormatArray2String(
                                                     RootVar.bootStringDict['labelWizardLangIntro']))
            Widgets.comboboxWizardLang = ttk.Combobox(window,
                                                      state = 'readonly',
                                                      textvariable = Widgets.comboboxStorageWizardLang,
                                                      values = Widgets.comboboxStorageWizardLangList,
                                                      width = 60)
            Widgets.labelTskLang = Label(window,
                                         justify = LEFT,
                                         text = RootVar.bootStringDict['labelTskLang'])
            Widgets.labelTskLangIntro = Label(window,
                                              justify = LEFT,
                                              text = Unit.FormatArray2String(RootVar.bootStringDict['labelTskLangIntro']),
                                              wraplength = 500)
            Widgets.comboboxTskLang = ttk.Combobox(window,
                                                          state = 'readonly',
                                                          textvariable = Widgets.comboboxStorageTskLang,
                                                          values = Widgets.comboboxStorageTskLangList,
                                                          width = 60)

            Widgets.buttonNext = Button(window,
                                        text = RootVar.bootStringDict['nextStepButton'],
                                        command = lambda : Methods.LanguageSelect.NextStep_SaveSettings(),
                                        width = 10)
            Widgets.buttonExit = Button(window,
                                        text = RootVar.bootStringDict['exitButton'],
                                        command = lambda : LibTk.Window.ExitWizard(),
                                        width = 10)

            Widgets.labelWizardLang.place(x = 25, y = 25)
            Widgets.labelWizardLangIntro.place(x = 55, y = 55)
            Widgets.comboboxWizardLang.place(x = 95, y = 115)
            Widgets.labelTskLang.place(x = 25, y = 155)
            Widgets.labelTskLangIntro.place(x = 55, y = 185)
            Widgets.comboboxTskLang.place(x = 95, y = 275)

            Widgets.buttonNext.place(x = 450, y = 430)
            Widgets.buttonExit.place(x = 540, y = 430)

        def SetLangAndCopyBack():
            from LibInstallProfile import BootstrapLocale

            wizardLang = Widgets.comboboxStorageWizardLang.get()
            tskLang = Widgets.comboboxStorageTskLang.get()
            convertDict = BootstrapLocale['DisplayLang2DevLang']

            wizardDevLang = convertDict[wizardLang]
            tskDevLang = convertDict[tskLang]

            LibProfile.Language.WizardDevLanguage = wizardDevLang
            LibProfile.Language.TskDevLanguage = tskDevLang

            # A safe destroy method to prevent error
            # can't invoke "winfo" command:  application has been destroyed
            RootVar.bootstrapGui.eval('::ttk::CancelRepeat')
            RootVar.bootstrapGui.destroy()

            Methods.LanguageSelect.FillPathsBackToLibProfile()

        def NextStep_SaveSettings():
            boolWizardLang = bool(Widgets.comboboxStorageWizardLang.get())
            boolTskLang = bool(Widgets.comboboxStorageTskLang.get())

            if boolWizardLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict['errorWizardLangEmpty'])
            elif boolTskLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict['errorTskLangEmpty'])
            else:
                Methods.LanguageSelect.SetLangAndCopyBack()  

        def Wrapper():
            Methods.LanguageSelect.DetectSupportedLang()

    class LoadingScreen:
        def ReadConfigFromDisk():
            from LibOperate import WaterWellsYaml as wwYaml
            from LibInstallProfile import RawProfileDict
            from LibInstallProfile import DecodedProfile

            # Read yaml files from disk
            try:
                DecodedProfile.Config.DebugYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['DebugOptions'])
                DecodedProfile.Config.ArchiveYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['Archive'])
                DecodedProfile.Config.GamesYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['Games'])
                DecodedProfile.Config.BatchEditorYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['BatchEditor'])
                DecodedProfile.Config.StructureYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['Structure'])
                DecodedProfile.Config.StringYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['String'])
                DecodedProfile.Config.TkinterYaml = wwYaml.read_yaml_from_disk(RawProfileDict['Installer']['ConfigPath']['Tkinter'])
            except Exception as e:
                from LibPython import Process
                Process.handle_exception(e, True)
                sys.exit(-4)

        def FillVarFromConfig():
            from LibInstallProfile import RawProfileDict
            from LibInstallProfile import DecodedProfile

            # Add Archive Collection Array
            # This Array will be use in a "for" method,
            # design for shortest code to unpack the archives.
            RawProfileDict['Installer']['Archive']['Collection'] = DecodedProfile.Config.ArchiveYaml['Collection']

            # Add optional installer options.
            RawProfileDict['Installer']['Optional']['ProgramStructure'] = DecodedProfile.Config.StructureYaml['Program']

        def DoLoadConfig(window):
            from LibPython import Process

            import LibInstallProfile as LibProfile
            Methods.LoadingScreen.ReadConfigFromDisk()
            Methods.LoadingScreen.FillVarFromConfig()

            # End bootstrap and loading screen.
            from LibTkinter import Window as LibTkWin
            LibTkWin.SafeDestroy(window)

        def TheLoadingScreen():
            import tkinter
            import LibTkinter as LibTk

            TkLoadingScreen = tkinter.Tk()
            propDict = {'Geometry':'400x100',    'Title':'Tensokukan Tsk Installer'}
            LibTk.Window.InitializeWindow(TkLoadingScreen, propDict)

            Lable = tkinter.Label(TkLoadingScreen,
                                  text = 'Initalizing Installer...\nThis will take a few seconds.',
                                  justify = tkinter.LEFT)
            Lable.place(x = 25, y = 25)

            TkLoadingScreen.after(Unit.Second2Millisecond(1),
                                  lambda : Methods.LoadingScreen.DoLoadConfig(TkLoadingScreen))
            LibTk.Window.ShowWindow(TkLoadingScreen)

        def Wrapper():
            Methods.LoadingScreen.TheLoadingScreen()


def Wrapper():
    try:
        Methods.Initialize.Wrapper()
        Methods.LanguageSelect.Wrapper()
        Methods.LoadingScreen.Wrapper()
    except Exception as e:
        from LibPython import Process
        Process.handle_exception(e, True)
        sys.exit(-3)