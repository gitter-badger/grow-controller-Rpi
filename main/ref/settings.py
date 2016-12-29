###settings.py###

###set min max temps here###
def temps():
    global maxTemp, minTemp
    maxTemp = 30
    minTemp = 20
###set pins here###
def pins():
    global ballast, ballastfan, heater, ocfan, dhtsensor
    ballast = 27
    ballastfan = 22
    heater = 18
    ocfan = 23
    dhtsensor = 17
def expGpio():
    global gp1, gp2, gp3, gp4
    gp1 = "/sys/class/gpio/gpio27/value"
    gp2 = "/sys/class/gpio/gpio22/value"
    gp3 = "/sys/class/gpio/gpio18/value"
    gp4 = "/sys/class/gpio/gpio23/value"

###set light times here###
def light():
    global lightOn, lightOff
    lightOn = 8
    lightOff = 20

