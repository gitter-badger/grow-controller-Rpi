#!/bin/bash
while :
do
clear
fortune | cowsay -f tux 
echo "︻╦╤─--------------------!--------------------─╤╦︻"
echo "!  TOOLS                 ! RPi Grow controller    !"
echo "︻╦╤─--------------------!--------------------─╤╦︻"
echo "! [1] apt-get update     ! [a]                    !"
echo "! [2] apt-get upgrade    ! [b] 400HPS on  (GPIO3) !"
echo "! [3] apt-get dist-up    ! [c] 400HPS off (GPIO3) !"
echo "! [4] apt-get autoremove ! [d] T5 on      (GPIO4) !"
echo "! [5] crontab -e         ! [e] T5 off     (GPIO4) !"
echo "! [6] htop               ! [f] temp humidity      !"
echo "! [7] PROC temp          ! [g] watch DHT22        !"
echo "! [8] Check Space        ! [h] auth log           !"
echo "! [9] tail syslog        ! [i] Edit this Menu     !"
echo "! [0] Exit               ! [j] Shutdown           !"
echo "! [ ]                    ! [k] date               !"
echo "︻╦╤─--------------------!--------------------─╤╦︻"
echo -n "[1-0,a-k]: "
read yourch
case $yourch in
	1) sudo apt-get update && echo -n "Enter to continue"
                read yourch ;;
	2) sudo apt-get upgrade && echo -n "Enter to continue"
                read yourch ;;
	3) sudo apt-get dist-upgrade && echo -n "Enter to continue"
                read yourch ;;
	4) sudo apt-get autoremove && echo -n "Enter to continue"
                read yourch ;;
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
#	a)  ;;
	b) python /home/pi/HPSon.py && echo -n "Enter to continue"
                read yourch ;;
	c) python /home/pi/HPSoff.py && echo -n "Enter to continue"
                read yourch ;;
	d) python /home/pi/FLon.py && echo -n "Enter to continue"
                read yourch ;;
	e) python /home/pi/FLoff.py && echo -n "Enter to continue"
                read yourch ;;
	f) sudo python /home/pi/dht.py && echo -n "Enter to continue"
                read yourch ;;
	g) sudo python /home/pi/watchdht.py && echo -n "Enter to continue"
                read yourch ;;
	h) tail /var/log/auth.log && echo -n "Enter to continue"
                read yourch ;;
	i) sudo nano /home/pi/menu.sh && echo -n "Enter to continue"
                read yourch ;;
	j) sudo shutdown -h -P now ;;
	k) date && echo -n "Enter to continue"
                read yourch ;;
	0) exit 0 ;;
*) echo "really?";
echo "Press Enter to continue. . ." ; read ;;
esac
done
