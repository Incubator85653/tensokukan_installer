#!/usr/bin/python3
import argparse
import os
import LibEditor

# Add search path
import sys
sys.path.append("..\LibWaterWellsStudio")
# import shared library
from LibOperate import Yaml as libYaml

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("yaml", help="Specify a yaml file edited by installer.")
parser.add_argument("folder", help = "Specify a folder contains the source and target file. A path without slash, typically is installed folder.")

# Put arguments into variables
args = parser.parse_args()
config_path = args.yaml
config_is_exist = os.path.isfile(config_path)

# The file exist, then start file processing
if config_is_exist:
    config_file_readed = libYaml.read_yaml_from_disk(config_path)

    LibEditor.Parser.do_edit(config_file_readed, args)
# Otherwize return -1 as exit value and put a hint.
else:
    print("The specified yaml config file is not vailed.")
    sys.exit(-1)