import RPi.GPIO as GPIO
from .executor import Executor


class WaterPump(Executor):
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.setOff()

    def setOn(self):
        GPIO.output(self.pin, True)

    def setOff(self):
        GPIO.output(self.pin, False)
