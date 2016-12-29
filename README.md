***********************************************************************************

#lastest raspbian ssh server is off by default
create a file in "boot" partition named "ssh"

************************************************************************************

Raspberry Pi Zero v1.3

using OS: Raspbian jessie lite

Using Adafruit DHT22 raspberry pi library(https://github.com/adafruit/Adafruit_Python_DHT) 

Using Adafruit 16x2 I2C PiPlate LCD display (https://github.com/adafruit/Adafruit_Python_CharLCD)

***************************************************************************************
![Menu](/main/test/git-assets/menu.PNG)
***************************************************************************************
## install
  sudo apt update
  
  sudo apt upgrade -y
  
  sudo apt install build-essential python3 python3-dev python-smbus python3-pip git cowsay fortune rpi-update -y
  
  sudo rpi-update
  
  cd ~
  
  git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  
  git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
  
  cd Adafruit_Python_DHT
  
  sudo python setup.py install 
  
  cd ~
  
  cd Adafruit_Python_CharLCD
  
  sudo python setup.py install 
  
  cd ~
  
  git clone https://github.com/growmaster420/grow-controller-Rpi.git /home/pi
  
  sudo dpkg-reconfigure tzdata
  
  cat /home/pi/grow-controller-Rpi/.bashrc > /home/pi/.bashrc
  
  sudo raspi-config #i2c enable
  
set variables in settings.py in menu [l]

*************************************
