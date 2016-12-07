
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser()
parser.add_argument("-h", "--heater", choices=['on', 'off'], help="wiring light")
parser.add_argument("-f", "--fan", choices=['on', 'off'], help="fans")
parser.add_argument("-b", "--ballastfan", choices=['on', 'off'], help="Ballast Fan")
parser.add_argument("-m", "--main", choices=['on', 'off'], help="HPS")

args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)#empty
GPIO.setup(23, GPIO.OUT)#fans
GPIO.setup(22, GPIO.OUT)#ballast fan
GPIO.setup(27, GPIO.OUT)#HPS

def hon():
  GPIO.output(18, GPIO.LOW)#on
def hoff():
  GPIO.output(18, GPIO.HIGH)#off
def fanon():
  GPIO.output(23, GPIO.LOW)#on
def fanoff():
  GPIO.output(23, GPIO.HIGH)#off
def bon():
  GPIO.output(22, GPIO.LOW)#on
def boff():
  GPIO.output(22, GPIO.HIGH)#off
def mon():
  GPIO.output(27, GPIO.LOW)#on
def moff():
  GPIO.output(27, GPIO.HIGH)#off

if args.wiring:
  if args.wiring == 'on':
    hon()
    exit()
  elif args.wiring == 'off':
    hoff()
    exit()
elif args.fan:
  if args.fan == 'on':
    fanon()
    exit()
  elif args.fan == 'off':
    fanoff()
    exit()
elif args.ballastfan:
  if args.ballastfan == 'on':
    bon()
    exit()
  elif args.ballastfan == 'off':
    boff()
    exit()
elif args.main:
  if args.main == 'on':
    mon()
    exit()
  elif args.main == 'off':
    moff()
    exit()

#print parser.parse_args() #4 testing
