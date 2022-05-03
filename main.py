import Adafruit_DHT
import time
from sensors.humtat_temperatura import HumitatTemperatura

DHT_SENSOR = HumitatTemperatura(4)

while True:
  humidity, temperature = DHT_SENSOR.read()
  print(f'{humidity}% {temperature}*C')
  time.sleep(2)