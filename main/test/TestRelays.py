#trying to do commandline arguments
import argparse
import RPi.GPIO as GPIO
parser = argparse.ArgumentParser()
parser.add_argument("-won")#wiring lights on
parser.add_argument("-woff")#wiring lights off
parser.add_argument("-fanon")#
parser.add_argument("-fanoff")#
parser.add_argument("-flon")#
parser.add_argument("-floff")#
parser.add_argument("-on")#
parser.add_argument("-off")#
parser.add_argument("-on")#
parser.add_argument("-off")#


args = parser.parse_args()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)#wiring light
GPIO.setup(23, GPIO.OUT)#fans
GPIO.setup(22, GPIO.OUT)#FL
GPIO.setup(27, GPIO.OUT)#HPS
def wlon():
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

if args.won:
  wlon()
  exit()
elif args.woff:
  woff()
  exit()
elif args.fanon:
  fanon()
  exit()
elif args.fanoff:
  fanoff()
  exit()
elif args.flon:
  flon()
  exit()
elif args.floff:
  floff()
  exit()
elif args.hon:
  hon()
  exit()
elif args.hoff:
  hoff()
  exit()








