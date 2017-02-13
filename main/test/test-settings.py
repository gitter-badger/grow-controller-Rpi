###testing###
import settings

###call the functions###
settings.pins()
settings.temps()
settings.light()
settings.expGpio()
settings.heat()
settings.cooling()
settings.webgui()
settings.boot()
#######################

###Set Variables######
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
pin5 = settings.dhtsensor
lightOn = settings.lightOn
lightOff = settings.lightOff
temp1 = settings.maxTemp
temp2 = settings.minTemp
pinvar1 = settings.gp1
pinvar2 = settings.gp2
pinvar3 = settings.gp3
pinvar4 = settings.gp4
heatvar = settings.heat1
coolvar = settings.cool1
ADAFRUIT_IO_KEY = settings.key1
guienable = settings.enable1
b1 = settings.boot1
b2 = settings.boot2
b3 = settings.boot3
b4 = settings.boot4
#######################

###Relay Pins###
print("--pin settings--")
print("ballast pin", pin1)
print("ballastfan pin", pin2)
print("heater pin", pin3)
print("ocfan pin", pin4)
################
print("\n--temp settings--")
###temp values###
print("Max temp", temp1)
print("Min Temp", temp2)
#################
print("\n--light no/off times--")
print("light on", lightOn)
print("light off", lightOff)
#################
print("\n--pinvars--")
print("pinvar1", pinvar1)
print("pinvar2", pinvar2)
print("pinvar3", pinvar3)
print("pinvar4", pinvar4)
#################
print("\n--is HVAC controlled (1=yes)--")
print("heatvar", heatvar)
print("coolvar", coolvar)
#################
print('key1', ADAFRUIT_IO_KEY)
print('gui enable', guienable)
#################
print('boot1', b1)
print('boot2', b2)
print('boot3', b3)
print('boot4', b4)