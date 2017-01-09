#!/usr/bin/env python3

import Adafruit_DHT as dht
import time
import os
from datetime import datetime
import settings
settings.pins()
pin5 = settings.dhtsensor
now = datetime.now()
now_time = now.time()
while True:
    h,t = dht.read_retry(dht.DHT22, pin5) #read DHT22 value, set pi
    print(now_time)
    print("temp", t, "\nhum", h)
    time.sleep(8.0)
    os.system('clear')
