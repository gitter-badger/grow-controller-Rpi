Writen with K.I.S.S. in mind (https://en.wikipedia.org/wiki/KISS_principle)
***********************************************************************************

#lastest raspbian ssh server is off by default
create a file in "boot" partition named "ssh"

************************************************************************************

Raspberry Pi Zero v1.3

Python v3

using BCM for GPIO values

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)

Using Adafruit-IO python client (https://github.com/adafruit/io-client-python)

***************************************************************************************
## install
    sudo apt update
  
    sudo apt upgrade -y
  
    sudo apt install build-essential python3 python3-dev python3-smbus python3-pip git cowsay fortune rpi-update python3-rpi.gpio  -y
  
    sudo pip3 install adafruit-io
  
    sudo rpi-update
  
    cd ~
  
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  
    git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
  
    git clone https://github.com/growmaster420/grow-controller-Rpi.git
  
    cd Adafruit_Python_DHT
  
    sudo python3 setup.py install 
  
    cd ~
  
    cd Adafruit_Python_CharLCD
  
    sudo python3 setup.py install 
  
    cd ~
    
    sudo dpkg-reconfigure tzdata
    
    sudo raspi-config #i2c enable
  
put Adafruit.IO key in settings.py if enabled 
  
set variables in settings.py in menu [l]

*************************************

I plan to continue development on this project until my death.

***************************************************************************************
#Main Menu
![Menu](/main/test/git-assets/menu.PNG)
#AdafruitIO (https://io.adafruit.com/growmaster420/dashboards/grow-controller-rpi)
![AdafruitIO](/main/test/git-assets/AdafruitIO.png)
***************************************************************************************

4 more project info read comments in settings.py
