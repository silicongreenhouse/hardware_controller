import Adafruit_DHT as DHT

class HumitatTemperatura:
    def __init__(self, pin):
        self.pin = pin
        self.model = DHT.DHT11
    
    def read(self):
        humidity, temperature = DHT.read(self.model, self.pin)
        return humidity, temperature