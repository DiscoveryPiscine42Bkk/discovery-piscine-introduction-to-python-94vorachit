#!/usr/bin/env python3

import sys

x = len(sys.argv)
#print("parameters: ",x-1)
y = sys.argv[1:]
#print(y)
z = []
if x > 2:
    for char in y:
        if char.isalpha():
            z.append(char)
    print("parameters: ",len(z))
    for i in range (len(z)):
        print(z[i], ":" , len(z[i]))
else :
    print("none")