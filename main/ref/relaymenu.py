import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while True:
  os.system('clear')
  print "!------------------------!"
  print "!  TOOLS                 !"
  print "!------------------------!"
  print "! [1]                    !"
  print "! [2] 400HPS on          !"
  print "! [3] 400HPS off         !"
  print "! [4] GPIO 22 on         !"
  print "! [5] GPIO 22 off        !"
  print "! [6] GPIO 18 on         !"
  print "! [7] GPIO 18 off        !"
  print "! [8] GPIO 23 on         !"
  print "! [9] GPIO 23 off        !"
  print "! [0] Exit               !"
  print "!------------------------!"
  var = input("[1-0,a-k]: ")
#  if var == 1:
  if var == 2:
    GPIO.output(27, GPIO.LOW)#on
  elif var == 3:
    GPIO.output(27, GPIO.HIGH)#off
  elif var == 4:
    GPIO.output(22, GPIO.LOW)#on
  elif var == 5:
    GPIO.output(22, GPIO.HIGH)#off
  elif var == 6:
    GPIO.output(18, GPIO.LOW)#on
  elif var == 7:
    GPIO.output(18, GPIO.HIGH)#off
  elif var == 8:
    GPIO.output(23, GPIO.LOW)#on
  elif var == 9:
    GPIO.output(23, GPIO.HIGH)#off
  elif var == 0:
    exit()
