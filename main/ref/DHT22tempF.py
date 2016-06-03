import Adafruit_DHT as dht

h,t = dht.read_retry(dht.DHT22, 17)
print t * 9/5.0 + 32
