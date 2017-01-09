#!/usr/bin/env python3
#  Adafruit 16x2 I2C PiPlate / simple, buttons and display script
#  simple lcd control
# 
# file relies on settings.py
from multiprocessing import Process
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import settings
import RPi.GPIO as GPIO
from datetime import datetime
import time
settings.temps()
settings.pins()
lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
temp1 = settings.maxTemp
temp2 = settings.minTemp
pin5 = settings.dhtsensor
pin1 = settings.ballast
GPIO.setup(pin1, GPIO.OUT)#HPS
def lcdDis(): #display function
  while True:
    now = datetime.now()
    h,t = dht.read_retry(dht.DHT22, pin5) #read DHT22
    time.sleep(1)
    t1 = t * 9/5.0 + 32
    if t > temp2:
      if t < temp1:
        lcd.set_color(0.0, 1.0, 0.0) # green = good temp
    if t > temp1: # explains itself
      lcd.set_color(1.0, 0.0, 0.0) # red = too hot turn off extra lighting, fan at max
      lcd.clear()
      lcd.message(' TEMP TOO HIGH \n')
      time.sleep(5)
    if t < temp2:
      lcd.set_color(0.0, 0.0, 1.0) # Blue = cold shut off a/c
      lcd.message('TEMP TOO LOW\n')
      time.sleep(5)
    time.sleep(1)
    lcd.clear() # clear the lcd
    lcd.message('T={0:0.1f} H={1:0.1f}\nF={2:0.1f} %s:%s:%s'.format(t, h, t1) % (now.hour, now.minute, now.second)) # print the DHT22 values in the lcd
    time.sleep(5)



def lcdBut():
  while True:
    time.sleep(0.5) # without this time.sleep, 23% cpu usage. with 3%
    if lcd.is_pressed(LCD.UP):
      GPIO.output(pin1, GPIO.LOW)#on
    if lcd.is_pressed(LCD.DOWN):
      GPIO.output(pin1, GPIO.HIGH)#off

if __name__ == '__main__': #run the above functions in the background, FOREVER!!!!!!!!!!!!!!!!!!!!!
  Process(target=lcdDis).start()
  Process(target=lcdBut).start()
