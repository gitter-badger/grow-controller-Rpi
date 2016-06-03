# need to shorten data prints 10 decimal points :(
import Adafruit_DHT as dht
h,t = dht.read_retry(dht.DHT22, 17)
t1 = t * 9/5.0 + 32 #convert data to F
print "C"
print t
print "F"
print t1

#print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t, h)
#print 'temp'
#print t * 9/5.0 + 32
#print 'humidity'
#print h

