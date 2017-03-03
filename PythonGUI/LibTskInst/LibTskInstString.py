import LibTskInstPython as TheCfg
stringDict = TheCfg.yaml_loader(r'Resources\zh-CN\Config\String.yaml')
class TskInstStringTheWizard:
    yaml = stringDict.get('TskInstStringTheWizard')
    # basic properties to initalize installer window
    InstallerTitle = yaml.get('InstallerTitle')
    InstallerGeometry = yaml.get('InstallerGeometry')

class LibTskInstStepWizardMode:
    yaml = stringDict.get('LibTskInstStepWizardMode')

    labelTextStartInstall = yaml.get('labelTextStartInstall')
    labelTextWizardModeSelect = yaml.get('labelTextWizardModeSelect')
    labelTextNovice = yaml.get('labelTextNovice')
    labelTextAdvanced = yaml.get('labelTextAdvanced')
    labelTextDebugWarn = yaml.get('labelTextDebugWarn')
    labelTextDebugWarn2 = yaml.get('labelTextDebugWarn2')
    popupUseDebugMode = '新手模式没做好，用第2个吧。'

    buttonTextNextStep = yaml.get('buttonTextNextStep')
    buttonTextExit = yaml.get('buttonTextExit')

    # Don't modify when you're doing a translate.

    # Wizard mode and radiobutton
    wizardModeNovice = 1
    wizardModeDebug = 2
class LibTskInstStringTkinter:
        # ext = extension
        # these line are sample, not in use, and don't remove
        # tskCfg is the characteristic you can change
        tskCfgBrowseAllFilesName = 'all files'
        tskCfgBrowseAllFilesExt = '.*'
        tskCfgBrowseInitialfileName = 'config.yaml'
        tskCfgBrowseFileTypeName = 'tsk_report config'
        tskCfgBrowseFileTypeExt = '.yaml'

        tskCfgBrowseDialogTitle = 'Select your ID yaml'
class LibTskInstStringStepId:
    labelTextTencoID = 'Tenco ID:'
    radioTextTypeIn = '稍后手动输入ID和密码。'
    radioTextFromYaml = '从旧版的config.yaml导入。'
    radioTextRegister = '注册新的ID。'
    radioTextSkipId = '不设置ID（跳过）。'

    buttonTextBrowseYaml = '浏览'
    buttonTextNextStep = '保存'
    # Not in use
    exitButton = '退出'
    # Do not change following text
    installTypeNew = 1
    installTypeUpgrade = 2

    idInstallTypeManually = 1
    idInstallTypeYaml = 2
    idInstallTypeRegisterNew = 3
    idInstallTypeSkip = 4

    defaultFilesExt = '.yaml'



class TskInstStringStepBasicDebug:
    labelTextSelectedAdvancedMode = '选择了Debug Mode。'
    labelTextTskInstallPath = '安装到这:'
    # TEMP location MUST NOT contains CJK characters like "C:\假猪套天下第一\tsk".
    labelTextTskTempPath = 'Temp文件夹:'

    radioTextNewInstall = '新的安装'
    radioTextUpgrade = "升级"

    buttonTextBrowseTskInstallPath = '浏览'
    buttonTextBrowseTskTempPath = '浏览'

    dialogTitleBrowseTskInstallPath = '选择天则观安装目录'
    dialogTitleBrowseTskTempPath = '选择天则观Temp目录'

    buttonTextNextStep = '保存'
    buttonTextExit = '退出'

    labelTextSelectedNewInstall = '选择了“新的安装”。'
    labelTextSelectedUpgrade2 = '选择了“升级”'
    popupCantUpgrade = '现在不能升级，只能新安装。'

    # Do not change following text if you're doing a translate
    radioStorageInstallTypeNew = 1
    radioStorageInstallTypeUpgrade = 2
class TskInstStringStepId:
    class TypeIn:
        labelTextTitle = '输入天则观ID:'
        labelTextId = 'ID:'
        labelTextPassword = '密码:'
        labelTextSuggest1 = '推荐保存以前检查下密码对不对，'
        labelTextSuggest2 = '输入ID以后点这个检查按钮，'
        labelTextSuggest3 = '或者直接保存。'

        buttonTextCheck = '检查'
        buttonTextNextStep = '保存'

        idFirst = '检查以前先输入ID。'
        beforeSave = '两个都输入了才能保存。'
class TskInstStringStepGame:
    entryTextConnectGame = '选择最常用的游戏版本。'

    entryTextGameInstalledPath = '游戏exe(th123.exe):'
    buttonTextBrowseGameExec = '浏览'

    entryTextGameVersion = '游戏版本（标题栏）:'

    buttonTextNextStep = '保存'
class TskInstStringStepShortcuts:
    labelTitleCreateShortcuts = 'Create the shortcuts.'
    labelTextCreateStartMenu = 'Start menu:'
    labelTextCreateDesktop = 'Desktop:'

    entryStorageStartMenuDefaultDirName = 'Tensokukan International Edition'
    entryStorageDesktopDefaultShortcutsName = 'Tensokukan.lnk'

    checkbuttonTextDntstartMenu = 'Do not create startup menu shortcuts.'
    checkbuttonTextDntDesktop = 'Do not create desktop shortcuts.'

    buttonSave = 'Save'
    buttonExit = 'Exit'
    buttonResetDefaultNames = 'Reset as default shortcuts name'
class TskInstStringStepInstalling:
    labelTitleInstalling = 'Installing your Tensokukan program.'

    labelTitleCurrentStatus = 'Current status:'
    labelTitleTotalStatus = 'Total status:'

    labelTotalOperationCheckDir = 'Check install directory...'
    labelTotalOperationInstalling = 'Installing...'

    labelOperationPreprocessing = 'Preprocess...'
    labelOperationUnpackingProgram = 'Unpack program files...'
    labelOperationInstallUpdate = 'Install updates...'
    labelOperationSaveSettings = 'Save settings...'
    labelOperationSetProgramVer = 'Set installed program version...'

    labelOperationBackupData = 'Backup exist user data...'
    labelOperationRemoveOldVer = 'Uninstall exist version...'

    labelOperationDone = 'Done.'
    readPoetry = '苟利国家生死以，岂因祸福避趋之'
class TskInstStringStepInstall:
    labelTextInstalling = '安装中……'
    labelTextDone = '安装完了。点退出。'
    buttonTextExit = '退出'
class TskInstStringStepDataImport:
    labelTextImportDataPart1 = 'Import old version Tensokukan user data(1/2).'
    labelTextImportDataPart2 = 'Import old version Tensokukan user data(2/2)'

    labelTextTskIni = 'Tensokukan main ini config file(tsk.ini):'
    buttonTextBrowseTskIni = 'Not this one?'
    checkbuttonTextDntManageTskIni = 'Do not import main config.'

    labelTextTskDatabase = 'Database(default.db):'
    buttonTextBrowseDb = 'Browse'
    checkbuttonTextDntManageDb = 'Do not import database:'

    labelTextIdYaml = 'Saved Tenco ID and password(config.yaml):'
    buttonTextBrowseYaml = 'Not this one?'
    checkbuttonTextDntManageId = 'Do not import Tenco ID settings.'
    
    labelTextSWRSAddr = 'Connected game version(SWRSAddr.ini):'
    buttonTextBrowseSWRSAddr = 'Not this one?'
    checkbuttonTextDntSWRSAddr = 'Do not import connected game version settings.'
    checkbuttonTextChooseFromGameList = 'I want select a supported game version from the list.'

    buttonTextNextStep = 'Next Step'
    buttonTextSave = 'Save'
    buttonTextExit = 'Exit'
class TskInstStringErrors:
    # Basic
    errorTextInstallPathEmpty = 'You have not select the install path.'
    errorTextTempPathEmpty = 'You have not select temp file path.'
    errorTextInstallTypeNotSelected = 'You have not select a install type.\nNew install or upgrade.'
    # ID
    errorTextIdTypeNotSelected = 'You must specify a id install method.\nIn this version please type in your id manually.'
    errorTextRegisterUnavailable = 'Sorry, can\'t register right now.\nPlease to use another method.\nThe register feature is not implemented.'
    errorTextIdInstallYamlEmpty = 'You\'re using import config method,\nbut you have not select a yaml file.'
    errorTextImportYamlUnavailable = 'Sorry, can\'t import id from yaml right now.\nPlease to use another method.\nThe import feature is not implemented.'
    # Game
    errorTextGameExecPathEmpty = 'You have not select the game executeable file path(th123.exe).'
    errorTextGameVersionEmpty = 'You have not select your game version.'
    # Data import
    errorTextDatabasePathEmpty = 'You have not select the Tensokukan Database.'
    errorTextIdUpgradeYamlEmpty = 'You have not select the Tsk_report config yaml.'
    errorTextSWRSAddrPathEmpty = 'You have not select your SWRSAddr file.'
    errorTextTskIniEmpty = 'You have not select your Tsk main config.'
class TskInstStringHints:
    howToLibId = '第2、3个选项不能用。\n已经注册过ID需要登陆选1，没有注册过选4。'
    howToBasicDebug = '现在不能升级，只能新安装。\nTemp目录如果有中文，就得选一个不含有中文的路径。\n建议先去硬盘上建好天则观安装和Temp两个目录以后再点浏览。\n在浏览里点新建文件夹可能会卡死。'
    howtoId = '输入ID以后点检查会打开浏览器，\n密码框里输入密码以后右边的日语按钮是检查密码对不对，\n如果网页打开是404代表ID不存在。\n密码错了会显示 アカウント認証失敗！'
    howtoGame = '第一个是选择你游戏的exe，\n第二个是选游戏版本，如果你的游戏不在列表里就选 跳过。\n即使跳过，之后也必须提供一个SWRSAddr.ini才能正常使用天则观。'