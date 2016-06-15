    # Mabey this will work, Test tomorrow durring  SD card redo
    # merge into lcd.py, test before reboot
    # TEST BEFORE REBOOT 
    #still not tested
    import time
    import Adafruit_CharLCD as LCD
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)

    lcd = LCD.Adafruit_CharLCDPlate()

    buttons = ( (LCD.SELECT),
                (LCD.LEFT),
                (LCD.UP),
                (LCD.DOWN),
                (LCD.RIGHT)

    print('Press Ctrl-C to quit.')
    while True:
        for button in buttons:
            if lcd.is_pressed(LCD.SELECT):# its ether this
#            if lcd.is_pressed(SELECT):# or this, or mabey not who knows
                GPIO.output(18, GPIO.LOW)

