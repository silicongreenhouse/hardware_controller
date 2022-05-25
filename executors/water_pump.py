import RPi.GPIO as GPIO
from .executor import Executor


class WaterPump(Executor):
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.setOff()

    def setState(self, state):
        if state == "on":
            GPIO.output(self.pin, True)
        elif state == "off":
            GPIO.output(self.pin, False)