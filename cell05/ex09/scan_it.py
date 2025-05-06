#!/usr/bin/env python3

import sys
import re

first = sys.argv[2:]
second = str(sys.argv[1])

print(second)
#result = re.findall(second,first)
#print(result)
#x = len(sys.argv)
#y = sys.argv[1:]
#z = []
##print(x)

if len(sys.argv) <= 2:
    print("none")
else :
    result = re.findall(r"second",first)
    print(result)
#    for char in y:
#        if char.isalpha():
#            z.append(char)
#    print(z[::-1])
#    for i in range (-1, -len(z)-1, -1):
#        print(z[i],end=" ")
#        print()
