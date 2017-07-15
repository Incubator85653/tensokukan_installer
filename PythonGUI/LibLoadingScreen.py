from tkinter import *
from sys import stdin
from os import getcwd
import LibPython as LibPython

tskInstallerBoot = Tk()

bootstrapDict = LibPython.yaml_loader('Bootstrap.yaml')
langArrayDict = bootstrapDict.get('Array')
langEncodingDict = bootstrapDict.get('Encoding')

shortLang = bootstrapDict.get('ShortLanguage').get(langEncodingDict.get(stdin.encoding))
guiStringDefaultDict = bootstrapDict.get('String').get(shortLang).get('Default')
#guiStringExtraDict = bootstrapDict.get('String').get(shortLang).get('Extra')
class Widgets:
    # Local variable
    checkbuttonStorageEncodingManually = IntVar()
    comboboxStorageLanguageList = StringVar()
    entryStorageCodePage = StringVar()

    comboboxStorageLanguageList.set(langEncodingDict.get(stdin.encoding))
    entryStorageCodePage.set(stdin.encoding)
    # Widgets
    labelSelectYourLanguage = None
    labelTutorial1 = None
    labelTutorial2 = None
    comboboxLanguageList = None
    labelEncodingManually = None
    checkbuttonEncodingManually = None
    labelCurrentEncoding = None
    entryCodePage = None

    buttonNextStep = None
    buttonExit = None
class Methods:
    def CopyBack():
        # zh-CN
        shortLang = bootstrapDict.get('ShortLanguage').get(langEncodingDict.get(stdin.encoding))
        # path
        resourcePath = r'{0}\Resources\{1}'.format(getcwd(), shortLang)
        pathDict = {'config' : r'{0}\Config'.format(resourcePath),
                    'archive' : r'{0}\Archive'.format(resourcePath),
                    'bin' : r'{0}\Bin'.format(resourcePath)}
        return
    def SwitchCodePageEditStatus(window):
        statusBool = bool(Widgets.checkbuttonStorageEncodingManually.get())
        Widgets.entryCodePage.destroy()
        if(statusBool):
            Widgets.entryCodePage = Entry(window,
                                          textvariable = Widgets.entryStorageCodePage,
                                          state = NORMAL)
        elif(statusBool is False):
            Widgets.entryCodePage = Entry(window,
                                          textvariable = Widgets.entryStorageCodePage,
                                          state = DISABLED)
        Widgets.entryCodePage.place(x = 85, y = 255)
        return
def ConfigureWidgets(window):
    Widgets.labelSelectYourLanguage = Label(window,
                                            text = guiStringDefaultDict.get('labelSelectYourLanguage'))
    Widgets.labelTutorial1 = Label(window,
                                   text = guiStringDefaultDict.get('labelTutorial1'))
    Widgets.labelTutorial2 = Label(window,
                                   text = guiStringDefaultDict.get('labelTutorial2'))
    Widgets.comboboxLanguageList = ttk.Combobox(window,
                                                state = 'readonly',
                                                textvariable = Widgets.comboboxStorageLanguageList,
                                                values = langArrayDict,
                                                width = 40)
    Widgets.labelEncodingManually = Label(window,
                                          text = guiStringDefaultDict.get('labelEncodingManually'))
    Widgets.checkbuttonEncodingManually = Checkbutton(window,
                                                      text = guiStringDefaultDict.get('checkbuttonEncodingManually'),
                                                      variable = Widgets.checkbuttonStorageEncodingManually,
                                                      command = lambda : Methods.SwitchCodePageEditStatus(window))
    Widgets.labelCurrentEncoding = Label(window,
                                         text = guiStringDefaultDict.get('labelCurrentEncoding'))
    Widgets.entryCodePage = Entry(window,
                                  textvariable = Widgets.entryStorageCodePage,
                                  state = DISABLED)

    Widgets.labelSelectYourLanguage.place(x = 25, y = 25)
    Widgets.labelTutorial1.place(x = 55, y = 55)
    Widgets.labelTutorial2.place(x = 55, y = 85)
    Widgets.comboboxLanguageList.place(x = 95, y = 115)
    Widgets.labelEncodingManually.place(x = 55, y = 165)
    Widgets.checkbuttonEncodingManually.place(x = 55, y = 195)
    Widgets.labelCurrentEncoding.place(x = 55, y = 225)
    Widgets.entryCodePage.place(x = 85, y = 255)

    return
def Wrapper():
    ConfigureWidgets(tskInstallerBoot)
    tskInstallerBoot.mainloop()
    return