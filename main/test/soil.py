# Testing soil resistive levels
# yl-38 yl-69 mcp3008
# 
# mcp3008 not ordered yet
#
# cd ~
# git clone git://github.com/doceme/py-spidev
# cd py-spidev/
# sudo python setup.py install
#
import time
import mcp3008

while True:
    m = mcp3008.readadc(5)
    print "Moisture level: {:>5} ".format(m)
    time.sleep(0.5)
    #read_pct()
    print(m)
