#! /usr/bin/env python3
# expect this file to get infinitely more complex 
#Copyright (C) 2016  Growmaster420
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import settings
import gpioState
import RPi.GPIO as GPIO
from datetime import datetime
import time
from Adafruit_IO import Client

###Adafruit.IO###
settings.webgui()
guienable = settings.enable1
ADAFRUIT_IO_KEY = settings.key1
web = Client(ADAFRUIT_IO_KEY)
###GPIOstate###
gpioState.relay1()
gpstate1 = gpioState.state1  # heater
gpioState.relay3()
gpstate3 = gpioState.state3  # heater
gpioState.relay4()
gpstate4 = gpioState.state4  # ac
####Settings####
settings.temps()
temp1 = settings.maxTemp
temp2 = settings.minTemp
settings.pins()
pin5 = settings.dhtsensor
pin3 = settings.heater
pin4 = settings.ocfan
settings.heat()
heatvar = settings.heat1
settings.cooling()
coolvar = settings.cool1
###setup###
GPIO.setup(pin3, GPIO.OUT)  # heater
GPIO.setup(pin4, GPIO.OUT)  # ac
lcd = LCD.Adafruit_CharLCDPlate() # defines lcd

###Main Loop###
while True:
    now = datetime.now()
    try:
        h,t = dht.read_retry(dht.DHT22, pin5)  # read DHT22
    except Exception:
        time.sleep(5.0)
        print("DHTread error @ ", now)
    time.sleep(2)
    if guienable == 1:
        try:
            web.send('Temp', t)
            web.send('Humd', h)
        except Exception:
            print("AdafruitIO send error error @ ", now)
            time.sleep(5.0)
    time.sleep(2)
    t1 = t * 9/5.0 + 32
    if t > temp2:
        if t < temp1:
            lcd.set_color(0.0, 1.0, 0.0) # green = good temp
            if heatvar == 1:
                if gpstate3 == 0:
                    GPIO.output(pin3, GPIO.HIGH)  # heater off
            if coolvar == 1:
                if gpstate4 == 0:
                    GPIO.output(pin4, GPIO.HIGH)  # ac off
    if t > temp1:  # explains itself
        lcd.set_color(1.0, 0.0, 0.0)  # high heat
        lcd.clear()
        lcd.message(' TEMP TOO HIGH \n')
        time.sleep(5)
        if heatvar == 1:
            if gpstate3 == 0:
                GPIO.output(pin3, GPIO.HIGH)  # heater off
        if coolvar == 1:
            if gpstate4 == 1:
                GPIO.output(pin4, GPIO.LOW)  # ac on
    if t < temp2:
        lcd.set_color(0.0, 0.0, 1.0)  # Blue = cold shut off a/c
        lcd.message('TEMP TOO LOW\n')
        time.sleep(5)
        if coolvar == 1:
            if gpstate4 == 0:
                GPIO.output(pin4, GPIO.HIGH)  # ac off
        if heatvar == 1:
            if gpstate3 == 1:
                GPIO.output(pin3, GPIO.LOW)  # heater on
    time.sleep(2)
    lcd.clear()  # clear the lcd
    lcd.message('T={0:0.1f} H={1:0.1f}\nF={2:0.1f} %s:%s:%s'.format(t, h, t1) % (now.hour, now.minute, now.second))
    time.sleep(10)
    if gpstate1 == 1:
        lcd.clear
        lcd.set_color(0.0, 0.0, 1.0)
        lcd.message('light is off\n DO NOT OPEN DOOR!!!' )
        time.sleep(5)

