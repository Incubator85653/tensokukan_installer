import yaml
import subprocess

class UnitConversion:
    def Second2Millisecond(input):

        return int(input * 1000)
    def FormatArray2String(inputArray):

        return '\n'.join(inputArray)
    def Str2Unicode(input):
        text = u"{0}".format(input)
        return text
    def StrAddNextLine(input):
        # This method replace {0} in a string...by "\n"
        # seems A string readed from yaml won't add next line.
        return input.format("\n")
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
        # This class do path combined job.
        class Complement:
            def merge_manually(first, second):
                """Usage:
                Both two path must be "slash removed" path.
                the second one can be a folder or a file with extension.

                This method is prevent a crash on some Ghost systems.
                On these systems, os.path.join will fail, reason unknown.
                It almost do the same thing just like os.path.join, but Windows platform specified.
                Return a path just like os.path.join.
                """

                result = "{0}\\{1}".format(first, second)
                return result

            def merge_system(first, second):
                """
                Use os.path.join to combined two path.
                """
                import os

                success = False # Use this to confirm if os.path.join is success.
                result = None
                try:
                    print("Auto merging path:\n\t{}, {}".format(first, second))

                    result = os.path.join(first, second)

                    print("Auto merged path: {}".format(result))
                    success = True # Set success var to true once os.path.join is success.
                except Exception as e:
                    print(e)
                    print("\nAuto merge path failed.\n")
                
                # Try manually combined if system method is failed.
                if success is not True:
                    try:
                        print("Manually merging path:\n\t{}, {}".format(first, second))
                        
                        result = merge_manually(first, second)
                        
                        print("Manually merged path: {}".format(result))
                    except Exception as e:
                        print(e)

                return result

        def get_full_work_dir():
            """Return current working directory,
            If can't get current working directory(for any reason),
            print error message and return False instead.
            """
            import os

            result = None
            try:
                result = os.getcwd()
            except Exception as e:
                print(e)
                result = False
                
            return result

        def merge_path_with_work_dir(path_name): 
            """Return a path with working dir.
            Give a name, use this method to get a full path with current working directory.
            <Dirve>:\<workingDir>\<path_name>
            """           
            result = None

            # pwd come from a Linux CLI command.
            pwd = get_full_work_dir()

            if pwd is not False:
                result = Environment.Path.Complement.merge_system(pwd, path_name)
            else:
                result = False

            return result