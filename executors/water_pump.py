import RPi.GPIO as GPIO
import time

class Water_pump:
    def __init__(self, pin=12):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
    
    def start(self):
        GPIO.output(self.pin, True)

    def end(self):
        GPIO.output(self.pin, False)