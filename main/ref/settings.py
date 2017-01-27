#!/usr/bin/env python3
###settings.py###

###set min max temps here, in C###
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

#  heat/ handled in lcd.py#0 = no heat, 1 = heat
def heat():
    global heat1
    heat1 = 0
def cooling():
    global cool1
    cool1 = 0
def webgui():
    global EDV, ADAFRUIT_IO_KEY
    EDV = 1   # logging enable ##1 = yes, 0 = no
    ADAFRUIT_IO_KEY = 'your_adafruit_IO_key'
