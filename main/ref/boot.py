#!/usr/bin/env python3
# boot set default relay values
import RPi.GPIO as GPIO
import settings
from datetime import datetime
from time import sleep
settings.pins()
settings.light()
settings.boot()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
lightOn = settings.lightOn
lightOff = settings.lightOff

now = datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)  #  HPS
GPIO.setup(pin2, GPIO.OUT)  #  ballast fan
GPIO.setup(pin3, GPIO.OUT)  #  water pump
GPIO.setup(pin4, GPIO.OUT)  #  oc fan
var1 = now.hour
if (var1 < lightOff) and (var1 >= lightOn):
    sleep(15)  # if power outage was short give the bulb a little time to cool
    GPIO.output(pin1, GPIO.LOW)  # main light on
    GPIO.output(pin2, GPIO.LOW)  # ballast fan on
    GPIO.output(pin3, GPIO.HIGH)  # off
    GPIO.output(pin4, GPIO.HIGH)  # off
exit()
