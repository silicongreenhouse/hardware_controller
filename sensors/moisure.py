import RPi.GPIO as GPIO

class Moisure:
    def __init__(self, pin=26):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    
    def read(self):
      return GPIO.input(self.pin) == 0