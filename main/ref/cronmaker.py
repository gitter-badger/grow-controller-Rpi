#import os
import settings
settings.pins()
settings.light()
pin1 = settings.ballast
pin2 = settings.ballastfan
pin3 = settings.heater
pin4 = settings.ocfan
lightOn = settings.lightOn
lightOff = settings.lightOff
print("@reboot python /home/pi/grow-controller-Rpi/main/ref/boot.py")
print("@reboot python /home/pi/grow-controller-Rpi/main/ref/lcd.py &")
print("@reboot sudo echo", pin1, "/sys/class/gpio/export")
print("@reboot sudo echo", pin2, "/sys/class/gpio/export")
print("@reboot sudo echo", pin3, "/sys/class/gpio/export")
print("@reboot sudo echo", pin4, "/sys/class/gpio/export")
print("0", lightOn, "* * * python /home/pi/grow-controller-Rpi/main/ref/relay.py -m on")
print("0", lightOff, "* * * python /home/pi/grow-controller-Rpi/main/ref/relay.py -m off")
print("0", lightOn, "* * * python /home/pi/grow-controller-Rpi/main/ref/relay.py -b on")
print("0", lightOff, "* * * python /home/pi/grow-controller-Rpi/main/ref/relay.py -b off")
