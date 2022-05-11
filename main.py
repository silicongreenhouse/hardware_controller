from sys import exec_prefix
import time
from sensors.humitat_temperatura import HumitatTemperatura
from executors.rele import Relay

from sensors.ultrasons import Ultrasons


dht_sensor = HumitatTemperatura(4)
rele = Relay(17)
ultrasons = Ultrasons()

while True:
  humidity, temperature = dht_sensor.read()
  print(f'{humidity}% {temperature}*C')
  nivell_aigua = ultrasons.mesura()
  try:
    rele.open()
  except KeyboardInterrupt:
    print("Keyboard interrupt")
  except:
    print("some error")

  # finally:
  #   rele.open()
  #   rele.cleanup()

  print(nivell_aigua)

  time.sleep(1)
