#trying to do commandline arguments
import argparse
import RPi.GPIO as GPIO
parser = argparse.ArgumentParser()
parser.add_argument("-won")#wiring lights
parser.add_argument("-woff")
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
  
if args.won:
  wlon()
  exit()
elif args.woff:
  woff()
  exit()










