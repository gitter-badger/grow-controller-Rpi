###set min max temps here###
def temps():
    global maxTemp, minTemp
    maxTemp = 30
    minTemp = 20

###set pins here###
##not yet intergrated project wide##
def pins():
    global ballast, ballastfan, heater, ocfan, dhtsensor
    ballast = 27
    ballastfan = 22
    heater = 18
    ocfan = 23
    dhtsensor = 17
