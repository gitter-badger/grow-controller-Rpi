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
print(gpstate1)  # 0 == on, 1 == off
print(gpstate2)  # 0 == on, 1 == off
print(gpstate3)  # 0 == on, 1 == off
print(gpstate4)  # 0 == on, 1 == off
