#simple argparse relay control
#usage $ python relay.py -h #output will explain usage
#MAKING SOMETHING SIMPLE,,,,, COMPLICATED
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wiring", choices=['on', 'off'], help="wiring light")
parser.add_argument("-f", "--fan", choices=['on', 'off'], help="fans")
parser.add_argument("-t", "--tlight", choices=['on', 'off'], help="t5 light")
parser.add_argument("-m", "--main", choices=['on', 'off'], help="HPS")

args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)#wiring light
GPIO.setup(23, GPIO.OUT)#fans
GPIO.setup(22, GPIO.OUT)#FL
GPIO.setup(27, GPIO.OUT)#HPS

def won():
  GPIO.output(18, GPIO.LOW)#on
def woff():
  GPIO.output(18, GPIO.HIGH)#off
def fanon():
  GPIO.output(23, GPIO.LOW)#on
def fanoff():
  GPIO.output(23, GPIO.HIGH)#off
def flon():
  GPIO.output(22, GPIO.LOW)#on
def floff():
  GPIO.output(22, GPIO.HIGH)#off
def hon():
  GPIO.output(27, GPIO.LOW)#on
def hoff():
  GPIO.output(27, GPIO.HIGH)#off

if args.wiring:
  if args.wiring == 'on':
    won()
    exit()
  elif args.wiring == 'off':
    woff()
    exit()
elif args.fan:
  if args.fan == 'on':
    fanon()
    exit()
  elif args.fan == 'off':
    fanoff()
    exit()
elif args.tlight:
  if args.tlight == 'on':
    flon()
    exit()
  elif args.tlight == 'off':
    floff()
    exit()
elif args.main:
  if args.main == 'on':
    hon()
    exit()
  elif args.main == 'off':
    hoff()
    exit()

#print parser.parse_args() #4 testing
