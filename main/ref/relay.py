import argparse
import RPi.GPIO as GPIO
import settings

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thermo", choices=['on', 'off'], help="thermo")
parser.add_argument("-f", "--fan", choices=['on', 'off'], help="fans")
parser.add_argument("-b", "--ballfan", choices=['on', 'off'], help="Ballast Fan")
parser.add_argument("-m", "--main", choices=['on', 'off'], help="HPS")
settings.pins()
args = parser.parse_args()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


###(main/ballast)###
pin1 = settings.ballast
GPIO.setup(pin1, GPIO.OUT)#HPS
def mainon():
  GPIO.output(pin1, GPIO.LOW)#on
def mainoff():
  GPIO.output(pin1, GPIO.HIGH)#off
if args.main:
  if args.main == 'on':
    mainon()
    exit()
  elif args.main == 'off':
    mainoff()
    exit()
###(ballast cooling)###
pin2 = settings.ballastfan
GPIO.setup(pin2, GPIO.OUT)#ballast fan
def ballaston():
  GPIO.output(pin2, GPIO.LOW)#on
def bballastoff():
  GPIO.output(pin2, GPIO.HIGH)#off
if args.ballfan:
  if args.ballfan == 'on':
    ballaston()
    exit()
  elif args.ballfan == 'off':
    ballastoff()
    exit()
###(heater)###
pin3 = settings.heater
GPIO.setup(pin3, GPIO.OUT)#heater    
def heateron():
  GPIO.output(pin3, GPIO.LOW)#on
def heateroff():
  GPIO.output(pin3, GPIO.HIGH)#off
if args.thermo:
  if args.thermo == 'on':
    heateron()
    exit()
  elif args.thermo == 'off':
    heateroff()
    exit()
###(ocfan)###
pin4 = settings.ocfan
GPIO.setup(pin4, GPIO.OUT)#ocfan  
def fanon():
  GPIO.output(pin4, GPIO.LOW)#on
def fanoff():
  GPIO.output(pin4, GPIO.HIGH)#off
if args.fan:
  if args.fan == 'on':
    fanon()
    exit()
  elif args.fan == 'off':
    fanoff()
    exit()

#print parser.parse_args() #4 testing
