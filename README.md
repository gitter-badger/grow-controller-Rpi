0.0.0.0.0.1beta
***************************************************************************************
#Main Menu
![Menu](/main/test/git-assets/BashMenu.jpg)
#AdafruitIO 
![AdafruitIO](/main/test/git-assets/AdafruitIO.png)

(https://io.adafruit.com/growmaster420/dashboards/grow-controller-rpi)
***************************************************************************************
## install
    sudo apt update
  
    sudo apt upgrade -y
  
    sudo apt install build-essential python3 python3-dev python3-smbus python3-pip git cowsay fortune python3-rpi.gpio  -y
  
    sudo pip3 install adafruit-io
  
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

create a file in "boot" partition named "ssh"

4 more project info read comments in settings.py


Raspberry Pi Zero v1.3

Python v3

using BCM for GPIO values

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)

Using Adafruit-IO python client (https://github.com/adafruit/io-client-python)

