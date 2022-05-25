import RPi.GPIO as GPIO

from .executor import Executor


class Fans(Executor):
    def __init__(self, pin=11):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def setState(self, state):
        if state == "on":
            GPIO.output(self.pin, GPIO.HIGH)
        elif state == "off":
            GPIO.output(self.pin, GPIO.LOW)