# using https://www.adafruit.com/products/1110 lcd
# buttons need to do something
# This file gets invoked by Cron, installed by changing light cycle in menu

import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import time

lcd = LCD.Adafruit_CharLCDPlate()

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
