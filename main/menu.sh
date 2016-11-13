#!/bin/bash
while :
do
clear
fortune | cowsay -f tux #sudo apt-get install fortune cowsay -y
date +%F_%T
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo "!  MENU                  ! RPi Grow controller      !  GROWMASTER420         !"
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo "! [1] apt-get u/g/d/a/i  ! [a] Light menu           !                        !"
echo "! [2] calculate V/A      ! [b] Light Cycle          !                        !"
echo "! [3] w & last           ! [c]                      !                        !"
echo "! [4]                    ! [d]                      !                        !"
echo "! [5] crontab -e         ! [e] HDMI OFF             !                        !"
echo "! [6] htop               ! [f] network info         !                        !"
echo "! [7] processor temp     ! [g] watch DHT22          !                        !"
echo "! [8] Check Space        ! [h] auth log             !                        !"
echo "! [9] tail syslog        ! [i] Edit this Menu       !                        !"
echo "! [0] Exit               ! [j] Shutdown             !                        !"
echo "! [ ]                    ! [k] date                 !                        !"
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo -n "[1-0,a-k]: "
read yourch
case $yourch in
	1) bash /home/pi/grow-controller-Rpi/main/ref/update.sh && echo -n "Enter to continue"
                read yourch ;;
	2) python /home/pi/grow-controller-Rpi/main/ref/calc.py && echo -n "Enter to continue"
                read yourch ;;
	3) W && last && echo -n "Enter to continue"
                read yourch ;;
#	4) <command> && echo -n "Enter to continue"
#                read yourch ;;
	5) crontab -e &&  echo -n "Enter to continue"
                read yourch ;;
	6) htop && echo -n "Enter to continue"
                read yourch ;;
	7) vcgencmd measure_temp && echo -n "Enter to continue"
                read yourch ;;
	8) df -hT && echo -n "Enter to continue"
                read yourch ;;
	9) tail -f /var/log/syslog && echo -n "Enter to continue"
                read yourch ;;
	a) python /home/pi/grow-controller-Rpi/main/ref/relaymenu.py && echo -n "Enter to continue"
                read yourch ;;
	b) python /home/pi/grow-controller-Rpi/main/ref/changeLightCycle.py && echo -n "Enter to continue"
                read yourch ;;
        e) /opt/vc/bin/tvservice -o && echo -n "Enter to continue"
                read yourch ;;
        f) ifconfig && iwconfig wlan0 && echo -n "Enter to continue"
                read yourch ;;
	g) python /home/pi/grow-controller-Rpi/main/ref/watchdht.py && echo -n "Enter to continue"
                read yourch ;;
	h) tail /var/log/auth.log && echo -n "Enter to continue"
                read yourch ;;
	i) sudo nano /home/pi/grow-controller-Rpi/main/menu.sh && echo -n "Enter to continue"
                read yourch ;;
	j) sudo shutdown -h -P now ;;
	k) date && echo -n "Enter to continue"
                read yourch ;;
	0) exit 0 ;;
*) echo "really?";
echo "Press Enter to continue. . ." ; read ;;
esac
done
