import settings


settings.pins()
settings.temps()

pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
temp1 = settings.maxTemp
temp2 = settings.minTemp



print("ballast pin", pin1)
print("ballastfan", pin2)
print("heater", pin3)
print("ocfan", pin4)

print("Max temp", temp1)
print("Min Temp", temp2)
