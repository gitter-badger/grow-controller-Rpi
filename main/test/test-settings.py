###testing###
import settings

###call the functions###
settings.pins()
settings.temps()
settings.light()
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
print("light on", lightOn)
print("light off", lightOff)
