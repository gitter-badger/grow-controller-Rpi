import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import time

lcd = LCD.Adafruit_CharLCDPlate() # defines lcd

while True:
  h,t = dht.read_retry(dht.DHT22, 17) #read DHT22
  t1 = t * 9/5.0 + 32 # Convert to F
  time.sleep(10) #sleep for 10 sec
  lcd.clear() # clear the lcd
  lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)) # print the DHT22 values in the lcd
  if t1 > 80: # explains itself
    lcd.set_color(1.0, 0.0, 0.0) # red
  if t1 < 80: # explains itself
    if t1 > 69:
      lcd.set_color(0.0, 1.0, 0.0) # green
  if t1 < 69: 
    lcd.set_color(0.0, 0.0, 1.0) # Blue?
