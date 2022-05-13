import RPi.GPIO as GPIO

from .executor import Executor


class Fans(Executor):
    def __init__(self, pin=11):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def setOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def setOff(self):
        GPIO.output(self.pin, GPIO.LOW)
