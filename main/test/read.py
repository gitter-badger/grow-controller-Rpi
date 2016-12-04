with open('/sys/class/gpio/gpio22/value') as gpio22:
  var22 = int(gpio22.read())
if var22 == 0:
  print "on"
elif var22 == 1:
  print "off"


