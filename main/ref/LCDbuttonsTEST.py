#I Dont understand why this doesnt work!!!!!!!!!!!! SMASHES KEYBOARD
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()


# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, GPIO.output(18, GPIO.LOW)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

print('Press Ctrl-C to quit.')
while True:
    # Loop through each button and check if it is pressed.
    for button in buttons:
        if lcd.is_pressed:
            lcd.clear()
