import RPi.GPIO as GPIO

class Moisure:
    def __init__(self, pin=37):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    
    def read(self):
        gpio_input = GPIO.input(self.pin) == 0
        if gpio_input:
            return "high"
        else:
            return "low"