#!/usr/bin/python
#does not turn on any lights 
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

def temp():
  h,t = dht.read_retry(dht.DHT22, 17) #read DHT22 value, set pi
  t1 = t * 9/5.0 + 32
  print(t1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT) #side lighting
GPIO.setup(23, GPIO.OUT) #fan
#GPIO.setup(?, GPIO.OUT) #heater
while True:
  time.sleep(5)
  temp()



  
  
#  if t1 > 79:
#    GPIO.output(22, GPIO.HIGH) #side lighting off
#    GPIO.output(23, GPIO.LOW) #fan on
#  elif t1 < 68:
#    if t1 > 66:
#      GPIO.output(?, GPIO.LOW) #heater on
#      time.sleep(30)
#      GPIO.output(?, GPIO.HIGH ) #heater off
