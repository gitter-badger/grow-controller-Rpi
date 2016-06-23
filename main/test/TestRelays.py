import sys, getopt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)#FL
GPIO.setup(27, GPIO.OUT)#HPS

if opt == '-h':
  GPIO.output(18, GPIO.HIGH)#on
  exit
  
