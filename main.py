import threading
import json
import os

config_path = os.environ["COONFIG_PATH"]
config_file = open(config_path)
config = json(config_file)
print(config)
