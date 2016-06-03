#!!!!WARNING REPLACES CURRENT CRONTAB!!!!
#
#
import os

print"Set light cycle"
print"!!!! WARNING  REPLACES   CURRENT  CRONTAB !!!!"
print"!!!! CHECK YOUR CRONTAB WITH $ crontab -l !!!!"
print"Ctrl-C to EXIT"
t = input("12 or 18\n$")
if t == 12:
        print"light cycle set to\nFLOWER"
        os.system("crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower")#insert command
if t == 18:
        print"light cycle set to\nVEG"
        os.system("crontab /home/pi/grow-controller-Rpi/main/ref/crontab.veg")#insert command
else:
        exit()
