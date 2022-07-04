import importlib.resources as pkg_resources
import json
import ast

from epibox import common


def get_default(username):

    try:
        with open(
            "/home/{}/Documents/epibox/args.json".format(username), "r"
        ) as json_file:
            defaults = json_file.read()
            defaults = ast.literal_eval(defaults)

    except Exception as e:  # the first time using EpiBOX Core, there will be no default file
        defaults = {
            "initial_dir": "EpiBOX Core",
            "fs": 1000,
            "channels": [],
            "devices_mac": {"MAC1": "12:34:56:78:91:10", "MAC2": "01:19:87:65:43:21"},
            "save_raw": "true",
            "patient_id": "default",
            "service": "Bitalino",
        }

        with open(
            "/home/{}/Documents/epibox/args.json".format(username), "w+"
        ) as json_file:
            json.dump(defaults, json_file)

    return defaults
