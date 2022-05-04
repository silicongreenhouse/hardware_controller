import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT)
try:
    GPIO.output(17, GPIO.HIGH)
    time.sleep(10)
except KeyboardInterrupt:
   print("Keyboard interrupt")

except:
   print("some error")

finally:
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()