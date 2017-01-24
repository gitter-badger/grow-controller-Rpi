#!/usr/bin/env bash
command -v apt >/dev/null 2>&1 || { echo "apt is not installed. not ubuntu?" >&2; exit 0; }
echo "want to install anything?: [y/n]"  
read yourch
sudo apt update
if [ $yourch = "y" ];
    then
        echo "what program would u like to install"
        read insch
        sudo apt install $insch
        sudo apt upgrade
        sudo apt dist-upgrade
        sudo apt autoremove
fi
if [ $yourch != "y" ];
    then
        sudo apt upgrade
        sudo apt dist-upgrade
        sudo apt autoremove
fi
exit
