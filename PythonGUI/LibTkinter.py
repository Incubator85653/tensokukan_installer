from tkinter import *

# sample
#fileDialog = Tk()

# visible again
#fileDialog.deiconify()

# close
#fileDialog.destroy()

class RootVar:
    UniversalExitButton = None

def InitializeLibTkinter():
    RootVar.LibTkHiddenWindow = Tk()
    RootVar.LibTkHiddenWindow.withdraw()
    return
class FileDialog:
    def AskDirectoryName(options):
        dirname = filedialog.askdirectory(**options)
        return dirname
    def AskFileName(options):
        filename = filedialog.askopenfilename(**options)
        return filename
class Window:
    def InitializeWindow(window, propDict):
        window.geometry(propDict['Geometry'])
        window.title(propDict['Title'])

        window.grid()
        return
    # Every single mainloop should refer to this method.
    # If the program running on other platform, mainloop is not necessary...
    # Disable one mainloop that all mainloop can be disabled.
    def ShowWindow(window):
        window.mainloop()
        return
    # Update before destroy to prevent a "tkinter destroy ThemeChanged" error.
    def SafeDestroy(window):
        window.update()
        window.destroy()
        return
    def CleanWidgets(window):
        for widgets in window.children.values():
            widgets.place_forget()
        return
    def StrNotice(str):
        from tkinter import messagebox
        mBox = messagebox.showinfo(message = str)
    def ArrayNotice(array):
        from LibPython import UnitConversion
        
        line = UnitConversion.FormatArray2String(array)
        Window.StrNotice(line)
        return
    def ExitWizard():
        import sys
        sys.exit()
        return
    def UnivWizardController_Place(window, widgetNextButton):
        from LibInstallProfile import DecodedProfile
        exitLocale = DecodedProfile.Config.StringYaml['TskInstTheWizard']['Exit']
        # 1 width = 8 px
        # Default height is 30 px.

        # Do not use in bootstrap.
        # The reason is bootstrap manage it's exit button itself.
        RootVar.UniversalExitButton = Button(window,
                                             text = exitLocale,
                                             command = lambda: Window.ExitWizard(),
                                             width = 10)
        RootVar.UniversalExitButton.place(x = 540, y = 430)
        widgetNextButton.place(x = 450, y = 430)

        window.update()
        return
    def UnivWizardController_Hide(window, widgetToHide):
        RootVar.UniversalExitButton.place_forget()
        widgetToHide.place_forget()

        window.update()
        return
    def UnivWizardHint_Place(window, widgetHintButton):
        widgetHintButton.place(x = 360, y = 430)

        window.update()
        return