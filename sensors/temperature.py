import Adafruit_DHT as DHT
import time

class Temperature:
    def __init__(self, pin=4):
        self.pin = pin
        self.model = DHT.DHT11

    """
    Read data from dht sensor

    Read the humidity and temperature from dhtp sensor

    Returns:

    """    
    def read(self):
        total_temperature = 0
        i = 0

        while i < 5:
            _, temperature = DHT.read(self.model, self.pin)
            if temperature == None:
                continue
            
            total_temperature += temperature

            i += 1
            time.sleep(0.2)
        
        temperature = total_temperature / 5

        return temperature