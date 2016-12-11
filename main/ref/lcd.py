#  Adafruit 16x2 I2C PiPlate / simple, buttons and display script
#  simple lcd control
# buttons currently not in use
# more intergrations into this file must be made



from multiprocessing import Process
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import Adafruit_DHT as dht
import Adafruit_DHT
import sqlite3
from datetime import datetime
import time

conn = sqlite3.connect('dht.db')
c = conn.cursor()

# Read all the configured sensors from the DB.
c.execute('SELECT name, type, pin FROM sensors')
sensors = []
for row in c:
    name, dht_type, pin = row
    print('Configuring sensor: {0} of type: {1} on pin: {2}'.format(name, dht_type, pin))
    # Convert DHT type from string to DHT library value.
    if dht_type == 'DHT22':
        dht_type = Adafruit_DHT.DHT22
    elif dht_type == 'DHT11':
        dht_type = Adafruit_DHT.DHT11
    else:
        raise RuntimeError('Unknown sensor type: {0}'.format(dht_type))
    # Save the sensor into the list of configured sensors.
    sensors.append((name, dht_type, pin))

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
      if t < 35:
        lcd.set_color(0.0, 1.0, 0.0) # green = good temp
    if t > 35: # explains itself
      lcd.set_color(1.0, 0.0, 0.0) # red = too hot turn off extra lighting, fan at max
      lcd.clear()
      lcd.message(' TEMP TOO HIGH \n')
      time.sleep(5)
    if t < 20:
      lcd.set_color(0.0, 0.0, 1.0) # Blue = cold shut off a/c
      lcd.message('TEMP TOO LOW\n')
      time.sleep(5)
    time.sleep(1)
    lcd.clear() # clear the lcd
    lcd.message('T={0:0.1f} H={1:0.1f}\nF={2:0.1f} %s:%s:%s'.format(t, h, t1) % (now.hour, now.minute, now.second)) # print the DHT22 values in the lcd
    time.sleep(5)

def logVal():    
   while True:
    # Save the current unix time for this measurement.
    reading_time = int(time.time())
    # Go through each sensor and take a reading.
    for s in sensors:
        name, dht_type, pin = s
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, pin)
        #print('Read sensor: {0} humidity: {1:0.2f}% temperature: {2:0.2f}C'.format(name, humidity, tempera$
        # Save the reading in the readings table.
        c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                  (reading_time, '{0} Humidity'.format(name), humidity))
        c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                  (reading_time, '{0} Temperature'.format(name), temperature))
        conn.commit()
    time.sleep(10.0)

''' 
def lcdBut(): #button functions !!!NOT IN USE!!!
  while True:
    time.sleep(0.1) # without this time.sleep, 23% cpu usage. with 3%
    if lcd.is_pressed(LCD.SELECT):
    if lcd.is_pressed(LCD.UP):
      GPIO.output(18, GPIO.LOW)
    elif lcd.is_pressed(LCD.DOWN):
      GPIO.output(18, GPIO.HIGH)
    elif lcd.is_pressed(LCD.LEFT):
      GPIO.output(22, GPIO.LOW)
    elif lcd.is_pressed(LCD.RIGHT):
      GPIO.output(22, GPIO.HIGH)
'''


if __name__ == '__main__': #run the above functions in the background, FOREVER!!!!!!!!!!!!!!!!!!!!!
  Process(target=logVal).start()
  Process(target=lcdDis).start()
#  Process(target=lcdBut).start() #NOT IN USE
