import threading
import json
import os
import time
from sensors.humitat_temperatura import HumitatTemperatura
from sensors.ultrasons import Ultrasons
from sensors.moisure import Moisure
import RPi.GPIO as GPIO

## No es toca s'ha de posar en aquest mode abans d'utilitzar qualsevol sensor
GPIO.setmode(GPIO.BOARD)

config_path = os.environ["CONFIG_PATH"]
config_file = open(config_path)
config = json.load(config_file)
print(config["sensors"][0]["events"][0])

sensor = Moisure()
x = threading.Thread(target=Moisure)
while True:
    print(sensor.read())
    time.sleep(1)
