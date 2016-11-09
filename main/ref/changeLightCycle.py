#!!!!WARNING REPLACES CURRENT CRONTAB!!!!
#
#
import os
print"Set light cycle"
print"!!!! WARNING  REPLACES   CURRENT  CRONTAB !!!!"
print"!!!! CHECK YOUR CRONTAB WITH $ crontab -l !!!!"
print"Ctrl-C to EXIT"
print"12 is flower ON=11:00 OFF=23:00"
print"18 is veg ON=19:00 OFF=13:00"
print"2 = two room setup"
print"press 9 to edit files"
t = input("12, 18, 2, or 9\n$")
if t == 12:
  print"light cycle set to\nFLOWER"
  os.system("crontab /home/pi/grow-controller-Rpi/main/ref/crontab.flower")
if t == 18:
  print"light cycle set to\nVEG"
  os.system("crontab /home/pi/grow-controller-Rpi/main/ref/crontab.veg")
if t == 2:
  print"light cycle set to\nTwo Rooms, One Grow Controller"
  os.system("crontab /home/pi/grow-controller-Rpi/main/ref/crontab.tworoom")
if t == 9:
  print"select file to edit; 12,18,or 2 "
  s = input("12, 18 or 2")
  if s == 12:
    os.system("nano /home/pi/grow-controller-Rpi/main/ref/crontab.flower")
  if s == 18:
    os.system("nano /home/pi/grow-controller-Rpi/main/ref/crontab.veg")
  if s == 2:
    os.system("nano /home/pi/grow-controller-Rpi/main/ref/crontab.tworoom")  
else:
  exit()
