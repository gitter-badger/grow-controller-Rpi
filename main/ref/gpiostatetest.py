import gpioState
###call the functions###
gpioState.relay1()
gpioState.relay2()
gpioState.relay3()
gpioState.relay4()

###Set Variables######
gpstate1 = gpioState.state1  # ballast
gpstate2 = gpioState.state2  # ballast fan
gpstate3 = gpioState.state3  # heater
gpstate4 = gpioState.state4  # ocfan

###Print Variables######
print(gpstate1)
print(gpstate2)
print(gpstate3)
print(gpstate4)
