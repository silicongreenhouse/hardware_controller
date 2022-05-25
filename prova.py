import asyncio
import json
import websockets
import time
import RPi.GPIO as GPIO

from sensors.ultrasons import Ultrasons
from sensors.temperature import Temperature
from sensors.moisure import Moisure

GPIO.setmode(GPIO.BOARD)

ultrasounds = Ultrasons()
temperature = Temperature()
moisure =Moisure()

sensor_data = {
    "temperature": 0,
    "water_level": 0,
    "floor_humidity": "low",
}
async def send_sesor_data():
    async with websockets.connect("ws://172.16.251.176:3000/ws_raspberry") as websocket:
        while True:
            distance = ultrasounds.read()
            distance = round(distance, 2)
            # temp = temperature.read()
            humidity = moisure.read()
            sensor_data["water_level"] = distance
            sensor_data["floor_humidity"] = humidity
            # sensor_data["temperature"] = temp
            await websocket.send(json.dumps(sensor_data))
            response = await websocket.recv()
            print(response)
            await asyncio.sleep(1.5)

asyncio.run(send_sesor_data())