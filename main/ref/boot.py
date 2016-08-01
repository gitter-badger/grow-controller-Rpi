# boot set default relay values
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)#
GPIO.setup(23, GPIO.OUT)#
GPIO.setup(22, GPIO.OUT)#
GPIO.setup(27, GPIO.OUT)#HPS

GPIO.output(18, GPIO.HIGH)#off
GPIO.output(23, GPIO.HIGH)#off
GPIO.output(22, GPIO.HIGH)#off
GPIO.output(27, GPIO.HIGH)#off
exit()
