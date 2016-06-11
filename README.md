# grow-controller-RPi3
***************************************************************************
"THE WEED-WARE LICENSE" :
 <scott snyder> scott@yep.duckdns.org wrote these files.  As long as you
 retain this notice you can do whatever you want with this stuff. 
 If we meet some day, and you think this stuff is worth it,
 you can smoke me a bowl in return.
***************************************************************************

Using the "change light cycle" in the "light menu" replaces your current crontab, it also places @reboot lcd.py.
if your not using the Adafruit PiPlate lcd # out the lcd.py call in crontab.flower and crontab.veg. If U have other
jobs in your crontab U'll want to also add them to crontab.flower and crontab.veg.
 
I am teaching myself a bit of python with this project

#*********assume none of this code works**********

using OS: Raspbian jessie lite

SD card size: 2GB

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

#Grow controller

$ cd ~

$ git clone https://github.com/growmaster420/grow-controller-Rpi.git

#To Use

$ cd grow-controller-Rpi

$ cd main

$ bash menu.sh

Install the crontab in light menu

$ sudo reboot now
