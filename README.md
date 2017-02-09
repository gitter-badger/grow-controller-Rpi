# grow-controller-Rpi

grow conrtoller 1 is now a dev unit, all other units on main feed

0.0.0.0.0.5-beta

This controller controls:
    
    heater
    A/C
    Light timer
    
To be added:
    
    soil moisture sensor
    co2 sensor
    Others
***************************************************************************************
#Main Menu
![Menu](/main/test/git-assets/menu.png)
#AdafruitIO 
![AdafruitIO](/main/test/git-assets/AdafruitIO.png)

(https://io.adafruit.com/growmaster420/dashboards/grow-controller-rpi)(<DOWN until further notice)
***************************************************************************************

# install
## step1

    passwd #change password

    sudo apt update
  
    sudo apt upgrade -y
  
    sudo apt install build-essential python3 python3-dev python3-smbus python3-pip git cowsay fortune python3-rpi.gpio  -y
  
    sudo pip3 install adafruit-io
  
    cd ~
  
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  
    git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
  
    git clone https://github.com/growmaster420/grow-controller-Rpi.git
    
    sudo python3 Adafruit_Python_DHT/setup.py install 
      
    sudo python3 Adafruit_Python_CharLCD/setup.py install 
      
    sudo dpkg-reconfigure tzdata
    
    sudo raspi-config #i2c enable
## step2 
 
 
put Adafruit.IO key in settings.py if enabled 
  
set variables in settings.py in (menu 'l')

create a file in "boot" partition named "ssh"

install wpa_supplicant.conf in sdcard as root

4 more project info read comments in settings.py

run cronmaker from menu (menu 'b')

install crontab from menu (menu 'g')

**************************************************

Raspberry Pi Zero v1.3

Python v3

using BCM for GPIO values

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)

Using Adafruit-IO python client (https://github.com/adafruit/io-client-python)

**************************************************

Dev branches are normally stable if u git clone after the days commits stop, around 12GMT = 4PST

this project will reach v1.0 when all elements are I require added 