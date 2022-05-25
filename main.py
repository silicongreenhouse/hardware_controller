#!/usr/bin/python3

import json
import os
import time

from executors.fans import Fans
from executors.water_pump import WaterPump

from sensors.moisure import Moisure
from sensors.temperature import Temperature
from sensors.ultrasounds import Ultrasounds


# Read a dictionary and load events into an array
def load_events(events_data):
    for sensor in events_data["sensors"]:
        try:
            for event in sensor["events"]:
                event["sensor"] = sensor["id"]
                events.append(event)

        except:
            continue


# Get an event and check sensors based on event data
def event_listener(event):
    sensor = sensors[event["sensor"]]
    executor = executors[event["executor"]]
    state = event["state"]
    set_state = False

    while True:
        if event["sensor"] == "s3":
            if event["value"] == sensor.read():
                set_state = True
        else:
            if event["above"] != 0:
                if event["above"] > sensor.read():
                    set_state = True
                else:
                    set_state = False

            if event["equal"] != 0:
                if event["equal"] == sensor.read():
                    set_state = True
                else:
                    set_state = False

            if event["below"] != 0:
                if event["below"] < sensor.read():
                    set_state = True
                else:
                    set_state = False

        if set_state:
            executor.setState(state)
        time.sleep(1)


events = []
sensors = {"s1": Temperature(), "s2": Ultrasounds(), "s3": Moisure()}
executors = {"e1": Fans(), "e2": WaterPump()}

file = open(os.getenv("CONFIG_PATH"), "r")
data = json.loads(file.read())
file.close()


load_events(data)
