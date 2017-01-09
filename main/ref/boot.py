#!/usr/bin/env python3
# boot set default relay values
import RPi.GPIO as GPIO
import settings
from datetime import datetime, time
settings.pins()
settings.light()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
lightOn = settings.lightOn
lightOff = settings.lightOff
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)  #HPS
GPIO.setup(pin2, GPIO.OUT)  #ballast fan
GPIO.setup(pin3, GPIO.OUT)  #water pump
GPIO.setup(pin4, GPIO.OUT)  #oc fan
now = datetime.now()
now_time = now.time()
if now_time >= time(lightOn, 0) and now_time <= time(lightOff, 0): #light ON
    GPIO.output(pin1, GPIO.LOW)  # main light on
    GPIO.output(pin2, GPIO.LOW)  # ballast fan on
    GPIO.output(pin3, GPIO.HIGH)  # off
    GPIO.output(pin4, GPIO.HIGH)  # off
if now_time <= time(lightOn, 0) and now_time >= time(lightOff, 0):  # light OFF
    GPIO.output(pin1, GPIO.HIGH)  # off
    GPIO.output(pin2, GPIO.HIGH)  # off
    GPIO.output(pin3, GPIO.HIGH)  # off
    GPIO.output(pin4, GPIO.HIGH)  # off
exit()
