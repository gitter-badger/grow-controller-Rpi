#do not run as sh file
#installer
echo"this script fails"
exit
sudo apt update
sudo apt upgrade -y
sudo apt install 
sudo apt install build-essential python-dev python-smbus python-pip git cowsay fortune rpi-update -y
sudo rpi-update
git clone https://github.com/adafruit/Adafruit_Python_DHT.git /home/pi
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git /home/pi
sudo python /home/pi/Adafruit_Python_DHT/setup.py install 
sudo python /home/pi/Adafruit_Python_CharLCD/setup.py install 
git clone https://github.com/growmaster420/grow-controller-Rpi.git /home/pi
sudo dpkg-reconfigure tzdata
cat /home/pi/grow-controller-Rpi/.bashrc > /home/pi/.bashrc
crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower
sudo raspi-config #i2c enable

