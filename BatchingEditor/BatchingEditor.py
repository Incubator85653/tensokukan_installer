#!/usr/bin/python3
import argparse
import os
import LibEditor

# Add search path
import sys
sys.path.append("..\LibWaterWellsStudio")
# import shared library
from LibOperate import WaterWellsYaml as libYaml
from LibPython import Console

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("yaml_path", help="Specify a yaml file edited by installer.")
parser.add_argument("resouce_folder", help = "Specify a folder contains the source and target file. A path without slash, typically is installed folder.")

# Put arguments into variables
args = parser.parse_args()
str_config_path = args.yaml
bool_config_exist = os.path.isfile(str_config_path)

# The file exist, then start file processing
if bool_config_exist:
    config_dict = libYaml.read_yaml_from_disk(str_config_path)

    LibEditor.Parser.do_edit(config_dict, args)
# Otherwize return -1 as exit value and put a hint.
else:
    Console.ansi_print("The specified yaml config file is not vailed.")
    sys.exit(-1)