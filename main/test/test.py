
###PiPlate buttons

while True:
    time.sleep(0.5)  # without this time.sleep, 23% cpu usage. with 3%
    if lcd.is_pressed(LCD.UP):
        GPIO.output(pin1, GPIO.LOW)  # on
    if lcd.is_pressed(LCD.DOWN):
        GPIO.output(pin1, GPIO.HIGH)  # off
