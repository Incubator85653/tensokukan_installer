import locale
from os import path
from LibOperate import WaterWellsYaml as wwYaml

# Create string absolute path
pyLocation = path.dirname(path.abspath(__file__))
# 'lang' is the folder name of lang pack folder.
formula = r'{0}\lang\{1}.yaml'
# Example: r'.\lang\cp437.yaml'
dict_path = formula.format(pyLocation, locale.getdefaultlocale()[0])

# Alternative/Universal English library string if the lang is not supported.
if path.isfile(dict_path) is not True:
    dict_path = formula.format(pyLocation, 'cp437')
string_dict = wwYaml.read_yaml_from_disk(dict_path)

headers_dict = string_dict['headers_dict']
hint_dict = string_dict['hint_dict']
warn_dict = string_dict['warn_dict']
error_dict = string_dict['error_dict']

class Headers:
    hint_header = headers_dict['hint_header']
    error_header = headers_dict['error_header']
    warn_header = headers_dict['warn_header']
    broken_system = headers_dict['broken_system']

class HintString:
    # Hints have header.
    trying_manually_path_join = hint_dict['trying_manually_path_join']
    
    # No header hints.
    external_command = hint_dict['external_command']
    error_begin = hint_dict['error_begin']
    error_end = hint_dict['error_end']
    
class ErrorString:
    # Errors have header.
    os_path_normpath_failed = Headers.error_header + error_dict['os_path_normpath_failed'] + Headers.broken_system
    os_getcwd_failed = Headers.error_header + error_dict['os_getcwd_failed'] + Headers.broken_system
    # No header errors.
class WarnString:
    # Warns have header.
    os_path_join_failed = Headers.warn_header + warn_dict['os_path_join_failed'] + Headers.broken_system
    # No header warns.