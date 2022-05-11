import Adafruit_DHT as DHT

class HumitatTemperatura:
    def __init__(self, pin):
        self.pin = pin
        self.model = DHT.DHT11

    """
    Read data from dht sensor

    Read the humidity and temperature from dhtp sensor

    Returns:

    """    
    def read(self):
        humidity, temperature = DHT.read(self.model, self.pin)
        return humidity, temperature