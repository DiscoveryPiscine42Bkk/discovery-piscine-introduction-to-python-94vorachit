#!/usr/bin/env python3

import sys

y = sys.argv[1:]
z = []

def shrink():
    x = slice(8)
    for arg1 in y:
        z.append(arg1[x])

def enlarge():
    for arg2 in z:
        i = len(arg2)
        for i in range (i,8,1):
            arg2 += "z"
        print(arg2)

if len(sys.argv) > 1 :

    shrink()
#    shrink()
#    x = slice(8)
#    for arg1 in y:
#        z.append(arg1[x])
#        for int(len(arg)) in range (8):
#            arg +="z"
#    print(z)
    enlarge()
#    for arg2 in z:
#        i = len(arg2)
#        for i in range (i,8,1):
#            arg2 += "z"
#        print(arg2)
else :
    print("none")
