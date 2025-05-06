#!/usr/bin/env python3

import sys

x = len(sys.argv)
y = sys.argv[1:]
z = []
#print(x)
if x <= 2:
    print("none")
else :
    for char in y:
        if char.isalpha():
            z.append(char)
#    print(z[::-1])
    for i in range (-1, -len(z)-1, -1):
        print(z[i],end=" ")
        print()