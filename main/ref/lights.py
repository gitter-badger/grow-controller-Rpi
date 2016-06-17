import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

print "︻╦╤─----------------─╤╦︻"
print "!  TOOLS                 !"
print "︻╦╤─----------------─╤╦︻"
print "! [1] Light cycle change !"
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
if var == 1:
elif var == 2:
elif var == 3:
elif var == 4:
elif var == 5:
elif var == 6:
elif var == 7:
  GPIO.output(18, GPIO.HIGH)#off
elif var == 8:
elif var == 9:
elif var == 0:
