from gpioState import relay1, relay2, relay3 ,relay4
import RPi.GPIO as GPIO
import os
import time
import settings

settings.pins()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])


while True:
  os.system('clear')
  print "!-------------------------------!"
  print "!  Relay Menu            (GPIO) !"
  print "!-------------------------------!"
  print "! [1] States*******BROKEN*******!"
  print "! [2] Main Light on        (27) !"  
  print "! [3] Main Light off       (27) !" 
  print "! [4] Ballast Fan on       (22) !"  
  print "! [5] Ballast Fan off      (22) !"
  print "! [6] Heater on            (18) !"
  print "! [7] Heater off           (18) !"
  print "! [8] Oscillating Fan on   (23) !"
  print "! [9] Oscillating Fan off  (23) !"
  print "! [0] Exit                      !"
  print "!-------------------------------!"
  var = input("[1-0]: ")
  if var == 1:
    print "relay1, "
    relay1()
    print "relay2, Ballast Fan"
    relay2()
    print "relay3, Oscillating Fan"
    relay3()
    print "relay4, Main Light"
    relay4()
    time.sleep(5)
  elif var == 2:
    print "TURN ON MAIN LIGHT!!!![y/n]:"
    choice = raw_input().lower()
    if choice in yes:
      GPIO.output(pin1, GPIO.LOW)#on
    elif choice in no:
      print "Think Before U Fuck Everything Up"
  elif var == 3:
    print "TURN OFF MAIN LIGHT!!!![y/n]:"
    choice = raw_input().lower()
    if choice in yes:
      GPIO.output(pin1, GPIO.HIGH)#off
    elif choice in no:
      print "Think Before U Fuck Everything Up"
  elif var == 4:
    GPIO.output(pin2, GPIO.LOW)#on
  elif var == 5:
    GPIO.output(pin2, GPIO.HIGH)#off
  elif var == 6:
    GPIO.output(pin3, GPIO.LOW)#on
  elif var == 7:
    GPIO.output(pin3, GPIO.HIGH)#off
  elif var == 8:
    GPIO.output(pin4, GPIO.LOW)#on
  elif var == 9:
    GPIO.output(pin4, GPIO.HIGH)#off
  elif var == 0:
    exit()
