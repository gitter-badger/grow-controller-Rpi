import Adafruit_DHT as dht
import time
import os
import datetime

while True:
        h,t = dht.read_retry(dht.DHT22, 17)
        time.sleep(8.0)
        t1 = t * 9/5.0 + 32
        os.system('clear')
        print datetime.datetime.now().strftime("%H:%M:%S")
        print 'T={0:0.1f}*F\nH={1:0.1f}%'.format(t1, h)
