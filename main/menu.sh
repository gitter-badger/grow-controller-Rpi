#!/usr/bin/env bash
while :
do
clear
fortune | cowsay -f tux # sudo apt install fortune cowsay -y
uptime
echo "All settings are in settings.py. Selection [l]"
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo "!  MENU                  ! RPi Grow controller      !  GROWMASTER420         !"
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo "! [1] apt-get u/g/d/a/i  ! [a] Light menu           ! [l] edit settings.py    !"
echo "! [2] calculate V/A      ! [b] crontab maker        ! [m] SelectDefaultEditor !"
echo "! [3] w & last           ! [c] GPIO state           ! [n] Reset I2C bus       !"
echo "! [4] root crontab -l    ! [d] Start main.py &      ! [o] All Relays Off      !"
echo "! [5] root crontab -e    ! [e] HDMI OFF             ! [p]                     !"
echo "! [6] htop               ! [f] network info         ! [q]                     !"
echo "! [7] processor temp     ! [g]                      ! [r]                     !"
echo "! [8] Check Space        ! [h] auth log             ! [s]                     !"
echo "! [9] tail syslog        ! [i] Edit this Menu       ! [t]                     !"
echo "! [0] Exit               ! [j] Shutdown             ! [u]                     !"
echo "! [ ]                    ! [k] date                 ! [v]                     !"
echo "︻╦╤─--------------------*==========================*---------------------─╤╦︻"
echo -n "[1-0,a-k]: "
read yourch
case $yourch in
    1) bash /home/pi/grow-controller-Rpi/main/ref/update.sh && echo -n "Enter to continue"
        read yourch ;;
    2) python3 /home/pi/grow-controller-Rpi/main/ref/calc.py && echo -n "Enter to continue"
        read yourch ;;
    3) W && last && echo -n "Enter to continue"
        read yourch ;;
    4) sudo crontab -l && echo -n "Enter to continue"
        read yourch ;;
    5) sudo crontab -e &&  echo -n "Enter to continue"
        read yourch ;;
    6) htop && echo -n "Enter to continue"
        read yourch ;;
    7) vcgencmd measure_temp && echo -n "Enter to continue"
        read yourch ;;
    8) df -hT && echo -n "Enter to continue"
        read yourch ;;
    9) tail -f /var/log/syslog && echo -n "Enter to continue"
        read yourch ;;
    a) python3 /home/pi/grow-controller-Rpi/main/ref/relaymenu.py && echo -n "Enter to continue"
        read yourch ;;
    b) python3 /home/pi/grow-controller-Rpi/main/ref/cronmaker.py && echo -n "Enter to continue"
        read yourch ;;
    c) python3 /home/pi/grow-controller-Rpi/main/ref/gpioState.py && echo -n "Enter to continue"
        read yourch ;;
    d) python3 /home/pi/grow-controller-Rpi/main/ref/main.py & echo -n "Enter to continue"
        read youch ;;	
    e) /opt/vc/bin/tvservice -o && echo -n "Enter to continue"
        read yourch ;;
    f) ifconfig && iwconfig wlan0 && echo -n "Enter to continue"
        read yourch ;;
#    g) python3 /home/pi/grow-controller-Rpi/main/ref/ && echo -n "Enter to continue"
#        read yourch ;;
    h) tail /var/log/auth.log && echo -n "Enter to continue"
        read yourch ;;
    i) nano /home/pi/grow-controller-Rpi/main/menu.sh && echo -n "Enter to continue"
        read yourch ;;
    j) echo -n 'shutdown? [y/n]'
        read Var1 -n
           if [ $Var1 = 'y' ] ; then
             echo 'sudo shutdown -h -P now'
             sleep 5
             sudo shutdown -h -P now
           fi ;;
    k) date && echo -n "Enter to continue"
        read yourch ;;
    l) nano /home/pi/grow-controller-Rpi/main/ref/settings.py && echo -n "Enter to continue"
        read yourch ;;
    m) python3 /home/pi/grow-controller-Rpi/main/ref/selectEditor.py && echo -n "Enter to continue"
        read yourch ;;
    n) sudo modprobe -r i2c_bcm2708 && sudo modprobe i2c_bcm2708 baudrate=100010 && echo -n "Enter to continue"
        read yourch ;;
    o) python3 /home/pi/grow-controller-Rpi/main/ref/alloff.py && echo -n "Enter to continue"
        read yourch ;;
    0) exit 0 ;;
*) echo "really?";
echo "Press Enter to continue. . ." ; read ;;
esac
done
