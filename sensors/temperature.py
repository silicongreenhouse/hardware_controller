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
        temperature = None

        while temperature == None:
            _, temperature = DHT.read(self.model, self.pin)
           
        return temperature
