with open('/sys/class/gpio/gpio22/value') as gpio18:
  var18 = int(gpio18.read())
if var18 == 0:
  print "on"
elif var18 == 1:
  print "off"

with open('/sys/class/gpio/gpio22/value') as gpio22:
  var22 = int(gpio22.read())
if var22 == 0:
  print "on"
elif var22 == 1:
print "off"

with open('/sys/class/gpio/gpio22/value') as gpio23:
  var23 = int(gpio23.read())
if var23 == 0:
  print "on"
elif var23 == 1:
print "off"

with open('/sys/class/gpio/gpio22/value') as gpio27:
  var27 = int(gpio27.read())
if var27 == 0:
  print "on"
elif var27 == 1:
print "off"

