
  sudo apt update
  sudo apt upgrade -y
  sudo apt install 
  sudo apt install build-essential python-dev python-smbus python-pip git cowsay fortune rpi-update -y
  sudo rpi-update
  cd ~
  git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
  cd Adafruit_Python_DHT
  sudo python /home/pi/Adafruit_Python_DHT/setup.py install 
  cd ~
  cd Adafruit_Python_CharLCD
  sudo python /home/pi/Adafruit_Python_CharLCD/setup.py install 
  cd ~
  git clone https://github.com/growmaster420/grow-controller-Rpi.git /home/pi
  sudo dpkg-reconfigure tzdata
  cat /home/pi/grow-controller-Rpi/.bashrc > /home/pi/.bashrc
  crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower
  sudo raspi-config #i2c enable


***********************************************************************************

#lastest raspbian ssh server is off by default
create a file in "boot" partition named "ssh"

************************************************************************************

Raspberry Pi Zero v1.3

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)



***************************************************************************************


$ sudo apt-get update && sudo apt-get upgrade -y 


$ sudo apt install build-essential python-dev python-smbus python-pip git cowsay fortune rpi-update -y

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
