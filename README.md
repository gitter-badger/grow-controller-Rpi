# grow-controller-RPi3
***************************************************************************
"THE WEED-WARE LICENSE" :
 <scott snyder> scott@yep.duckdns.org wrote these files.  As long as you
 retain this notice you can do whatever you want with this stuff. 
 If we meet some day, and you think this stuff is worth it,
 you can smoke me a bowl in return.
***************************************************************************
 
I am teaching myself a bit of python with this project

*********assume none of this code works**********

pins must be set across many files

using OS: Raspbian jessie lite

SD card size: 2GB

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) requires root :<(

Using the Raspbian GPIO library for relay control(built in, no DL required) 


building a Raspberry pi grow controller using python and crontab and some shell script

just a menu for now, learning how to automate all and will

be updating this repo with what i come up with.

goals are to have the relays react to temp values, auto watering



will be building a complete "plant and forget" grow controller.............

.............eventually
 
add soil EC sensor(moisture)

add water pump

add liquid flow sensor

watchdht.py ---> lcd 16x2 I2C lcd =  Adafruit PRODUCT ID: 1110 
