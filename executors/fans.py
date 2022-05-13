import RPi.GPIO as GPIO
from executor import Executor


class Fans(Executor):
    def __init__(self, pin):
        GPIO.setup(self.pin, GPIO.OUT)
        self.pin = pin

    def setOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def setOff(self):
        GPIO.output(self.pin, GPIO.LOW)
