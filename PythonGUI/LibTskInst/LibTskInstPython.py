import yaml
import subprocess

class MoHa:
    def Add1S():
        return
class UnitConversion:
    def Second2Millisecond(input):

        return int(input * 1000)
    def FormatArray2String(inputArray):

        return '\n'.join(inputArray)
    def Str2Unicode(input):
        text = u"{0}".format(input)
        return text
class Process:
    def DoLaunchAndWait(command, useShell):
        p = subprocess.Popen(command, shell = useShell)
        p.wait()
        return
class Environment:
    class System:
        def GetSysTempPath():
            import os
            from os.path import normpath
            # A user reported that "default temp" is mismatched with cmd %TEMP% environment variable.
            # To avoid it, get this variable directly is better than use "import tempfile".

            return normpath(os.environ['TEMP'])
        def GetSysShortLang(ShortLangDict):
            # Return a short language.
            # This is a system information.

            # The language detect is through user system non-unicode encoding.
            # Or I call it "stdin".  I get the encoding by get stdin.
            # If someone got the better or the best way to get non-unicode
            # encoding,
            #   then let me know, I will use that method to get information
            #   what we
            #   need.
            import sys
            return ShortLangDict.get(sys.stdin.encoding)
        def GetSysStartupMenuPath():
            import winshell
            from os.path import normpath

            return normpath(winshell.programs())
        def GetSysDesktopPath():
            import winshell
            from os.path import normpath

            return normpath(winshell.desktop())
    class Path:
        def AddWorkingDirToRelativePath(RelativePath):
            import os
            # pwd come from a Linux CLI command.
            pwd = os.getcwd()
            return os.path.join(pwd, RelativePath)
        def GetWorkingDirectory():
            # Please use os.getcwd() in code.
            # This is just a sample, do not use in the code.
            import os
            return os.getcwd()
        def GetInstallPath():
            from LibTskInstResources import InstallationProfile
            return InstallationProfile['Basic']['InstallPath']
class InputOutput:
    class Yaml:
        def ReadYaml(filePath):
            with open(filePath, 'r', encoding = 'utf8') as file:
                dict = yaml.load(file)
            return dict
        def WriteYaml(dict, filePath):
            with open(filePath, 'w', encoding = 'utf8') as file:
                yaml.dump(dict, file, default_flow_style = False, allow_unicode = True)
            return
    class Zip:
        def DoUnpack(file, targetPath):
            def GenerateCommand(file, targetPath):
                from LibTskInstResources import Methods as binCfg

                # Example:
                # 7za x "Archive.7z" -o"C:\Unpack" -y

                binPath = binCfg.Installer.Bin.Zip()

                binArg = r'"{0}" x'.format(binPath)
                fileArg = r'"{0}"'.format(file)
                targetPathArg = r'"{0}"'.format(targetPath)

                command = r'{0} {1} -o{2} -y'.format(binArg, fileArg, targetPathArg)

                return command

            command = GenerateCommand(file, targetPath)
            Process.DoLaunchAndWait(command, True)
            return
    class Templates:
        def DoModify(perFileDict):
            from LibTskInstResources import Methods as wizardCfg
            from os import path

            # UTF-8: utf8
            # ANSI: mbcs
            # All source file(read) would be UTF-8 format.

            # Decode basic object properties

            installPath = wizardCfg.Basic.InstallPath()
            perFileDict['FullSource'] = path.join(installPath, perFileDict['RelativeSource'])
            perFileDict['FullOutput'] = path.join(installPath, perFileDict['RelativeOutput'])

            # Get replace information.

            editorProfile = perFileDict['Config']

            # Bug: if use for directly, it only do single modify.
            # Because each modify read same unmodified template.
            # Write first file, then read this new file instead of the unmodified template.

            firstTimeEdit = True

            # Open file, input and output.
            # Remember to close() this file at the end!

            templateFile = open(perFileDict['FullSource'], 'r', encoding = 'utf8')
            
            # Methods for editing the file.

            def ModifyRules(groupName, optionName, optionValue, endOfLine):
                result = ''
                fixedResult = None
                EOL = endOfLine

                def AddOption(optionValue):

                    return optionName + optionValue
                # Universal removed comments
                if groupName == 'Comment':
                    result = ''
                    EOL = False

                # Simple combined groups.
                # This group name will combined option and value together,
                # without any extra process.
                if groupName == 'Combined':
                    result = AddOption(optionValue)

                # Tsk_MainConfig
                if groupName == 'GameExePath':
                    result = AddOption(wizardCfg.Basic.GameExePath())
                if groupName == 'TskNetExePath':
                    result = AddOption(wizardCfg.Installer.Optional.ProgramStructure.TskNet.Bin.TskNetMainExe())

                # TskNet_LauncherScript
                if groupName == 'SetTempPath':
                    result = AddOption(wizardCfg.Basic.TempPath())

                # TskNet_ProgramScript

                # No action available / required.

                # TskNet_Account
                if groupName == 'TencoAccount':
                    if wizardCfg.Unattended.ManageId() == True:
                        result = AddOption(wizardCfg.UserData.TencoAccount())
                    else:
                        result = AddOption('')
                if groupName == 'TencoPassword':
                    if wizardCfg.Unattended.ManageId() == True:
                        result = AddOption(wizardCfg.UserData.TencoPassword())
                    else:
                        result = AddOption('')

                # Add EOL
                if EOL == True:
                    fixedResult = result + '\n'
                else:
                    fixedResult = result

                return fixedResult
            def GetReplacedLine(lineToReplaceDict, line):
                groupName = lineToReplaceDict['Group']
                optionMark = lineToReplaceDict['Mark']
                optionName = lineToReplaceDict['Option']
                optionValue = lineToReplaceDict['Value']
                

                if line.find(optionMark) != -1:
                    result = ModifyRules(groupName, optionName, optionValue, True)
                else:
                    result = line
                return result

            # A for loop to modify config.

            # Get per modify config group dictionary.
            for perModifyDict in editorProfile:

                # Get the group name, it can't be directly read.
                for perModifyDictName in perModifyDict:

                    # Use group name to receive final replace profile dictionary.
                    lineToReplaceDict = perModifyDict[perModifyDictName]

                    # Check if this is the first time to open the file.
                    # Else, open wrote file instead open template.
                    # The file designed for modify multiple times.

                    if firstTimeEdit != False:
                        lineList = templateFile.readlines()
                        with open(perFileDict['FullOutput'], 'w', encoding = perFileDict['Encoding']) as outputFile:
                            for line in lineList:
                                result = GetReplacedLine(lineToReplaceDict, line)
                                outputFile.write(result)
                        firstTimeEdit = False

                    elif firstTimeEdit == False:
                        # Open and read wrote file to memory.
                        inputFile = open(perFileDict['FullOutput'], 'r', encoding = perFileDict['Encoding'])
                        lineList = inputFile.readlines()
                        inputFile.close()

                        # Overwrite the wrote file use 'w'.
                        with open(perFileDict['FullOutput'], 'w', encoding = perFileDict['Encoding']) as outputFile:
                            for line in lineList:
                                result = GetReplacedLine(lineToReplaceDict, line)
                                outputFile.write(result)

            templateFile.close()
            return
    class Shortcut:
        def CreateShortcut(lnkFileLocation, targetFullPath, targetWorkingDir):
            #from win32com.client import Dispatch
            import winshell

            # The shortcut icon is the same as the source exe file.

            winshell.CreateShortcut(Path = lnkFileLocation,
                                    Target = targetFullPath,
                                    StartIn = targetWorkingDir,
                                    Icon = (targetFullPath, 0),
                                    Description = '')

            #shell = Dispatch('WScript.Shell')
            #shortcut = shell.CreateShortCut(uLnkFileLocation)

            #shortcut.Targetpath = uTragetFullPath
            #shortcut.WorkingDirectory = uTargetWorkingDir
            #shortcut.IconLocation = uTragetFullPath

            #shortcut.save()
            return