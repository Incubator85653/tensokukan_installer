import yaml

class WaterWellsYaml:
    def read_yaml_from_disk(filePath):
        result = False

        with open(filePath, 'r', encoding = 'utf8') as file:
            result = yaml.load(file)

        return result
    def write_yaml_to_disk(dict, filePath):
        with open(filePath, 'w', encoding = 'utf8') as file:
            yaml.dump(dict, file, default_flow_style = False, allow_unicode = True)
    # Sometimes you have a yaml and has multiple sub-dictionary
    # Use for loop you can get file name
    # and put it in here to get it's contents
    def get_yaml_content_by_its_name(name, dict):
        result = dict[name]
        
        return result

class Zip:
    def GenerateCommand(file, targetPath):
            from LibResources import Methods as binCfg

            # Example:
            # 7za x "Archive.7z" -o"C:\Unpack" -y

            binPath = binCfg.Installer.Bin.Zip()

            binArg = r'"{0}" x'.format(binPath)
            fileArg = r'"{0}"'.format(file)
            targetPathArg = r'"{0}"'.format(targetPath)

            command = r'{0} {1} -o{2} -y'.format(binArg, fileArg, targetPathArg)

            return command
    def DoUnpack(file, targetPath):
        command = GenerateCommand(file, targetPath)
        try:
            Process.DoLaunchAndWait(command, True)
        except:
            LibErr.ZipUnpackError(command)

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