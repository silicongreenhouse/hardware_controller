import RPi.GPIO as GPIO

class Relay:
   def __init__(self, pin):
      GPIO.setup(self.pin, GPIO.OUT)
      self.pin = pin
   
   def close(self):
      GPIO.output(self.pin, GPIO.HIGH)

   def open(self):
      GPIO.output(self.pin, GPIO.LOW)
