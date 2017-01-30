#!/usr/bin/env python3
import time
import sys; print('Python %s on %s' % (sys.version, sys.platform))
while True:
    print("Select Default Editor")
    print("1) emacs")
    print("2) nano   <----Recommended")
    print("3) Vi     <----trolls love this editor")
    var1 = input("[1,2,3]:\n")
    if var1 == "1":
        print("try again")
    if var1 == "2":
        print("good choice")
        exit()
    if var1 == "3":
        for x in range(1,100):
            print("please remove all of my code from your storage")
            time.sleep(0.01)
        print("Thank You")
        time.sleep(5)
