# grow-controller-RPi3 -RPi2 -PiZero
***************************************************************************
"THE WEED-WARE LICENSE" :
 <scott snyder> scott@yep.duckdns.org wrote these files.  As long as you
 retain this notice you can do whatever you want with this stuff. 
 If we meet some day, and you think this stuff is worth it,
 you can smoke me a bowl in return.
***************************************************************************

UNPLUG MAINS A/C WHILE REBOOT IS A GOOD IDEA RANDOM RELAYS COME ON i think this is due to the GPIO libary automatically setting the pins to low when there first GPIO "setup" called,  boot.py  sets defaults, a Battery backup for the PI is kind of required, a 1 sec power outage caused all the realys to turn on during lights out while flowering, NOT GOOD.. 

# Releases are stable versions of this grow controller


Using the "light cycle" in the "main menu" replaces your current crontab, it also places @reboot lcd scripts.
if your not using the Adafruit PiPlate lcd # out the lcd calls in crontab.flower and crontab.veg. If U have other
jobs in your crontab U'll want to also add them to crontab.flower and crontab.veg.
 
I am teaching myself a bit of python with this project



using OS: Raspbian jessie lite

SD card size: 2GB sd card expansion not needed, latest "raspbian lite" automagicly expanded the SD at first boot

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) requires root :<(

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)

Using the Raspbian GPIO library for relay control(comes with raspbian lite, no DL required) 


building a Raspberry pi grow controller using python and crontab and some shell script

just a menu for now, learning how to automate all and will

be updating this repo with what i come up with.

goals are to have the relays react to temp values, auto watering



will be building a complete "plant and forget" grow controller.............

.............eventually
 
add soil EC sensor(moisture)

add water pump

add liquid flow sensor

add water PH/TDS/EC sensor

add Android Apk to control everything

***************************************************************************************
#Installation and use

$ sudo apt-get update && sudo apt-get upgrade -y 

/\ while u wait U can evolve into a superbeing, it takes that F'n long(even on a Pi3, if your on a Pi1 this repo will be outdated before this command is done)
 
$ sudo apt-get install build-essential python-dev python-smbus git -y

#DHT22

$ cd ~

$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git

$ cd Adafruit_Python_DHT

$ sudo python setup.py install

#Adafruit LCD

$ cd ~

$ git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git

$ cd Adafruit_Python_CharLCD

$ sudo python setup.py install

$ sudo raspi-config 

Advanced Options>A6 I2C>enable

#Grow controller

$ cd ~

$ git clone https://github.com/growmaster420/grow-controller-Rpi.git

#To Use

$ cd grow-controller-Rpi

$ cd main

$ bash menu.sh

Install the crontab in light menu

$ sudo reboot now
