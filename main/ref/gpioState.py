# make more useful 
# relay menu depends on this for state, must update for future changes
### file depends on crontab opening system gpio



import settings

settings.pins()

pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan

def relay1():
  with open('/sys/class/gpio/gpio', pin1'/value') as gpio1:
    var1 = int(gpio1.read())
  if var1 == 0:
    print "on"
  elif var1 == 1:
    print "off"

def relay2():
  with open('/sys/class/gpio/gpio', pin2'/value') as gpio2:
    var2 = int(gpio2.read())
  if var2 == 0:
    print "on"
  elif var2 == 1:
    print "off"

def relay3():
  with open('/sys/class/gpio/gpio', pin3'/value') as gpio3:
    var3 = int(gpio3.read())
  if var3 == 0:
    print "on"
  elif var3 == 1:
    print "off"

def relay4():
  with open('/sys/class/gpio/gpio', pin4'/value') as gpio4:
    var4 = int(gpio4.read())
  if var4 == 0:
    print "on"
  elif var4 == 1:
    print "off"

    
if __name__ == "__main__":
  relay1()
  relay2()
  relay3()
  relay4()
