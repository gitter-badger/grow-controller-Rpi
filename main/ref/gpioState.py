#!/usr/bin/env python3
#state 0 = on
#state 1 = off
import settings
settings.expGpio()
pinvar1 = settings.gp1  # ballast
pinvar2 = settings.gp2  # ballast fan
pinvar3 = settings.gp3  # heater
pinvar4 = settings.gp4  # ac
def relay1():
    global state1
    with open(pinvar1) as gpio1:
        state1 = int(gpio1.read())
def relay2():
    global state2
    with open(pinvar2) as gpio2:
        state2 = int(gpio2.read())
def relay3():
    global state3
    with open(pinvar3) as gpio3:
        state3 = int(gpio3.read())
def relay4():
    global state4
    with open(pinvar4) as gpio4:
        state4 = int(gpio4.read())
if __name__ == "__main__":
    relay1()
    print("Ballast", state1)
    if state1 == 1:
        print('off')
    if state1 == 0:
        print('on')
    relay2()
    print("Ballast Fan", state2)
    if state2 == 1:
        print('off')
    if state2 == 0:
        print('on')
    relay3()
    print("Heater", state3)
    if state3 == 1:
        print('off')
    if state3 == 0:
        print('on')
    relay4()
    print("ac fan", state4)
    if state4 == 1:
        print('off')
    if state4 == 0:
        print('on')
