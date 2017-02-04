#!/usr/bin/env python3

from Adafruit_IO import Client
import time
import settings

settings.webgui()
ADAFRUIT_IO_KEY = settings.key
web = Client(ADAFRUIT_IO_KEY)

while True:
    data = web.receive('test1')
    time.sleep(1.0)
    print("test1 data",data.value)

