#!/usr/bin/python
#cant run during lights off
#This script is not complete
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(?, GPIO.OUT) #set relay pins here
#h,t = dht.read_retry(dht.DHT22, ?)
#t = t * 9/5.0 + 32 #convert DHT22 data to F #unreliable find alt. or learn C
#print t #for testing remove later
# need to read gpio state
# \/\/\/\/\/\/\/\/\/\/\/
#temp = (t1 + t2 + t3) / (3) #average multi dht setup
##################
while 1:
  h,t = dht.read_retry(dht.DHT22, ?) #read DHT22 value, set pin
  time.sleep(1)
  if t > 28:
    GPIO.output(?, GPIO.HIGH) #side lighting off
    GPIO.output(?, GPIO.LOW) #emergency vent fan on
    time.sleep(30) #runs emergency vent fan for ()seconds
    GPIO.output(?, GPIO.HIGH) #emergency vent fan off
  if t < 20:
    GPIO.output(?, GPIO.LOW) #side light on
