import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
# the setup
GPIO.setmode(GPIO.BCM) #sets the GPIO mode
GPIO.setwarnings(False) # do not show GPIO warnings
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as an output
lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
buttons = ( (LCD.SELECT),
            (LCD.LEFT),
            (LCD.UP),
            (LCD.DOWN),
            (LCD.RIGHT)
# the loop
while True:
  h,t = dht.read_retry(dht.DHT22, 17) #read DHT22
  t1 = t * 9/5.0 + 32 # Convert to F
  time.sleep(10) #sleep for 10 sec
  lcd.clear() # clear the lcd
  lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)) # print the DHT22 values in the lcd
  if t1 > 80: # explains itself
    lcd.set_color(1.0, 0.0, 0.0) # red
  if t1 < 80: # explains itself
    lcd.set_color(0.0, 1.0, 0.0) # green
  for button in buttons: # call the button function
    if lcd.is_pressed(LCD.SELECT):# its ether this
#    if lcd.is_pressed(SELECT):# or this, or mabey not who knows
      GPIO.output(18, GPIO.LOW) # set GPIO pin 18 low, relay on

