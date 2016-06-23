#combined cron lcd.py
#test 4 cpu usage
from multiprocessing import Process
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import time

lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def lcdDis():
  while True:
    h,t = dht.read_retry(dht.DHT22, 17) #read DHT22
    t1 = t * 9/5.0 + 32 # Convert to F
    lcd.clear() # clear the lcd
    lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)) # print the DHT22 values in the lcd
    if t1 > 80: # explains itself
      lcd.set_color(1.0, 0.0, 0.0) # red = too hot turn off extra lighting, fan at max
    if t1 > 69:
      lcd.set_color(0.0, 1.0, 0.0) # green = good temp
    if t1 < 69: 
     lcd.set_color(0.0, 0.0, 1.0) # Blue = cold shut off a/c
    time.sleep(10)
  
def lcdBut():
  while True:
    time.sleep(0.1) # without this time.sleep, 23% cpu usage. with 3%
#    if lcd.is_pressed(LCD.SELECT):
    if lcd.is_pressed(LCD.UP):
      GPIO.output(18, GPIO.LOW)
    if lcd.is_pressed(LCD.DOWN):
      GPIO.output(18, GPIO.HIGH)
    if lcd.is_pressed(LCD.LEFT):
      GPIO.output(23, GPIO.LOW)
    if lcd.is_pressed(LCD.RIGHT):
      GPIO.output(23, GPIO.HIGH)
  

if __name__ == '__main__':
  Process(target=lcdDis).start()
  Process(target=lcdBut).start()
  
  
 
  
