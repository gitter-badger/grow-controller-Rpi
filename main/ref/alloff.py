import settings
import RPi.GPIO as GPIO
settings.pins()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.HIGH)
exit()
