#add lcd support
#using https://www.adafruit.com/products/1110 lcd
#waiting for lcd cant test. lcd shipping tomorrow
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import time
import os
import datetime

lcd = LCD.Adafruit_CharLCDPlate()

while True:
  h,t = dht.read_retry(dht.DHT22, 17)
  t1 = t * 9/5.0 + 32
  os.system('clear')
  print datetime.datetime.now()
  print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t, h)
  time.sleep(10)
  lcd.clear()
  lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h))
#  PRINT DHT VALUE ON LCD
# lcd.message(print 'T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)) #test
#  
  if t1 > 80
    lcd.set_color(1.0, 0.0, 0.0)#red
