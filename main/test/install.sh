#!/usr/bin/env bash

sudo apt update
sudo apt install build-essential python3 python3-dev python3-smbus python3-pip git cowsay fortune python3-rpi.gpio  -y
sudo pip3 install adafruit-io
cd ~
git clone https://github.com/growmaster420/Adafruit_Python_DHT.git
git clone https://github.com/growmaster420/Adafruit_Python_CharLCD.git
git clone https://github.com/growmaster420/grow-controller-Rpi.git
sudo python3 Adafruit_Python_DHT/setup.py install
sudo python3 Adafruit_Python_CharLCD/setup.py install
cat /home/pi/grow-controller-Rpi/.bashrc >> /home/pi/.bashrc
echo""
echo""
echo""
echo""

