#Glorified RPi Timer

the above title reflects the state of this project

the rest of the project will be completed with electronics engineering

***********************************************************************************
Raspberry Pi Zero v1.3

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)



***************************************************************************************


$ sudo apt-get update && sudo apt-get upgrade -y 


$ sudo apt-get install build-essential python-dev python-smbus git sqlite3 -y

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
