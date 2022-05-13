import RPi.GPIO as GPIO
from .executor import Executor


class WaterPump(Executor):
    def __init__(self, pin=12):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def setOn(self):
        GPIO.output(self.pin, True)

    def setOff(self):
        GPIO.output(self.pin, False)
