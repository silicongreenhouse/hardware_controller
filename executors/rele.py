import RPi.GPIO as GPIO

class Relay:
   def __init__(self, pin):
      self.pin = pin
   
   def close(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.OUT)
      
      try:
         GPIO.output(self.pin, GPIO.HIGH)
      except KeyboardInterrupt:
         print("Keyboard interrupt")
      except:
         print("Some error")
      finally:
         GPIO.cleanup()

   def open(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.OUT)
      
      try:
         GPIO.output(self.pin, GPIO.LOW)
      except KeyboardInterrupt:
         print("Keyboard interrupt")
      except:
         print("Some error")
      finally:
         GPIO.cleanup()