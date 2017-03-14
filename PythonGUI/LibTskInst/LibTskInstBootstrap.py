import LibTskInstPython as LibPy
import LibTskInstTkinter as LibTk
import LibTskInstResources as LibRes

from tkinter import *
from tkinter import ttk

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
        def GetBootString():
            # Return a language specified string dictionary for the bootstrap
            # interface.
            # If the system language is not supported by project, return en-US
            # as default language dictionary.
            import sys
            sysLang = LibPy.Environment.System.GetSysShortLang(LibRes.BootstrapLocale.get('CodePage2ShortLang'))
            supportedLangArray = LibRes.BootstrapLanguage.get('SupportedLanguages')

            if sysLang in supportedLangArray:
                bootString = LibRes.BootstrapString.get(sysLang)
            else:
                bootString = LibRes.BootstrapString.get('en-US')

            return bootString
        def InitalizeBootRes():
            from LibTskInstPython import InputOutput as LibIO

            LibRes.BootstrapLanguage = LibIO.Yaml.ReadYaml('BootstrapLanguage.yaml')
            LibRes.BootstrapLocale = LibIO.Yaml.ReadYaml('BootstrapLocale.yaml')
            LibRes.BootstrapPath = LibIO.Yaml.ReadYaml('BootstrapPath.yaml')
            LibRes.BootstrapString = LibIO.Yaml.ReadYaml('BootstrapString.yaml')

            LibRes.InstallationProfile = LibIO.Yaml.ReadYaml('BootstrapBlankProfile.yaml')
            return
        def InitalizeSelf():
            # Set bootstrap gui string dictionary, based on language.
            RootVar.bootStringDict = Methods.Initialize.GetBootString()

            # Create a window for bootstrap interface.
            RootVar.bootstrapGui = Tk()
            # Hide.
            RootVar.bootstrapGui.withdraw()

            # Initalize window properties.
            RootVar.bootstrapGuiProp = LibRes.BootstrapString.get('Universal')
            LibTk.Window.InitializeWindow(RootVar.bootstrapGui, RootVar.bootstrapGuiProp)

            # Display again after initialize.

            # Well, show this window when it is needed.
            #Methods.LoadingScreen.bootstrapGui.deiconify()
            return
        def InitalizeWidgetsProp():
            Widgets.comboboxStorageWizardLang = StringVar()
            Widgets.comboboxStorageWizardLangList = LibRes.BootstrapLanguage.get('WizardLanguages')

            Widgets.comboboxStorageTskLang = StringVar()
            Widgets.comboboxStorageTskLangList = LibRes.BootstrapLanguage.get('TskLanguages')
            return

        def Wrapper():
            Methods.Initialize.InitalizeBootRes()
            Methods.Initialize.InitalizeSelf()
            Methods.Initialize.InitalizeWidgetsProp()
            return
    class LanguageSelect:
        def FillPathsBackToLibRes():
            import os
            # This method in bootstrap, it fill a language based resource path for installer.
            foldersDict = LibRes.BootstrapPath.get('Folders')
            filesDict = LibRes.BootstrapPath.get('Files')

            # Get root resources directory name.
            resourcesDirName = foldersDict.get('Resources')
            workingResourcesPath = LibPy.Environment.Path.OsPathJoinSimulator(os.getcwd(), resourcesDirName)

            # Generage language based root resource path(full path).
            langBasedRootResourcesPath = LibPy.Environment.Path.OsPathJoinSimulator(workingResourcesPath, LibRes.Language.WizardDevLanguage)

            langBasedWizardResPath = LibPy.Environment.Path.OsPathJoinSimulator(workingResourcesPath, LibRes.Language.WizardDevLanguage)
            langBasedWizardBinPath = LibPy.Environment.Path.OsPathJoinSimulator(workingResourcesPath, LibRes.Language.WizardBinLanguage)
            langBasedTskResPath = LibPy.Environment.Path.OsPathJoinSimulator(workingResourcesPath, LibRes.Language.TskDevLanguage)

            # Generate language based sub resource folder name and path by root resource path(full path).
            archiveDirName = foldersDict.get('Archive')
            binDirName = foldersDict.get('Bin')
            configDirName = foldersDict.get('Config')
        
            langBasedArchiveDirPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedTskResPath, archiveDirName)
            langBasedBinDirPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedWizardBinPath, binDirName)
            langBasedConfigDirPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedWizardResPath, configDirName)

            # Generate binary file path by language based sub resource path(full path).
            zipBinName = filesDict.get('Bin').get('7za')

            langBasedzipBinName = LibPy.Environment.Path.OsPathJoinSimulator(langBasedBinDirPath, zipBinName)

            # Generate installer configs file path by language based...
            archiveYamlName = filesDict.get('Config').get('Archive')
            gamesYamlName = filesDict.get('Config').get('Games')
            templatesYamlName = filesDict.get('Config').get('Templates')
            structureYamlName = filesDict.get('Config').get('Structure')
            stringYamlName = filesDict.get('Config').get('String')
            tkinterYamlName = filesDict.get('Config').get('Tkinter')

            langBasedArchiveYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, archiveYamlName)
            langBasedGamesYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, gamesYamlName)
            langBasedTemplatesYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, templatesYamlName)
            langBasedStructureYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, structureYamlName)
            langBasedStringYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, stringYamlName)
            langBasedTkinterYamlPath = LibPy.Environment.Path.OsPathJoinSimulator(langBasedConfigDirPath, tkinterYamlName)

            # Fill final results back to LibRes.

            LibRes.InstallationProfile['Installer']['Archive']['Source'] = langBasedArchiveDirPath

            LibRes.InstallationProfile['Installer']['Bin']['7-zip'] = langBasedzipBinName

            LibRes.InstallationProfile['Installer']['ConfigPath']['Archive'] = langBasedArchiveYamlPath
            LibRes.InstallationProfile['Installer']['ConfigPath']['Games'] = langBasedGamesYamlPath
            LibRes.InstallationProfile['Installer']['ConfigPath']['Templates'] = langBasedTemplatesYamlPath
            LibRes.InstallationProfile['Installer']['ConfigPath']['Structure'] = langBasedStructureYamlPath
            LibRes.InstallationProfile['Installer']['ConfigPath']['String'] = langBasedStringYamlPath
            LibRes.InstallationProfile['Installer']['ConfigPath']['Tkinter'] = langBasedTkinterYamlPath

            # Plz run Yaml loader(loading screen) after fill language based resources path.
            return
        def DetectSupportedLang():
            import sys
            convertDict = LibRes.BootstrapLocale.get('CodePage2ShortLang')
            supportedLangArray = LibRes.BootstrapLanguage.get('SupportedLanguages')
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
                                            text = RootVar.bootStringDict.get('labelWizardLang'))
            Widgets.labelWizardLangIntro = Label(window,
                                                 justify = LEFT,
                                                 text = LibPy.UnitConversion.FormatArray2String(RootVar.bootStringDict.get('labelWizardLangIntro')))
            Widgets.comboboxWizardLang = ttk.Combobox(window,
                                                      state = 'readonly',
                                                      textvariable = Widgets.comboboxStorageWizardLang,
                                                      values = Widgets.comboboxStorageWizardLangList,
                                                      width = 60)
            Widgets.labelTskLang = Label(window,
                                         justify = LEFT,
                                         text = RootVar.bootStringDict.get('labelTskLang'))
            Widgets.labelTskLangIntro = Label(window,
                                              justify = LEFT,
                                              text = LibPy.UnitConversion.FormatArray2String(RootVar.bootStringDict.get('labelTskLangIntro')),
                                              wraplength = 500)
            Widgets.comboboxTskLang = ttk.Combobox(window,
                                                          state = 'readonly',
                                                          textvariable = Widgets.comboboxStorageTskLang,
                                                          values = Widgets.comboboxStorageTskLangList,
                                                          width = 60)

            Widgets.buttonNext = Button(window,
                                        text = RootVar.bootStringDict.get('nextStepButton'),
                                        command = lambda : Methods.LanguageSelect.NextStep_SaveSettings(),
                                        width = 10)
            Widgets.buttonExit = Button(window,
                                        text = RootVar.bootStringDict.get('exitButton'),
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
            from LibTskInstResources import BootstrapLocale

            wizardLang = Widgets.comboboxStorageWizardLang.get()
            tskLang = Widgets.comboboxStorageTskLang.get()
            convertDict = BootstrapLocale.get('DisplayLang2DevLang')

            wizardDevLang = convertDict.get(wizardLang)
            tskDevLang = convertDict.get(tskLang)

            LibRes.Language.WizardDevLanguage = wizardDevLang
            LibRes.Language.TskDevLanguage = tskDevLang

            RootVar.bootstrapGui.destroy()
            Methods.LanguageSelect.FillPathsBackToLibRes()
            return
        def NextStep_SaveSettings():
            boolWizardLang = bool(Widgets.comboboxStorageWizardLang.get())
            boolTskLang = bool(Widgets.comboboxStorageTskLang.get())

            if boolWizardLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict.get('errorWizardLangEmpty'))
            elif boolTskLang is not True:
                LibTk.Window.StrNotice(RootVar.bootStringDict.get('errorTskLangEmpty'))
            else:
                Methods.LanguageSelect.SetLangAndCopyBack()
            return

        def Wrapper():
            Methods.LanguageSelect.DetectSupportedLang()
            return
    class LoadingScreen:
        def ReadConfigFromDisk():
            from LibTskInstPython import InputOutput as IO
            from LibTskInstResources import InstallationProfile as Profile
            from LibTskInstResources import Resources

            # ConfigInRam
            Resources.Config.ArchiveYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['Archive'])
            Resources.Config.GamesYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['Games'])
            Resources.Config.TemplatesYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['Templates'])
            Resources.Config.StructureYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['Structure'])
            Resources.Config.StringYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['String'])
            Resources.Config.TkinterYaml = IO.Yaml.ReadYaml(Profile['Installer']['ConfigPath']['Tkinter'])
            return
        def FillVarFromConfig():
            from LibTskInstResources import InstallationProfile
            from LibTskInstResources import Resources

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
            Methods.LoadingScreen.ReadConfigFromDisk()
            Methods.LoadingScreen.FillVarFromConfig()

            # End bootstrap and loading screen.
            from LibTskInstTkinter import Window as LibTkWin
            LibTkWin.SafeDestroy(window)
            return

        def TheLoadingScreen():
            import tkinter
            import LibTskInstTkinter as LibTk
            from LibTskInstPython import UnitConversion as Unit

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
    Methods.Initialize.Wrapper()
    Methods.LanguageSelect.Wrapper()
    Methods.LoadingScreen.Wrapper()
    return