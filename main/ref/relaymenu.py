from gpioState import relay18, relay22, relay23 ,relay27
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while True:
  os.system('clear')
  print "!-------------------------------!"
  print "!  Relay Menu            (GPIO) !"
  print "!-------------------------------!"
  print "! [1] States                    !"
  print "! [2] Main Light on        (27) !"  
  print "! [3] Main Light off       (27) !" 
  print "! [4] Ballast Fan on       (22) !"  
  print "! [5] Ballast Fan off      (22) !"
  print "! [6] GPIO 18 on           (18) !"
  print "! [7] GPIO 18 off          (18) !"
  print "! [8] Oscillating Fan on   (23) !"
  print "! [9] Oscillating Fan off  (23) !"
  print "! [0] Exit                      !"
  print "!-------------------------------!"
  var = input("[1-0]: ")
  if var == 1:
    print "relay18, "
    relay18()
    print "relay22, Ballast Fan"
    relay22()
    print "relay23, Oscillating Fan"
    relay23()
    print "relay27, Main Light"
    relay27()
    time.sleep(5)
  elif var == 2:
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
