with open('/sys/class/gpio/gpio22/value') as gpio22:
  var1 = gpio22.read()
  print var1

