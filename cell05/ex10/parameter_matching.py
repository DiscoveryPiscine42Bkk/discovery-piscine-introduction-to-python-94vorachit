#!/usr/bin/env python3

import sys

x = len(sys.argv)
#print(x)
if x == 1:
    print("none")
else :
    word = input("What was the parameter? ")
    if word == sys.argv[1]:
        print("Good job!")
    else :
        print("Nope, sorry...")