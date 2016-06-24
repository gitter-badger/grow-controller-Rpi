# boot set default relay values

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)#wiring light
GPIO.setup(23, GPIO.OUT)#fans
GPIO.setup(22, GPIO.OUT)#FL
GPIO.setup(27, GPIO.OUT)#HPS
GPIO.output(18, GPIO.LOW)#on
GPIO.output(23, GPIO.LOW)#on
GPIO.output(22, GPIO.LOW)#on
GPIO.output(27, GPIO.HIGH)#off
exit()
