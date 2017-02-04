#!/usr/bin/env python3
###settings.py###

###set min max temps here, in C###
def temps():
    global maxTemp, minTemp
    maxTemp = 30   # temp at which the A/C turns on
    minTemp = 20   # temp at which the heater turns on
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
###SET PINs ABOVE###
    
###set light times here### 24hr time scale
def light():
    global lightOn, lightOff
    lightOn = 8
    lightOff = 20
## BELOW ARE OPTIONAL, 0 all to turn off
#  heat/ handled in lcd.py#0 = no heat, 1 = heat
def heat():
    global heat1
    heat1 = 0  # is a heater installed, 0 = no / 1 = yes
def cooling():
    global cool1
    cool1 = 0  # is a AC unit installed, 0 = no / 1 = yes
def webgui():  #  requires a Adafruit.IO account(free)
    global enable1, key1
    enable1 = 1   # webGui enable #  ## 0 = no / 1 = yes
    key1 = 'your_adafruit_IO_key'


''' # what to turn on at boot, NOT FINISHED
def boot():
    global 1, 2, 3, 4
    1 = 0
    2 = 0
    3 = 0
    4 = 0


'''