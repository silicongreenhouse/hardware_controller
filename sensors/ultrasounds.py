from gpiozero import DistanceSensor
import time

class Ultrasounds:
    def __init__(self):
        self.sensor = DistanceSensor(echo=27, trigger=22, max_distance=500)

    def read(self):
        distancia = self.sensor.distance
        return distancia * 100
