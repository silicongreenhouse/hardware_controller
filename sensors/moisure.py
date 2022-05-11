import RPi.GPIO as GPIO

class Moisure:
    def __init__(self, pin=37):
        self.pin = pin
    
    def read(self):
      return GPIO.input(self.pin) == 0