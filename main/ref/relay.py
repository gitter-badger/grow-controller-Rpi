import argparse
import RPi.GPIO as GPIO
import settings

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thermo", choices=['on', 'off'], help="thermo")
parser.add_argument("-f", "--fan", choices=['on', 'off'], help="fans")
parser.add_argument("-b", "--ballfan", choices=['on', 'off'], help="Ballast Fan")
parser.add_argument("-m", "--main", choices=['on', 'off'], help="HPS")
settings.pins()

pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan

args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin3, GPIO.OUT)#heater
GPIO.setup(pin4, GPIO.OUT)#ocfan
GPIO.setup(pin2, GPIO.OUT)#ballast fan
GPIO.setup(pin1, GPIO.OUT)#HPS

def heateron():
  GPIO.output(pin3, GPIO.LOW)#on
def heateroff():
  GPIO.output(pin3, GPIO.HIGH)#off
def fanon():
  GPIO.output(pin4, GPIO.LOW)#on
def fanoff():
  GPIO.output(pin4, GPIO.HIGH)#off
def ballaston():
  GPIO.output(pin2, GPIO.LOW)#on
def bballastoff():
  GPIO.output(pin2, GPIO.HIGH)#off
def mainon():
  GPIO.output(pin1, GPIO.LOW)#on
def mainoff():
  GPIO.output(pin1, GPIO.HIGH)#off

if args.thermo:
  if args.thermo == 'on':
    heateron()
    exit()
  elif args.thermo == 'off':
    heateroff()
    exit()
elif args.fan:
  if args.fan == 'on':
    fanon()
    exit()
  elif args.fan == 'off':
    fanoff()
    exit()
elif args.ballfan:
  if args.ballfan == 'on':
    ballaston()
    exit()
  elif args.ballfan == 'off':
    ballastoff()
    exit()
elif args.main:
  if args.main == 'on':
    mainon()
    exit()
  elif args.main == 'off':
    mainoff()
    exit()

#print parser.parse_args() #4 testing
