###This button script is for gpio pin>button>ground connection
### requires no resistors..
###
###
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(?, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(?, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2)

while True:
    button_1 = GPIO.input(?)
#    button_2 = GPIO.input(?)

#    if button_2 == False:
#        print('')
    
    if button_1 == False:
        os.system("sudo apt-get update && sudo apt-get upgrade -y")
        time.sleep(2)
        os.system("sudo shutdown -h -P now")
    time.sleep(0.2)
