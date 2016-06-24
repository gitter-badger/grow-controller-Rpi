#  Adafruit 16x2 I2C PiPlate / simple, buttons and display script
#  simple lcd control

from multiprocessing import Process
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import time

lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def lcdDis(): #display function
  while True:
    h,t = dht.read_retry(dht.DHT22, 17) #read DHT22
    t1 = t * 9/5.0 + 32 ''' Convert to F # this function fails constantly!!!!!! sad i was born in the backwards US, 
    F is all i know, i have a suspicion that it the adafruit libary(blaming anyone but me for my mistakes, LOL) '''
    lcd.clear() # clear the lcd
    lcd.message('T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)) # print the DHT22 values in the lcd
    if t1 > 69:
      if t1 < 80:
        lcd.set_color(0.0, 1.0, 0.0) # green = good temp
    elif t1 > 80: # explains itself
      lcd.set_color(1.0, 0.0, 0.0) # red = too hot turn off extra lighting, fan at max
    elif t1 < 69: 
     lcd.set_color(0.0, 0.0, 1.0) # Blue = cold shut off a/c
    time.sleep(10)
  
def lcdBut(): #button functions
  while True:
    time.sleep(0.1) # without this time.sleep, 23% cpu usage. with 3%
#    if lcd.is_pressed(LCD.SELECT):
    if lcd.is_pressed(LCD.UP):
      GPIO.output(18, GPIO.LOW)
    elif lcd.is_pressed(LCD.DOWN):
      GPIO.output(18, GPIO.HIGH)
    elif lcd.is_pressed(LCD.LEFT):
      GPIO.output(23, GPIO.LOW)
    elif lcd.is_pressed(LCD.RIGHT):
      GPIO.output(23, GPIO.HIGH)
  

if __name__ == '__main__': #run the above functions in the background, FOREVER!!!!!!!!!!!!!!!!!!!!!
  Process(target=lcdDis).start()
  Process(target=lcdBut).start()
