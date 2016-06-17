#!/usr/bin/python
#cant run during lights off
#This script is not complete
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT) #side lighting
GPIO.setup(23, GPIO.OUT) #fan
while True:
  time.sleep(1)
  h,t = dht.read_retry(dht.DHT22, 17) #read DHT22 value, set pin
  time.sleep(1)
  t1 = t * 9/5.0 + 32
  time.sleep(1)
  if t1 > 79:
    GPIO.output(22, GPIO.HIGH) #side lighting off
    GPIO.output(23, GPIO.LOW) #fan on
  elif t1 < 68:
    GPIO.output(23, GPIO.HIGH) #fan off
