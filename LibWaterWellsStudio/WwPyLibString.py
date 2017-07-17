import sys
from LibOperate import WaterWellsYaml as wwYaml

string_dict = wwYaml.read_yaml_from_disk('{}.yaml'.format(sys.stdin.encoding))

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