"""
Handles pulling values from configs and recreating broken/missing config files
"""
import os
from time import sleep
# from core.default_configs import *  # Necessary for importing configs
from core.default_configs import *
from core.files import get_game_root

reload_configs = False
max_access_attempts = 5


def get_configs_path():
    """Returns the path to the configs folder"""

    return get_game_root() + "Configs/"


def create_config(config):
    """Creates a config file and writes in respective default_config

    :type config: str
    """

    config_file = open(get_configs_path() + config + ".txt", "w")
    config_file.write(eval(config))  # Imported config written to file
    config_file.close()


def get_value(config, key=None, eval_config=True, regen_config=False,
              attempt=0):
    """Finds or creates the given config and pulls the value from its dict

    :type key: str | None
    :type config: str
    :type regen_config: bool
    :type eval_config: bool
    :type attempt: int

    :param key: String key for value or None for entire config
    :param eval_config: If key is None, return config dict or string?
    :param regen_config: Used recursively if config is corrupt

    :rtype: Anything | dict | str
    """

    config_file_path = get_configs_path() + config + ".txt"

    # Check if config is missing or marked for deletion
    attempt_num = 0
    while attempt_num < max_access_attempts:
        try:
            if (reload_configs or regen_config) and os.path.exists(
                    get_configs_path()):
                # Auto deletes config for debugging or if specified
                for file in os.listdir(get_configs_path()):
                    os.remove(get_configs_path() + file)
                os.rmdir(get_configs_path())

            if not os.path.exists(get_configs_path()):
                # Recreates configs folder if missing
                os.mkdir(get_configs_path())

            if not os.path.exists(config_file_path):
                # Recreates config file if missing
                create_config(config)

        except IOError as exception:
            # Takes multiple tries sometimes
            print(exception.strerror + ". Attempts left: ",
                  max_access_attempts - attempt_num)
        else:
            break
        attempt_num += 1
        sleep(.1)

    config_file = open(config_file_path, "r")
    text = config_file.read()
    config_file.close()

    # Check if config needs regenned
    try:
        config_dict = eval(text)
    except SyntaxError as e:
        # Regen config if not evaluable
        print(config, "config syntax is broken, restoring to default")
        if attempt > 10:
            raise e
        attempt += 1
        return get_value(config, key, regen_config=True, attempt=attempt)

    if type(config_dict) != dict:
        # Regen config if not dict
        print(config, "config is not dict, restoring to default")
        attempt += 1
        if attempt > 10:
            raise Exception(config, "config is not dict")
        return get_value(config, key, regen_config=True, attempt=attempt)

    if isinstance(key, type(None)):
        # Return config as string or dict instead of getting value
        if eval_config:
            return config_dict
        return text

    if key not in config_dict.keys():
        # Regen config if missing key
        print(config, "config is missing key:",
              "'" + key + "'. Restoring to default")
        attempt += 1
        if attempt > 10:
            raise Exception(config, "config is missing key: ", "'" + key +
                            "'. Restoring to default")
        return get_value(config, key, regen_config=True, attempt=attempt)

    return config_dict[key]


def change_config(config_name, key, value):
    """Updates the given config with the new value.

    :type config_name: str
    :type key: str
    :type value: Anything
    """
    config_string = get_value(config_name, None, False)
    config = get_value(config_name, None, True)
    string_offset = 0
    if key in config and isinstance(config[key], str):  # TODO: Account for other .__str__()
        # variables that must include '
        string_offset = 2
    parts = ['', '']
    found_key = config_string.find("'" + key + "': ")
    if isinstance(value, str):
        value = "'" + value + "'"
    if found_key > -1:
        parts[0] = config_string[:found_key] + "'" + key + "': "
        parts[1] = config_string[
                   len(parts[0]) + len(str(config[key])) + string_offset:]
        new_config_string = parts[0] + str(value) + parts[1]
    else:
        parts[0] = config_string[:-1]
        parts[1] = "\n}"
        new_config_string = parts[0] + "'" + str(key) + "': " + str(value) + ",\n" + parts[1]
    config_path = get_configs_path() + config_name + ".txt"
    os.remove(config_path)
    config_file = open(config_path, "w")
    config_file.write(new_config_string)
    config_file.close()


def list_to_dict(_list):
    """Converts a list of dicts into a dict of dicts using the 'Name' key
    from the dicts in the list as the key for the dict in the dict of dicts"""

    _dict = {}
    for item in _list:
        if type(item) == dict:
            _dict[item["Name"]] = item
        else:
            _dict[item.name] = item
    return _dict