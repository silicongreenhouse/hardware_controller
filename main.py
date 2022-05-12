import threading
import json
import os

config_path = os.environ["CONFIG_PATH"]
config_file = open(config_path)
config = json.load(config_file)
print(config)
