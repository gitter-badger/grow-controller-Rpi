import Adafruit_DHT as dht
import time
import os
import datetime

def temp():
  h,t = dht.read_retry(dht.DHT22, 17) #read DHT22 value, set pi
  print datetime.datetime.now().strftime("%H:%M:%S")
  print 'T={0:0.1f}*C\nH={1:0.1f}%'.format(t, h)

while True:
  time.sleep(8.0)
  os.system('clear')
  temp()
