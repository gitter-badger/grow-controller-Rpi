# works
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
lcd = LCD.Adafruit_CharLCDPlate()

while True:
    if lcd.is_pressed(LCD.SELECT):
        GPIO.output(18, GPIO.LOW)

