
import settings
from Adafruit_IO import Client
import gpioState


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

###GPIOstate###
gpioState.relay1()
gpioState.relay2()
gpioState.relay3()
gpioState.relay4()
gpstate1 = gpioState.state1  # ballast
gpstate2 = gpioState.state2  # ballast fan
gpstate3 = gpioState.state3  # heater
gpstate4 = gpioState.state4  # ocfan


#main
web.send('timeOn', lightOn)
web.send('timeOff', lightOff)
web.send('lowTemp', temp2)
web.send('highTemp', temp1)

if gpstate1 == 0:
    web.send('ballastState', 'ON')
if gpstate1 == 1:
    web.send('ballastState', 'OFF')

if gpstate2 == 0:
    web.send('ballastFan', 'ON')
if gpstate2 == 1:
    web.send('ballastFan', 'OFF')

if gpstate3 == 0:
    web.send('heaterState', 'ON')
if gpstate3 == 1:
    web.send('heaterState', 'OFF')

if gpstate4 == 0:
    web.send('acfanState', 'ON')
if gpstate4 == 1:
    web.send('acfanState', 'OFF')
