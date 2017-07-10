import sys
sys.path.append("..\LibWaterWellsStudio")
from LibOperate import Yaml

class Variable:
    firstTimeEdit = None
    
    Encoding = None
    Source = None
    Target = None
    OptionArray = None
    class OptionArrayContents:
        OptionGroupDict = None
        class DecodedOption:
            Group = None
            Mark = None
            Option = None
            Value = None

class Parser:
    # Parse each option array.
    # Example: GameExePath
    # Under the dict, there're also Group, Mark, Option, Value
    def get_undecoded_option_dict():
        for option_group_name in Variable.OptionArrayContents.OptionGroupDict:
            undecodedOption = Yaml.get_yaml_content_by_its_name(
                option_group_name, Variable.OptionArrayContents.OptionGroupDict)

            Variable.OptionArrayContents.DecodedOption.Group = undecodedOption['Group']
            Variable.OptionArrayContents.DecodedOption.Mark = undecodedOption['Mark']
            Variable.OptionArrayContents.DecodedOption.Option = undecodedOption['Option']
            Variable.OptionArrayContents.DecodedOption.Value = undecodedOption['Value']

            Editor.do_modify()
            # Mark the file as edited.
            Variable.firstTimeEdit = False;

    # Parse option array.
    # Example: - GameExePath
    # the array. One array have only one dictionary.
    def decode_option_array_contents():
        # An item in array is directly is a dictionary, so don't need extra parse, notice that.
        for per_option_dict in Variable.OptionArray:
            Variable.OptionArrayContents.OptionGroupDict = per_option_dict
            Parser.get_undecoded_option_dict()

    # Parse file's properties, like encoding, file location, option array.
    # Example: Encoding, Source, Target, OptionArray
    def analysis_file_properties(per_file_dictionary, args):
        Variable.Encoding = per_file_dictionary['Encoding']
        Variable.Source = per_file_dictionary['Source'].format(args.folder)
        Variable.Target = per_file_dictionary['Target'].format(args.folder)
        Variable.OptionArray = per_file_dictionary['OptionArray']
        #print("Encoding: {}\nSource: {}\nTarget: {}\nObject:".format(
        #    encoding, source,
        #    target))
        Parser.decode_option_array_contents()

    # Parse each file dictionary in config file.
    # Example: Tsk_MainConfig
    def decode_per_file_dictionary(master_dictionary, args):
        for dictName in master_dictionary:
            per_file_dict = Yaml.get_yaml_content_by_its_name(dictName, master_dictionary)
            
            Parser.analysis_file_properties(per_file_dict, args)
            # Make first time edit condition as true at the end of the for loop,
            # prepaid for next file
            Variable.firstTimeEdit = True;
    
    # Wrapper method
    def do_edit(master_dictionary, args):
        Parser.decode_per_file_dictionary(master_dictionary, args)

class Editor:
    def modify_rules(groupName, optionName, optionValue, endOfLine):
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

        # Add EOL
        if EOL == True:
            fixedResult = result + '\n'
        else:
            fixedResult = result

        return fixedResult
    def get_replaced_line(line):
        groupName = Variable.OptionArrayContents.DecodedOption.Group
        optionMark = Variable.OptionArrayContents.DecodedOption.Mark
        optionName = Variable.OptionArrayContents.DecodedOption.Option
        optionValue = Variable.OptionArrayContents.DecodedOption.Value
                

        if line.find(optionMark) != -1:
            result = Editor.modify_rules(groupName, optionName, optionValue, True)
        else:
            result = line
        return result

    # Known issue: if loop edit directly, it only do single modify.
    # Because each modify read same unmodified template file.
    # To solve this, write the first modified file,
    # then read this new file instead of the unmodified template file.
    def do_modify():
        # UTF-8: utf8
        # ANSI: mbcs
        # All source file(read) would be UTF-8 format.

        # Open file, input and output.
        # Remember to close() this file at the end!
        templateFile = open(Variable.Source, 'r', encoding = 'utf8')
            
        # A for loop to modify config.
        if Variable.firstTimeEdit == True:
            lineList = templateFile.readlines()
            with open(Variable.Target, 'w', encoding = Variable.Encoding) as outputFile:
                for line in lineList:
                    result = Editor.get_replaced_line(line)
                    outputFile.write(result)

            firstTimeEdit = False
        elif Variable.firstTimeEdit == False:
            # Open and read wrote file to memory.
            inputFile = open(Variable.Target, 'r', encoding = Variable.Encoding)
            lineList = inputFile.readlines()
            inputFile.close()

            # Overwrite the wrote file use 'w'.
            with open(Variable.Target, 'w', encoding = Variable.Encoding) as outputFile:
                for line in lineList:
                    result = Editor.get_replaced_line(line)
                    outputFile.write(result)

        templateFile.close()
        return