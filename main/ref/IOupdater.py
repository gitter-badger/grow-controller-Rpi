
import settings
from Adafruit_IO import Client


settings.webgui()
guienable = settings.enable1
ADAFRUIT_IO_KEY = settings.key1
web = Client(ADAFRUIT_IO_KEY)

settings.light()
lightOn = settings.lightOn
lightOff = settings.lightOff

settings.temps()
temp1 = settings.maxTemp
temp2 = settings.minTemp

#main
try:
    web.send('timeOn', lightOn)
    web.send('timeOff', lightOff)
    web.send('lowTemp', temp2)
    web.send('highTemp', temp1)

