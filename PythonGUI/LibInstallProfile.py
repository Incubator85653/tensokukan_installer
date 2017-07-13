from LibPython import Environment

# Fill these lovely yaml at very beginning...
BootstrapLanguage = None
BootstrapLocale = None
BootstrapPath = None
BootstrapString = None

# Fill duiring installer steps.
InstallationProfile = {}

# All the variable is full path.
# Don't assign relative path to a variable.
class Language:
    # Change value if necessary.
    WizardDevLanguage = 'zh-CN'
    TskDevLanguage = 'zh-CN'
    # By design, the installer will always use en-US as wizard binary(like 7za)
    # language.
    # Only change it if necessary.
    WizardBinLanguage = 'en-US'
class Profile:
    class Config:
        # Add yamls read from disk after bootstrap.
        DebugYaml = None
        ArchiveYaml = None
        GamesYaml = None
        StructureYaml = None
        StringYaml = None
        TkinterYaml = None
    class Methods:
        class Structure:
            def GetDict():

                return Profile.Config.StructureYaml

            class Program:
                def GetDict():

                    return Profile.Methods.Structure.GetDict()['Program']

                class Tsk:
                    def GetDict():

                        return Profile.Methods.Structure.Program.GetDict()['Tsk']

                    class Bin:
                        def GetDict():

                            return Profile.Methods.Structure.Program.Tsk.GetDict()['Bin']

                        def DefaultInstallFolder():

                            return Profile.Methods.Structure.Program.Tsk.Bin.GetDict()['DefaultInstallFolder']
            class Shortcuts:
                def GetDict():

                    return Profile.Methods.Structure.GetDict()['Shortcuts']

                def StartupMenuGroup():

                    return Profile.Methods.Structure.Shortcuts.GetDict()['StartupMenuGroup']
                def TskMainLnk():

                    return Profile.Methods.Structure.Shortcuts.GetDict()['TskMainLnk']
                def Config():

                    return Profile.Methods.Structure.Shortcuts.GetDict()['Config']
class Methods:
    # Call these methods AFTER you fill the config!
    class Basic:
        def GetDict():

            return InstallationProfile['Basic']

        def MainShortcut():

            return Methods.Basic.GetDict()['DesktopShortcut']
        def GameExePath():

            return Methods.Basic.GetDict()['GameExePath']
        def InstallPath():

            return Methods.Basic.GetDict()['InstallPath']
        def StartMenuGroup():

            return Methods.Basic.GetDict()['StartMenuGroup']
        def TempPath():

            return Methods.Basic.GetDict()['TempPath']
    class Installer:
        def GetDict():
            
            return InstallationProfile['Installer']

        class Archive:
            def GetDict():

                return Methods.Installer.GetDict()['Archive']

            def Collection():

                return Methods.Installer.Archive.GetDict()['Collection']
            def Source():

                return Methods.Installer.Archive.GetDict()['Source']
        class Bin:
            def GetDict():

                return Methods.Installer.GetDict()['Bin']

            def Zip():

                return Methods.Installer.Bin.GetDict()['7-zip']
        class ConfigPath:
            def GetDict():

                return Methods.Installer.GetDict()['ConfigPath']

            def Archive():

                return Methods.Installer.ConfigPath.GetDict()['Archive']
            def Games():

                return Methods.Installer.ConfigPath.GetDict()['Games']
            def Structure():

                return Methods.Installer.ConfigPath.GetDict()['Structure']
            def String():

                return Methods.Installer.ConfigPath.GetDict()['String']
            def Tkinter():

                return Methods.Installer.ConfigPath.GetDict()['Tkinter']
        class Optional:
            def GetDict():

                return Methods.Installer.GetDict()['Optional']

            class ProgramStructure:
                def GetDict():

                    return Methods.Installer.Optional.GetDict()['ProgramStructure']

                class Tsk:
                    def GetDict():

                        return Methods.Installer.Optional.ProgramStructure.GetDict()['Tsk']

                    class Bin:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.Tsk.GetDict()['Bin']

                        def TskMainExe():
                            installedPath = Methods.Basic.InstallPath()
                            exePath = Methods.Installer.Optional.ProgramStructure.Tsk.Bin.GetDict()['TskMainExe']

                            result = Environment.Path.Complement.merge_system(installedPath, exePath)

                            return result
                    class Config:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.Tsk.GetDict()['Config']
                        
                        def TskMainIni():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.Tsk.Config.GetDict()['TskMainIni'])
                            return result
                    class Templates:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.Tsk.GetDict()['Templates']

                        def TskMainIniTemplate():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.Tsk.Templates.GetDict()['TskMainIni'])
                            return result
                class TskNet:
                    def GetDict():

                        return Methods.Installer.Optional.ProgramStructure.GetDict()['TskNet']

                    def RelativePath():

                        return Methods.Installer.Optional.ProgramStructure.TskNet.GetDict()['RelativePath']
                    def FullPath():
                        installPath = Methods.Basic.InstallPath()
                        result = Environment.Path.Complement.merge_system(installPath, Methods.Installer.Optional.ProgramStructure.TskNet.RelativePath())
                        
                        return result
                    class Bin:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.TskNet.GetDict()['Bin']

                        def TskNetMainExe():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Bin.GetDict()['TskNetMainExe'])
                            return result
                        def TskNetLauncherScript():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Bin.GetDict()['TskNetLauncherScript'])
                            return result
                        def TskNetProgramScript():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Bin.GetDict()['TskNetProgramScript'])
                            return result
                    class Config:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.TskNet.GetDict()['Config']

                        def Account():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Config.GetDict()['Account'])
                            return result
                    class Templates:
                        def GetDict():

                            return Methods.Installer.Optional.ProgramStructure.TskNet.GetDict()['Templates']
                        def TskNetLauncherScript():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Templates.GetDict()['TskNetLauncherScript'])
                            return result
                        def TskNetProgramScript():
                            result = Environment.Path.Complement.merge_system(Methods.Installer.Optional.ProgramStructure.TskNet.FullPath(), Methods.Installer.Optional.ProgramStructure.TskNet.Templates.GetDict()['TskNetProgramScript'])
                            return result
    class Unattended:
        def GetDict():

            return InstallationProfile['Unattended']

        def ManageDesktopShortcut():

            return Methods.Unattended.GetDict()['ManageDesktopShortcut']
        def ManageGameExePath():
            
            return Methods.Unattended.GetDict()['ManageGameExePath']
        def ManageId():
          
            return Methods.Unattended.GetDict()['ManageId']
        def ManageSWRSAddr():

            return Methods.Unattended.GetDict()['ManageSWRSAddr']
        def ManageStartMenuShortcut():
      
            return Methods.Unattended.GetDict()['ManageStartMenuShortcut']
        def UnattendedMode():
      
            return Methods.Unattended.GetDict()['UnattendedMode']
        def UpgradeDatabase():
      
            return Methods.Unattended.GetDict()['UpgradeDatabase']
        def UpgradeIdYaml():

            return Methods.Unattended.GetDict()['UpgradeIdYaml']
        def UpgradeSWRSAddr():
      
            return Methods.Unattended.GetDict()['UpgradeSWRSAddr']
        def UpgradeTskIni():
      
            return Methods.Unattended.GetDict()['UpgradeTskIni']
    class Upgrade:
        def GetDict():

            return InstallationProfile['Upgrade']

        def DatabasePath():

            return Methods.Upgrade.GetDict()['DatabasePath']
        def ReportYamlPath():

            return Methods.Upgrade.GetDict()['ReportYamlPath']
        def SwrsPath():

            return Methods.Upgrade.GetDict()['SwrsPath']
        def SwrsUpgradeMode():

            return Methods.Upgrade.GetDict()['SwrsUpgradeMode']
        def TskIniPath():

            return Methods.Upgrade.GetDict()['TskIniPath']
    class UserData:
        def GetDict():

            return InstallationProfile['UserData']

        def SWRSAddr7z():
            from LibPython import Environment

            archiveSource = Methods.Installer.Archive.Source()
            swrsaddr = Methods.UserData.GetDict()['SWRSAddr7z']

            if swrsaddr == False:
                result = False
            else:
                result = Environment.Path.Complement.merge_system(archiveSource, swrsaddr)

            return result
        def TencoAccount():

            return Methods.UserData.GetDict()['TencoID']
        def TencoPassword():

            return Methods.UserData.GetDict()['TencoPassword']