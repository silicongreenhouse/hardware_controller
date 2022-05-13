#!/usr/bin/python3

import threading
import json
import os
import RPi.GPIO as GPIO
import time

from executors.fans import Fans
from executors.water_pump import WaterPump
from sensors.temperature import Temperature
from sensors.moisure import Moisure
from sensors.ultrasons import Ultrasons

GPIO.setmode(GPIO.BCM)

ultrasounds = Ultrasons()

config_path = os.environ["CONFIG_PATH"]
config_file = open(config_path)

while True:
    print("do something")
    print(ultrasounds.read())
    print("do something")
    time.sleep(1)

GPIO.cleanup()