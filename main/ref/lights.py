import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

print "︻╦╤─----------------─╤╦︻"
print "!  TOOLS                 !"
print "︻╦╤─----------------─╤╦︻"
print "! [1]                   !"
print "! [2] 400HPS on          !"
print "! [3] 400HPS off         !"
print "! [4] T5 on              !"
print "! [5] T5 off             !"
print "! [6] wiring light on    !"
print "! [7] wiring light off   !"
print "! [8] fans on            !"
print "! [9] fans off           !"
print "! [0] Exit               !"
print "︻╦╤─----------------─╤╦︻"
var = input("[1-0,a-k]: ")
while True:
  if var == 1:
  elif var == 2:
    GPIO.output(27, GPIO.LOW)#on
  elif var == 3:
    GPIO.output(27, GPIO.HIGH)#off
  elif var == 4:
    GPIO.output(22, GPIO.LOW)#on
  elif var == 5:
    GPIO.output(22, GPIO.HIGH)#off
  elif var == 6:
    GPIO.output(18, GPIO.LOW)#on
  elif var == 7:
    GPIO.output(18, GPIO.HIGH)#off
  elif var == 8:
    GPIO.output(23, GPIO.LOW)#on
  elif var == 9:
    GPIO.output(23, GPIO.HIGH)#off
  elif var == 0:
    exit()
