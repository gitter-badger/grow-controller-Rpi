###This button script is for gpio pin>button>ground connection
### requires no resistors..
### USED 4 TESTING HARDWARE
###crontab ## @reboot /home/pi/grow-controller-Rpi/main/ref/shutdownbutton.py &
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


time.sleep(0.2)

while True:
  button_1 = GPIO.input(26)
  if button_1 == False:
    os.system("sudo shutdown -h -P now")
  time.sleep(0.2)
