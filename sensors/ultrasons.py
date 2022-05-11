from gpiozero import DistanceSensor
import time

class Ultrasons:
    def __init__(self):
        self.sensor = DistanceSensor(echo=27, trigger=22, max_distance=500)

    def mesura(self):
        distancia = self.sensor.distance
        return distancia *100