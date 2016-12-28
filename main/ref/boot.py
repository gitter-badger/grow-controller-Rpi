# boot set default relay values
import RPi.GPIO as GPIO
import settings

settings.pins()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin1, GPIO.OUT)#HPS
GPIO.setup(pin2, GPIO.OUT)#ballast fan
GPIO.setup(pin3, GPIO.OUT)#water pump
GPIO.setup(pin4, GPIO.OUT)#oc fan

GPIO.output(pin1, GPIO.HIGH)#off
GPIO.output(pin2, GPIO.HIGH)#off
GPIO.output(pin3, GPIO.HIGH)#off
GPIO.output(pin4, GPIO.LOW)#on

exit()
