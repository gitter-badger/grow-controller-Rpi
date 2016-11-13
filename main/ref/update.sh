command -v apt >/dev/null 2>&1 || { echo "apt is not installed. not ubuntu?" >&2; exit 0; }
echo "want to install anything?: [y/n]"  
read yourch
apt update
if [ $yourch = "y" ];
  then
    echo "what program would u like to install"
    read insch
    apt install $insch -y
    apt upgrade -y
    apt dist-upgrade -y
    apt autoremove -y
else
    apt upgrade -y
    apt dist-upgrade -y
    apt autoremove -y
fi
exit
