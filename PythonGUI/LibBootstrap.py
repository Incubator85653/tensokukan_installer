import LibTkinter as LibTk
import LibResources as LibRes

from tkinter import *
from tkinter import ttk
from LibPython import Environment as Env
from LibPython import UnitConversion as Unit
from LibOperate import WaterWellsYaml as wwYaml

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
            import sys
            sysLang = Env.System.GetSysShortLang(LibRes.BootstrapLocale['CodePage2ShortLang'])
            supportedLangArray = LibRes.BootstrapLanguage['SupportedLanguages']

            if sysLang in supportedLangArray:
                bootString = LibRes.BootstrapString.get(sysLang)
            else:
                bootString = LibRes.BootstrapString.get('en-US')

            return bootString

        def InitalizeBootRes():
            LibRes.BootstrapLanguage = wwYaml.read_yaml_from_disk('BootstrapLanguage.yaml')
            LibRes.BootstrapLocale = wwYaml.read_yaml_from_disk('BootstrapLocale.yaml')
            LibRes.BootstrapPath = wwYaml.read_yaml_from_disk('BootstrapPath.yaml')
            LibRes.BootstrapString = wwYaml.read_yaml_from_disk('BootstrapString.yaml')

            LibRes.InstallationProfile = wwYaml.read_yaml_from_disk('BootstrapBlankProfile.yaml')

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
            RootVar.bootstrapGuiProp = LibRes.BootstrapString.get('Universal')
            LibTk.Window.InitializeWindow(RootVar.bootstrapGui, RootVar.bootstrapGuiProp)

        def ConfigureWidgets():
            Widgets.comboboxStorageWizardLang = StringVar()
            Widgets.comboboxStorageWizardLangList = LibRes.BootstrapLanguage['WizardLanguages']

            Widgets.comboboxStorageTskLang = StringVar()
            Widgets.comboboxStorageTskLangList = LibRes.BootstrapLanguage['TskLanguages']

        def Wrapper():
            Methods.Initialize.InitalizeBootRes()
            Methods.Initialize.InitalizeSelf()
            Methods.Initialize.ConfigureWidgets()

    class LanguageSelect:
        def FillPathsBackToLibRes():
            import os
            # This method in bootstrap, it fill a language based resource path for installer.
            foldersDict = LibRes.BootstrapPath['Folders']
            filesDict = LibRes.BootstrapPath['Files']

            # Get root resources directory name.
            resourcesDirName = foldersDict['Resources']
            workingResourcesPath = Env.Path.merge_path_with_work_dir(resourcesDirName)

            # Generage language based root resource path(full path).
            if workingResourcesPath is not False: # Cover error.
                langBasedRootResourcesPath = Env.Path.Complement.merge_system(workingResourcesPath, LibRes.Language.WizardDevLanguage)

                langBasedWizardResPath = Env.Path.Complement.merge_system(workingResourcesPath, LibRes.Language.WizardDevLanguage)
                langBasedWizardBinPath = Env.Path.Complement.merge_system(workingResourcesPath, LibRes.Language.WizardBinLanguage)
                langBasedTskResPath = Env.Path.Complement.merge_system(workingResourcesPath, LibRes.Language.TskDevLanguage)

                # Generate language based sub resource folder name and path by root resource path(full path).
                archiveDirName = foldersDict.get('Archive')
                binDirName = foldersDict.get('Bin')
                configDirName = foldersDict.get('Config')
        
                langBasedArchiveDirPath = Env.Path.Complement.merge_system(langBasedTskResPath, archiveDirName)
                langBasedBinDirPath = Env.Path.Complement.merge_system(langBasedWizardBinPath, binDirName)
                langBasedConfigDirPath = Env.Path.Complement.merge_system(langBasedWizardResPath, configDirName)

                # Generate binary file path by language based sub resource path(full path).
                zipBinName = filesDict.get('Bin').get('7za')

                langBasedzipBinName = Env.Path.Complement.merge_system(langBasedBinDirPath, zipBinName)

                # Generate installer configs file path by language based...
                debugOptionsName = filesDict.get('Config').get('DebugOptions')
                archiveYamlName = filesDict.get('Config').get('Archive')
                gamesYamlName = filesDict.get('Config').get('Games')
                templatesYamlName = filesDict.get('Config').get('Templates')
                structureYamlName = filesDict.get('Config').get('Structure')
                stringYamlName = filesDict.get('Config').get('String')
                tkinterYamlName = filesDict.get('Config').get('Tkinter')

                langBasedDebugOptionsYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, debugOptionsName)
                langBasedArchiveYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, archiveYamlName)
                langBasedGamesYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, gamesYamlName)
                langBasedTemplatesYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, templatesYamlName)
                langBasedStructureYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, structureYamlName)
                langBasedStringYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, stringYamlName)
                langBasedTkinterYamlPath = Env.Path.Complement.merge_system(langBasedConfigDirPath, tkinterYamlName)

                # Fill final results back to LibRes.

                LibRes.InstallationProfile['Installer']['Archive']['Source'] = langBasedArchiveDirPath

                LibRes.InstallationProfile['Installer']['Bin']['7-zip'] = langBasedzipBinName

                LibRes.InstallationProfile['Installer']['ConfigPath']['DebugOptions'] = langBasedDebugOptionsYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['Archive'] = langBasedArchiveYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['Games'] = langBasedGamesYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['Templates'] = langBasedTemplatesYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['Structure'] = langBasedStructureYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['String'] = langBasedStringYamlPath
                LibRes.InstallationProfile['Installer']['ConfigPath']['Tkinter'] = langBasedTkinterYamlPath
                # Plz run Yaml loader(loading screen) after fill language based resources path.
            else:
                sys.exit(-2)
            
        def DetectSupportedLang():
            import sys
            convertDict = LibRes.BootstrapLocale['CodePage2ShortLang']
            supportedLangArray = LibRes.BootstrapLanguage['SupportedLanguages']
            sysDevLang = convertDict.get(sys.stdin.encoding)
        
            if sysDevLang in supportedLangArray:
                LibTk.Window.SafeDestroy(RootVar.bootstrapGui)
                LibRes.Language.WizardDevLanguage = sysDevLang
                LibRes.Language.TskDevLanguage = sysDevLang

                # Code to force enable such language, for debug use.
                #LibRes.Language.WizardDevLanguage = 'zh-CN'
                #LibRes.Language.TskDevLanguage = 'zh-CN'
                
                Methods.LanguageSelect.FillPathsBackToLibRes()
            else:
                Methods.LanguageSelect.ConfigureWidgets(RootVar.bootstrapGui)
                RootVar.bootstrapGui.deiconify()
                LibTk.Window.ShowWindow(RootVar.bootstrapGui)
            return
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
            return
        def SetLangAndCopyBack():
            from LibResources import BootstrapLocale

            wizardLang = Widgets.comboboxStorageWizardLang.get()
            tskLang = Widgets.comboboxStorageTskLang.get()
            convertDict = BootstrapLocale['DisplayLang2DevLang']

            wizardDevLang = convertDict[wizardLang]
            tskDevLang = convertDict[tskLang]

            LibRes.Language.WizardDevLanguage = wizardDevLang
            LibRes.Language.TskDevLanguage = tskDevLang

            RootVar.bootstrapGui.destroy()
            Methods.LanguageSelect.FillPathsBackToLibRes()
            return
        def NextStep_SaveSettings():
            boolWizardLang = bool(Widgets.comboboxStorageWizardLang.get())
            boolTskLang = bool(Widgets.comboboxStorageTskLang.get())

            if boolWizardLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict['errorWizardLangEmpty'])
            elif boolTskLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict['errorTskLangEmpty'])
            else:
                Methods.LanguageSelect.SetLangAndCopyBack()
            return

        def Wrapper():
            Methods.LanguageSelect.DetectSupportedLang()
            return
    class LoadingScreen:
        def ReadConfigFromDisk():
            from LibOperate import WaterWellsYaml as wwYaml
            from LibResources import InstallationProfile as Profile
            from LibResources import Resources

            # ConfigInRam
            Resources.Config.DebugYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['DebugOptions'])
            Resources.Config.ArchiveYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['Archive'])
            Resources.Config.GamesYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['Games'])
            Resources.Config.TemplatesYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['Templates'])
            Resources.Config.StructureYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['Structure'])
            Resources.Config.StringYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['String'])
            Resources.Config.TkinterYaml = wwYaml.read_yaml_from_disk(Profile['Installer']['ConfigPath']['Tkinter'])
            return
        def FillVarFromConfig():
            from LibResources import InstallationProfile
            from LibResources import Resources

            # Add Archive Collection Array
            # This Array will be use in a "for" method,
            # design for shortest code to unpack the archives.
            InstallationProfile['Installer']['Archive']['Collection'] = Resources.Config.ArchiveYaml['Collection']

            # Add optional installer options.
            # There is a feature require Tsk config Templates relative path.
            InstallationProfile['Installer']['Optional']['ProgramStructure'] = Resources.Config.StructureYaml['Program']
            InstallationProfile['Installer']['Optional']['Templates'] = Resources.Config.TemplatesYaml
            return
        def DoLoadConfig(window):
            from LibPython import Process

            import LibResources as LibRes
            Methods.LoadingScreen.ReadConfigFromDisk()
            Methods.LoadingScreen.FillVarFromConfig()

            # End bootstrap and loading screen.
            from LibTkinter import Window as LibTkWin
            LibTkWin.SafeDestroy(window)

        def TheLoadingScreen():
            import tkinter
            import LibTkinter as LibTk
            from LibPython import UnitConversion as Unit

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
            return

        def Wrapper():
            Methods.LoadingScreen.TheLoadingScreen()
            return


def Wrapper():
    import traceback
    from LibPython import Process
    try:
        Methods.Initialize.Wrapper()
        Methods.LanguageSelect.Wrapper()
        Methods.LoadingScreen.Wrapper()
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        Process.pauseMe()
        sys.exit(-3)
    return