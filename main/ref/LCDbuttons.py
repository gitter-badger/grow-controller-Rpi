# works
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
lcd = LCD.Adafruit_CharLCDPlate()

while True:
    time.sleep(0.1) # without this time.sleep, 23% cpu usage. with 3%
#    if lcd.is_pressed(LCD.SELECT):
    if lcd.is_pressed(LCD.UP):
        GPIO.output(18, GPIO.LOW)
    if lcd.is_pressed(LCD.DOWN):
        GPIO.output(18, GPIO.HIGH)
#    if lcd.is_pressed(LCD.LEFT):
#    if lcd.is_pressed(LCD.RIGHT):


