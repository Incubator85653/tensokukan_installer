import sys
import yaml
import subprocess

class Console:
    def ansi_print(print_object):
        """ANSI print method.
        As its name, you just use the console as a ANSI console.
        Fuck Windows."""
        sys_encoding = sys.stdin.encoding

        print(print_object.encode(sys_encoding,errors='replace').decode(sys_encoding, 'ignore'))
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
    def pause_program():
        programPause = input(r"Press the <ENTER> key to continue...")
    def handle_exception(err_object, pause):
        """Universal error print & log method.
        Catch an exception and throw it away here.
        Pause: a bool value that control if program need to pause after print error message.

        After that, give a exit code and close the program in your code if you give up.
        No matter, we're not a user-friendly software.
        JUST DO IT.

        # Log feature is not competed in this version.
        # TODO
        """
        import traceback

        Console.ansi_print("\nERROR BEGIN\n")

        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, 
                                  exc_value, 
                                  exc_traceback)

        Console.ansi_print("\nERROR END\n")

        if pause:
            Process.pause_program()
class Environment:
    class System:
        def GetSysTempPath():
            """MUST_SUCCESS_METHOD"""
            from os import environ
            from os.path import normpath
            # A user reported that "default temp" is mismatched with cmd %TEMP%
            # environment variable.
            # To avoid it, get this variable directly is better than use
            # "import tempfile".

            result = None
            try:
                result = normpath(environ['TEMP'])
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)

            return result

        def GetSysShortLang(ShortLangDict):
            """MUST_SUCCESS_METHOD"""
            # Return a short language.
            # This is a system information.

            # The language detect is through user system non-unicode encoding.
            # Or I call it "stdin".  I get the encoding by get stdin.
            # If someone got the better or the best way to get non-unicode
            # encoding,
            #   then let me know, I will use that method to get information
            #   what we
            #   need.
            result = None

            try:
                result = ShortLangDict.get(sys.stdin.encoding)
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)
            
            return result

        def GetSysStartupMenuPath():
            """MUST_SUCCESS_METHOD"""
            import winshell
            from os.path import normpath

            result = None
            
            try:
                result = normpath(winshell.programs())
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)

            return result

        def GetSysDesktopPath():
            """MUST_SUCCESS_METHOD"""
            import winshell
            from os.path import normpath

            result = None
            try:
                result = normpath(winshell.desktop())
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)

            return result
    class Path:
        # This class do path combined job.
        class Complement:
            def merge_manually(first, second):
                """MUST_SUCCESS_METHOD
                Usage:
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
                MUST_SUCCESS_METHOD
                """
                import os
                from os.path import normpath
                
                # This is result.
                result = None 
                # Use this to confirm if os.path.join, the system method is
                # success.
                success = False
                
                # Try merge path by system method.
                try:
                    Console.ansi_print("Merging path(system method):\n\t{}, {}".format(first, second))

                    result = normpath(os.path.join(first, second))
                    success = True # Set success var to true once os.path.join is success.

                    Console.ansi_print("\tMerge path success:\n\t{}".format(result))
                except Exception as err:
                    Process.handle_exception(err, False)
                    Console.ansi_print("\nMerge path by system method failed.\n")
                    Console.ansi_print("Try manually merge.")
                    
                # Try merge manually if system method is failed.
                if success is not True:
                    try:
                        Console.ansi_print("Merging path(manually method):\n\t{}, {}\n".format(first, second))
                        
                        result = Environment.Path.Complement.merge_manually(first, second)
                        result = normpath(result)
                        
                        Console.ansi_print("\tMerge path success:\n\t{}".format(result))
                    except Exception as err:
                        Process.handle_exception(err, False)
                        sys.exit(-42)

                return result
        def sys_norm_path(path):
            """Alternative method for os.path.normpath.
            Yet another common system method may failed for unknown reason.
            MUST_SUCCESS_METHOD"""
            from os.path import normpath

            result = None
            try:
                result = normpath(path)
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)

            return result

        def get_full_work_dir():
            """Return current working directory.
            MUST_SUCCESS_METHOD
            If can't get current working directory(for any reason),
            print error message and close the program for exit code -42.

            The program is not able to run successfully without a vailed working directory.
            """
            import os

            result = None
            try:
                result = os.getcwd()
            except Exception as e:
                Process.handle_exception(e, False)
                sys.exit(-42)
                
            return result

        def merge_path_with_work_dir(path_name): 
            """Return a path with working dir.
            Give a name, use this method to get a full path with current working directory.
            
            <Dirve>:\<working_dir_path>\<path_name>
            """           
            result = None

            # pwd come from a Linux CLI command.
            pwd = Environment.Path.get_full_work_dir()
            result = Environment.Path.Complement.merge_system(pwd, path_name)

            return result