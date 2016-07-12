# Testing soil resistive levels
# yl-38 yl-69 < these might not be what im looking for/testing not going well
# mcp3008
# 
# lcd.py is a good place for this
#
# mcp3008 not ordered yet
#
# https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008?view=all
#
# cd ~
# git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
# cd Adafruit_Python_MCP3008
# sudo python setup.py install
#

import time
import mcp3008

while True:
    read_adc(0)
    read_adc(1)
    read_adc(2)
    read_adc(3)
    
