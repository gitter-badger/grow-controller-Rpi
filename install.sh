# LAZY
sudo apt-get update &&
sudo apt-get upgrade -y &&
sudo apt-get dist-upgrade -y &&
sudo apt-get autoremove -y &&
sudo apt-get install build-essential python-dev python-smbus python-pip git -y &&
git clone https://github.com/adafruit/Adafruit_Python_DHT.git  &&
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git &&
git clone https://github.com/growmaster420/grow-controller-Rpi.git &&
crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower &&
dpkg-reconfigure tzdata
