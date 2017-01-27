#! /usr/bin/env python3
# expect this file to get infinitely more complex 
from multiprocessing import Process
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import settings
import gpioState
import RPi.GPIO as GPIO
from datetime import datetime
import time
from Adafruit_IO import Client


###\/these need to be ordered correctally\/####
settings.webgui()
gpioState.relay3()
gpioState.relay4()
settings.temps()
settings.pins()
settings.heat()
settings.cooling()
lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
temp1 = settings.maxTemp
temp2 = settings.minTemp
pin5 = settings.dhtsensor
pin1 = settings.ballast
pin3 = settings.heater
pin4 = settings.ocfan
coolvar = settings.cool1
heatvar = settings.heat1
gpstate3 = gpioState.state3  # heater
gpstate4 = gpioState.state4  # ac
GPIO.setup(pin1, GPIO.OUT)  #  ballast
GPIO.setup(pin3, GPIO.OUT)  # heater
GPIO.setup(pin4, GPIO.OUT)  # ac
guienable = settings.enable1
ADAFRUIT_IO_KEY = settings.key1
web = Client(ADAFRUIT_IO_KEY)


def lcdDis():   #  display function
    while True:
        now = datetime.now()
        h,t = dht.read_retry(dht.DHT22, pin5)  # read DHT22
        time.sleep(1)
        if guienable == 1:
            web.send('Temp', t)
            web.send('Humd', h)
        time.sleep(1)
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
        time.sleep(1)
        lcd.clear()  # clear the lcd
        lcd.message('T={0:0.1f} H={1:0.1f}\nF={2:0.1f} %s:%s:%s'.format(t, h, t1) % (now.hour, now.minute, now.second))
        time.sleep(5)

def lcdBut():
    while True:
        time.sleep(0.5)  # without this time.sleep, 23% cpu usage. with 3%
        if lcd.is_pressed(LCD.UP):
            GPIO.output(pin1, GPIO.LOW)  # on
        if lcd.is_pressed(LCD.DOWN):
            GPIO.output(pin1, GPIO.HIGH)  # off

if __name__ == '__main__':  # run the above functions in the background
    Process(target=lcdDis).start()
    Process(target=lcdBut).start()
