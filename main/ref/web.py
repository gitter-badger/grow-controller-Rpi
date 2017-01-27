#!/usr/bin/env python3

import Adafruit_DHT as dht
import time
import settings
from Adafruit_IO import Client

settings.webgui()
settings.pins()

ADAFRUIT_IO_KEY = settings.key1
aio = Client(ADAFRUIT_IO_KEY)
pin5 = settings.dhtsensor

while True:
    h,t = dht.read_retry(dht.DHT22, pin5) #read DHT22 value, set pi
    aio.send('Temp', t)
    aio.send('Humd', h)
    time.sleep(10.0)

