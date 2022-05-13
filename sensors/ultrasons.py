from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import time

class Ultrasons:
    def __init__(self):
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.IN)
        self.sensor = DistanceSensor(echo=27, trigger=22, max_distance=500)

    def read(self):
        distancia = self.sensor.distance
        return distancia * 100