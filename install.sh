git clone https://github.com/adafruit/Adafruit_Python_DHT.git /home/pi &&
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git /home/pi &&
git clone https://github.com/growmaster420/grow-controller-Rpi.git /home/pi &&
python /home/pi/Adafruit_Python_DHT/setup.py install &&
python /home/pi/Adafruit_Python_CharLCD/setup.py install &&
crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower
