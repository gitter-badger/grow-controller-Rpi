#!/usr/bin/env python3
#import os
import settings
settings.pins()
settings.light()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
lightOn = settings.lightOn
lightOff = settings.lightOff
print("###INSTALL AS ROOT###")
print("@reboot python3 /home/pi/grow-controller-Rpi/main/ref/main.py &")
print("@reboot python3 /home/pi/grow-controller-Rpi/main/ref/alloff.py")
print("@reboot sudo echo", pin1, "> /sys/class/gpio/export")
print("@reboot sudo echo", pin2, "> /sys/class/gpio/export")
print("@reboot sudo echo", pin3, "> /sys/class/gpio/export")
print("@reboot sudo echo", pin4, "> /sys/class/gpio/export")
print("0", lightOn, "* * * python3 /home/pi/grow-controller-Rpi/main/ref/relay.py -m on")
print("0", lightOff, "* * * python3 /home/pi/grow-controller-Rpi/main/ref/relay.py -m off")
print("0", lightOn, "* * * python3 /home/pi/grow-controller-Rpi/main/ref/relay.py -b on")
print("0", lightOff, "* * * python3 /home/pi/grow-controller-Rpi/main/ref/relay.py -b off")
print("0 0 * * * reboot now")
