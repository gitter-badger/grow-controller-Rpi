#!/bin/bash
while :
do
clear
fortune | cowsay -f tux #sudo apt-get install fortune cowsay -y
echo "︻╦╤─----------------─╤╦︻"
echo "!  TOOLS                 !"
echo "︻╦╤─----------------─╤╦︻"
echo "! [1] Light cycle change !"
echo "! [2] 400HPS on          !"
echo "! [3] 400HPS off         !"
echo "! [4] T5 on              !"
echo "! [5] T5 off             !"
echo "! [6] wiring light on    !"
echo "! [7] wiring light off   !"
echo "! [8] fans on            !"
echo "! [9] fans off           !"
echo "! [0] Exit               !"
echo "︻╦╤─----------------─╤╦︻"
echo -n "[1-0,a-k]: "
read yourch
case $yourch in
	1) python /home/pi/grow-controller-Rpi/main/ref/changeLightCycle.py && echo -n "Enter to continue"
                read yourch ;;
	2) python /home/pi/grow-controller-Rpi/main/ref/HPSon.py && echo -n "Enter to continue"
                read yourch ;;
	3) python /home/pi/grow-controller-Rpi/main/ref/HPSoff.py && echo -n "Enter to continue"
                read yourch ;;
	4) python /home/pi/grow-controller-Rpi/main/ref/FLon.py && echo -n "Enter to continue"
                read yourch ;;
	5) python /home/pi/grow-controller-Rpi/main/ref/FLoff.py && echo -n "Enter to continue"
                read yourch ;;
	6) python /home/pi/grow-controller-Rpi/main/ref/18on.py & echo -n "Enter to continue"
                read yourch ;;
  7) python /home/pi/grow-controller-Rpi/main/ref/18off.py & echo -n "Enter to continue"
                read yourch ;;
	8) python /home/pi/grow-controller-Rpi/main/ref/23on.py & echo -n "Enter to continue"
                read yourch ;;
  9) python /home/pi/grow-controller-Rpi/main/ref/23off.py & echo -n "Enter to continue"
                read yourch ;;
	0) exit 0 ;;
*) echo "really?";
echo "Press Enter to continue. . ." ; read ;;
esac
done
