#  Adafruit 16x2 I2C PiPlate / simple, buttons and display script
#  simple lcd control

from multiprocessing import Process
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
from datetime import datetime
import time

lcd = LCD.Adafruit_CharLCDPlate() # defines lcd
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT) #18 = wiring light 
GPIO.setup(22, GPIO.OUT) #22 = veg light

def lcdDis(): #display function
  while True:
    now = datetime.now()
    h,t = dht.read_retry(dht.DHT22, 17) #read DHT22
    time.sleep(1)
    t1 = t * 9/5.0 + 32

    if t > 20:
      if t < 29:
        lcd.set_color(0.0, 1.0, 0.0) # green = good temp
    if t > 29: # explains itself
      lcd.set_color(1.0, 0.0, 0.0) # red = too hot turn off extra lighting, fan at max
      lcd.clear()
      lcd.message(' TEMP TOO HIGH \n')
      time.sleep(5)
    if t < 20:
     lcd.set_color(0.0, 0.0, 1.0) # Blue = cold shut off a/c

    time.sleep(1)
    lcd.clear() # clear the lcd
    lcd.message('T={0:0.1f} H={1:0.1f}\nF={2:0.1f} %s:%s:%s'.format(t, h, t1) % (now.hour, now.minute, now.second)) # print the DHT22 values in the lcd
    time.sleep(5)
#def lcdBut(): #button functions
#  while True:
#    time.sleep(0.1) # without this time.sleep, 23% cpu usage. with 3%
#    if lcd.is_pressed(LCD.SELECT):
#    if lcd.is_pressed(LCD.UP):
#      GPIO.output(18, GPIO.LOW)
#    elif lcd.is_pressed(LCD.DOWN):
#      GPIO.output(18, GPIO.HIGH)
#    elif lcd.is_pressed(LCD.LEFT):
#      GPIO.output(22, GPIO.LOW)
#    elif lcd.is_pressed(LCD.RIGHT):
#      GPIO.output(22, GPIO.HIGH)


if __name__ == '__main__': #run the above functions in the background, FOREVER!!!!!!!!!!!!!!!!!!!!!
  Process(target=lcdDis).start()
#  Process(target=lcdBut).start()


