#!/usr/bin/env python3
from gpioState import relay1, relay2, relay3 ,relay4
import RPi.GPIO as GPIO
import os
import time
import settings
import gpioState

gpioState.relay1()
gpioState.relay2()
gpioState.relay3()
gpioState.relay4()
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
gpstate1 = gpioState.state1  # ballast
gpstate2 = gpioState.state2  # ballast fan
gpstate3 = gpioState.state3  # heater
gpstate4 = gpioState.state4  # ocfan
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])


while True:
    os.system('clear')
    print("!-------------------------------!")
    print("!  Relay Menu            (GPIO) !")
    print("!-------------------------------!")
    print("! [1] States                    !")
    print("! [2] Main Light on        (27) !")
    print("! [3] Main Light off       (27) !")
    print("! [4] Ballast Fan on       (22) !")
    print("! [5] Ballast Fan off      (22) !")
    print("! [6] Heater on            (18) !")
    print("! [7] Heater off           (18) !")
    print("! [8] Oscillating Fan on   (23) !")
    print("! [9] Oscillating Fan off  (23) !")
    print("! [0] Exit                      !")
    print("!-------------------------------!")
    var = input("[1-0]: ")
    if var == "1":
        if gpstate1 == 0:
            print("ballast on")
        if gpstate1 == 1:
            print("ballast off")
        if gpstate2 == 0:
            print("ballast fan on")
        if gpstate2 == 1:
            print("ballast fan off")
        if gpstate3 == 0:
            print("heater on")
        if gpstate3 == 1:
            print("heater off")
        if gpstate4 == 0:
            print("oc fan on")
        if gpstate4 == 1:
            print("ocfan off")
        fakevar = input("enter to continue")
    if var == "2":
        print("TURN ON MAIN LIGHT!!!![y/n]:")
        choice = input().lower()
        if choice in yes:
            GPIO.output(pin1, GPIO.LOW)#on
        if choice in no:
            print("Think Before U Fuck Everything Up")
    if var == "3":
        print("TURN OFF MAIN LIGHT!!!![y/n]:")
        choice = input().lower()
        if choice in yes:
            GPIO.output(pin1, GPIO.HIGH)#off
        if choice in no:
            print("Think Before U Fuck Everything Up")
    if var == "4":
        GPIO.output(pin2, GPIO.LOW)#on
    if var == "5":
        GPIO.output(pin2, GPIO.HIGH)#off
    if var == "6":
        GPIO.output(pin3, GPIO.LOW)#on
    if var == "7":
        GPIO.output(pin3, GPIO.HIGH)#off
    if var == "8":
        GPIO.output(pin4, GPIO.LOW)#on
    if var == "9":
        GPIO.output(pin4, GPIO.HIGH)#off
    if var == "0":
        exit()
