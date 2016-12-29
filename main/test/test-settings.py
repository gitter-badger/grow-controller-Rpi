###testing###
import settings

###call the functions###
settings.pins()
settings.temps()
settings.light()
settings.expGpio()
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
#################
print("pinvar1", pinvar1)
print("pinvar2", pinvar2)
print("pinvar3", pinvar3)
print("pinvar4", pinvar4)
