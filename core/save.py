"""
Handles saving objects as pickles and encrypting
"""
import os
import time

import jsonpickle
import json
# import pickle
# from cryptography.fernet import Fernet

from core.files import get_game_root, check_path
from core.configs import get_value, change_config

# key = b'9kuDNxazpWoLSeDo9RBbtcCzaYuCzKbgX5m46MY_gqY='
# cipher_suite = Fernet(key)

extension = get_value("save", "extension")


def save_to_file(game_save, file_name, saves_path=None):
    """Pickles, encrypts, and saves to file_path"""

    if isinstance(saves_path, type(None)):
        saves_path = get_saves_path()

    file_path = saves_path + file_name + "temp"

    time.sleep(.003)
    output = open(file_path, 'w')
    json.dump(jsonpickle.encode(game_save), output)
    output.close()
    if os.path.isfile(file_path[:-4]):
        os.remove(file_path[:-4])
    os.rename(file_path, file_path[:-4])


def load_from_file(file_name, saves_path=None):
    """Loads from file_path, decrypts, and depickles"""

    if isinstance(saves_path, type(None)):
        saves_path = get_saves_path()

    file_path = saves_path + file_name

    inp = open(file_path, 'r')
    input_str = inp.read() # cipher_suite.decrypt(bytes(inp.read()[2:-1], "UTF-8"))
    inp.close()
    game_save = jsonpickle.decode(json.loads(input_str))
    return game_save


def load(_save):
    """Returns the save stored in the config or makes a new one.

    :type _save: Save
    :param _save: Used to create a new save file when necessary
    :returns: path to file, if new file was created
    """

    save_file_path = get_saves_path()
    save_file_name, new = get_save_file_name(_save)

    return load_from_file(save_file_path + save_file_name + "."
                          + extension), new


def save(_save):
    """Saves to file based on current config's listed save path, etc.

    :type _save: Save
    """

    save_file_path = get_saves_path()
    save_file_name = get_save_file_name(_save)[0]

    save_to_file(save_file_path + save_file_name + "." + extension, _save)


def get_save_file_name(_save):
    """Returns the name of the save file in the config and creates a new one
     if missing.

    :type _save: Save
    :param _save: Used to create a new save file when necessary
    :rtype: str, bool
    :returns: save file name, if new file was created
    """

    new = False
    save_file_path = get_saves_path()
    save_file_name = get_value("save", "save_file")
    if isinstance(save_file_name, type(None)) \
            or not os.path.exists(save_file_path + save_file_name
                                  + "." + extension):
        # No file saved to config or saved file is missing

        # Get highest available number for file name
        highest_file = -1
        for file in os.listdir(save_file_path):
            if file.endswith("." + extension):
                file_num = -1
                try:
                    file_num = int(file[:-len("." + extension)])
                except ValueError:
                    continue
                if file_num > highest_file:
                    highest_file = file_num

        save_file_name = str(highest_file + 1)
        full_path = save_file_path + save_file_name + "." + extension
        file = open(full_path, "w")
        file.close()
        save_to_file(full_path, _save)
        change_config("save", "save_file", "'" + save_file_name + "'")
        print("Creating new save file")
        new = True
    return save_file_name, new


def get_saves_path():
    """Returns the path to the saves folder and creates new one if missing"""

    stored_path = get_value("save", "saves_path")\
        .replace("~Game Root~", get_game_root())

    check_path(stored_path)
    return stored_path


# OLD UNUSED FUNCTIONS:
def get_save_file_data(save_file):
    """Returns metadata for file given

    :type save_file: str
    """

    return time.strftime('%m/%d/%Y', time.gmtime(
        os.path.getctime(get_saves_path() + save_file)))
