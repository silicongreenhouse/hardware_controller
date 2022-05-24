#!/usr/bin/python3

from hashlib import shake_128
import json
import RPi.GPIO as GPIO
import time
import threading

from sensors.temperature import Temperature
from sensors.ultrasons import Ultrasons
from sensors.moisure import Moisure
from executors.fans import Fans
from executors.water_pump import WaterPump

GPIO.setmode(GPIO.BOARD)

events = []
sensors = {"s1": Temperature(), "s2": Ultrasons(), "s3": Moisure()}
executors = {"e1": Fans(), "e2": WaterPump()}


def diccionari():
    while True:
        print(executors["e2"])

def ultraputa():
    while True:
        distance = ultrasounds.read()
        distance = round(distance, 2)
        print(f'Distancia: {distance}')
        time.sleep(1)

def humitat():
    while True:
        humidity = moisure.read()
        print(f'{humidity}')
        time.sleep(1)

# def temperaputa():
#     GPIO.setmode(GPIO.BOARD)
#     fans = Fans()

#     while True:
#         temperatura = temperature.read()
        
#         if (temperatura > 30):
#             fans.setOn()
#         else:
#             fans.setOff()

#         print(f'Temperatura: {temperatura}')
#         time.sleep(1)

file = open ('/home/greenhouse/config.json', "r")

data = json.loads(file.read())

for sensor in data["sensors"]:
    try:
        for event in sensor["events"]:
            event["sensor"] = sensor["id"]
            events.append(event)
            print(event)
            
    except:
        continue

print(diccionari)

file.close()

# distancia = threading.Thread(target=ultraputa)
# moisureThread = threading.Thread(target=humitat)
# distancia.start()
# moisureThread.start()