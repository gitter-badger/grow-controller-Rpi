import settings

settings.expGpio()
pinvar1 = settings.gp1
pinvar2 = settings.gp2
pinvar3 = settings.gp3
pinvar4 = settings.gp4

def relay1():
  with open(pinvar1) as gpio1:
    var1 = int(gpio1.read())
  if var1 == 0:
    print "on"
  elif var1 == 1:
    print "off"
def relay2():
  with open(pinvar2) as gpio2:
    var2 = int(gpio2.read())
  if var2 == 0:
    print "on"
  elif var2 == 1:
    print "off"
def relay3():
  with open(pinvar3) as gpio3:
    var3 = int(gpio3.read())
  if var3 == 0:
    print "on"
  elif var3 == 1:
    print "off"
def relay4():
  with open(pinvar4) as gpio4:
    var4 = int(gpio4.read())
  if var4 == 0:
    print "on"
  elif var4 == 1:
    print "off"


    
if __name__ == "__main__":
  print "relay1"
  relay1()
  print "relay2"
  relay2()
  print "relay3"
  relay3()
  print "relay4"
  relay4()
