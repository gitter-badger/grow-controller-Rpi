#!/usr/bin/env python3

import Adafruit_DHT as dht
import time
import os
import datetime
import settings
settings.pins()
pin5 = settings.dhtsensor

while True:
  h,t = dht.read_retry(dht.DHT22, pin5) #read DHT22 value, set pi
  print(time.strftime('%X %x %Z'))
  print('T={0:0.1f}*C\nH={1:0.1f}%'.format(t, h))
  time.sleep(8.0)
  os.system('clear')
  temp()
