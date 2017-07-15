from LibPython import Environment

# Load bootstrap yaml before window showing up.
BootstrapLanguage = None
BootstrapLocale = None
BootstrapPath = None
BootstrapString = None

# Fill duiring installer steps.
RawProfileDict = {}

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
class DecodedProfile:
    class Config:
        # Add yamls read from disk after bootstrap.
        DebugYaml = None
        ArchiveYaml = None
        GamesYaml = None
        StructureYaml = None
        StringYaml = None
        TkinterYaml = None
        EditorYaml = None
    class Methods:
        # Call these methods AFTER you fill the config!
        class Basic:
            def GetDict():

                return RawProfileDict['Basic']

            def MainShortcut():

                return DecodedProfile.Methods.Basic.GetDict()['DesktopShortcut']
            def GameExePath():

                return DecodedProfile.Methods.Basic.GetDict()['GameExePath']
            def InstallPath():

                return DecodedProfile.Methods.Basic.GetDict()['InstallPath']
            def StartMenuGroup():

                return DecodedProfile.Methods.Basic.GetDict()['StartMenuGroup']
            def TempPath():

                return DecodedProfile.Methods.Basic.GetDict()['TempPath']
        class Installer:
            def GetDict():
            
                return RawProfileDict['Installer']

            class Archive:
                def GetDict():

                    return DecodedProfile.Methods.Installer.GetDict()['Archive']

                def Collection():

                    return DecodedProfile.Methods.Installer.Archive.GetDict()['Collection']
                def Source():

                    return DecodedProfile.Methods.Installer.Archive.GetDict()['Source']
            class Bin:
                def GetDict():

                    return DecodedProfile.Methods.Installer.GetDict()['Bin']

                def Zip():

                    return DecodedProfile.Methods.Installer.Bin.GetDict()['7-zip']
                def Editor():

                    return DecodedProfile.Methods.Installer.Bin.GetDict()['BatchEditor']
            class ConfigPath:
                def GetDict():

                    return DecodedProfile.Methods.Installer.GetDict()['ConfigPath']

                def Archive():

                    return DecodedProfile.Methods.Installer.ConfigPath.GetDict()['Archive']
                def Games():

                    return DecodedProfile.Methods.Installer.ConfigPath.GetDict()['Games']
                def Structure():

                    return DecodedProfile.Methods.Installer.ConfigPath.GetDict()['Structure']
                def String():

                    return DecodedProfile.Methods.Installer.ConfigPath.GetDict()['String']
                def Tkinter():

                    return DecodedProfile.Methods.Installer.ConfigPath.GetDict()['Tkinter']
        class Unattended:
            def GetDict():

                return RawProfileDict['Unattended']

            def ManageDesktopShortcut():

                return DecodedProfile.Methods.Unattended.GetDict()['ManageDesktopShortcut']
            def ManageGameExePath():
            
                return DecodedProfile.Methods.Unattended.GetDict()['ManageGameExePath']
            def ManageId():
          
                return DecodedProfile.Methods.Unattended.GetDict()['ManageId']
            def ManageSWRSAddr():

                return DecodedProfile.Methods.Unattended.GetDict()['ManageSWRSAddr']
            def ManageStartMenuShortcut():
      
                return DecodedProfile.Methods.Unattended.GetDict()['ManageStartMenuShortcut']
            def UnattendedMode():
      
                return DecodedProfile.Methods.Unattended.GetDict()['UnattendedMode']
            def UpgradeDatabase():
      
                return DecodedProfile.Methods.Unattended.GetDict()['UpgradeDatabase']
            def UpgradeIdYaml():

                return DecodedProfile.Methods.Unattended.GetDict()['UpgradeIdYaml']
            def UpgradeSWRSAddr():
      
                return DecodedProfile.Methods.Unattended.GetDict()['UpgradeSWRSAddr']
            def UpgradeTskIni():
      
                return DecodedProfile.Methods.Unattended.GetDict()['UpgradeTskIni']
        class Upgrade:
            def GetDict():

                return RawProfileDict['Upgrade']

            def DatabasePath():

                return DecodedProfile.Methods.Upgrade.GetDict()['DatabasePath']
            def ReportYamlPath():

                return DecodedProfile.Methods.Upgrade.GetDict()['ReportYamlPath']
            def SwrsPath():

                return DecodedProfile.Methods.Upgrade.GetDict()['SwrsPath']
            def SwrsUpgradeMode():

                return DecodedProfile.Methods.Upgrade.GetDict()['SwrsUpgradeMode']
            def TskIniPath():

                return DecodedProfile.Methods.Upgrade.GetDict()['TskIniPath']
        class UserData:
            def GetDict():

                return RawProfileDict['UserData']

            def SWRSAddr7z():
                from LibPython import Environment

                archiveSource = DecodedProfile.Methods.Installer.Archive.Source()
                swrsaddr = DecodedProfile.Methods.UserData.GetDict()['SWRSAddr7z']

                if swrsaddr == False:
                    result = False
                else:
                    result = Environment.Path.Complement.merge_system(archiveSource, swrsaddr)

                return result
            def TencoAccount():

                return DecodedProfile.Methods.UserData.GetDict()['TencoID']
            def TencoPassword():

                return DecodedProfile.Methods.UserData.GetDict()['TencoPassword']
        class Optional:
            class Structure:
                def GetDict():

                    return DecodedProfile.Config.StructureYaml
                class Program:
                    def GetDict():

                        return DecodedProfile.Methods.Optional.Structure.GetDict()['Program']

                    class Tsk:
                        def GetDict():

                            return DecodedProfile.Methods.Optional.Structure.Program.GetDict()['Tsk']

                        class Bin:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.Tsk.GetDict()['Bin']

                            def DefaultInstallFolder():
                                
                                return DecodedProfile.Methods.Optional.Structure.Program.Tsk.Bin.GetDict()['DefaultInstallFolder']
                            def TskMainExe():
                                installedPath = DecodedProfile.Methods.Basic.InstallPath()
                                exePath = DecodedProfile.Methods.Optional.Structure.Program.Tsk.Bin.GetDict()['TskMainExe']

                                result = Environment.Path.Complement.merge_system(installedPath, exePath)

                                return result
                        class Config:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.Tsk.GetDict()['Config']
                        
                            def TskMainIni():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.FullPath(),
                                    DecodedProfile.Methods.Optional.Structure.Program.Tsk.Config.GetDict()['TskMainIni'])
                                return result
                        class Templates:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.Tsk.GetDict()['Templates']

                            def TskMainIniTemplate():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.FullPath(), 
                                    DecodedProfile.Methods.Optional.Structure.Program.Tsk.Templates.GetDict()['TskMainIni'])
                                return result
                    class TskNet:
                        def GetDict():

                            return DecodedProfile.Methods.Optional.Structure.Program.GetDict()['TskNet']

                        def RelativePath():

                            return DecodedProfile.Methods.Optional.Structure.Program.TskNet.GetDict()['RelativePath']
                        def FullPath():
                            installPath = DecodedProfile.Methods.Basic.InstallPath()
                            result = Environment.Path.Complement.merge_system(installPath, 
                                DecodedProfile.Methods.Optional.Structure.Program.TskNet.RelativePath())
                        
                            return result
                        class Bin:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.TskNet.GetDict()['Bin']

                            def TskNetMainExe():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.RelativePath(), 
                                    DecodedProfile.Methods.Optional.Structure.Program.TskNet.Bin.GetDict()['TskNetMainExe'])
                                return result
                        class Config:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.TskNet.GetDict()['Config']

                            def Account():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.FullPath(),
                                    DecodedProfile.Methods.Optional.Structure.Program.TskNet.Config.GetDict()['Account'])
                                return result
                        class Templates:
                            def GetDict():

                                return DecodedProfile.Methods.Optional.Structure.Program.TskNet.GetDict()['Templates']
                            def TskNetLauncherScript():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.FullPath(), 
                                    DecodedProfile.Methods.Optional.Structure.Program.TskNet.Templates.GetDict()['TskNetLauncherScript'])
                                return result
                            def TskNetProgramScript():
                                result = Environment.Path.Complement.merge_system(DecodedProfile.Methods.Optional.Structure.Program.TskNet.FullPath(), 
                                    DecodedProfile.Methods.Optional.Structure.Program.TskNet.Templates.GetDict()['TskNetProgramScript'])
                                return result
                class Shortcuts:
                    def GetDict():

                        return DecodedProfile.Methods.Optional.Structure.GetDict()['Shortcuts']

                    def StartupMenuGroup():

                        return DecodedProfile.Methods.Optional.Structure.Shortcuts.GetDict()['StartupMenuGroup']
                    def TskMainLnk():

                        return DecodedProfile.Methods.Optional.Structure.Shortcuts.GetDict()['TskMainLnk']
                    def Config():

                        return DecodedProfile.Methods.Optional.Structure.Shortcuts.GetDict()['Config']