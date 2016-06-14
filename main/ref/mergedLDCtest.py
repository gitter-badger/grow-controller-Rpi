import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
lcd = LCD.Adafruit_CharLCDPlate()

buttons = ( (LCD.SELECT),
            (LCD.LEFT),
            (LCD.UP),
            (LCD.DOWN),
            (LCD.RIGHT)


while True:
  h,t = dht.read_retry(dht.DHT22, 17)
  t1 = t * 9/5.0 + 32
  time.sleep(10)
  lcd.clear()
  lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h))
  if t1 > 80:
    lcd.set_color(1.0, 0.0, 0.0)#red
  if t1 < 80:
    lcd.set_color(0.0, 1.0, 0.0)#green
  for button in buttons:
    if lcd.is_pressed(LCD.SELECT):# its ether this
#    if lcd.is_pressed(SELECT):# or this, or mabey not who knows
      GPIO.output(18, GPIO.LOW)

