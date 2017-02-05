#!/usr/bin/env python3
# send AdafruitIO
from Adafruit_IO import Client
import settings
# set-up
settings.webgui()
ADAFRUIT_IO_KEY = settings.key
web = Client(ADAFRUIT_IO_KEY)
# main
web.send('Temp', )
web.send('Humd', h)
# receive AdafruitIO
data = web.receive('test1')
print("test1 data",data.value)

