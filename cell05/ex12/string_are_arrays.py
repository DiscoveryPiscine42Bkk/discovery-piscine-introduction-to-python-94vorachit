#!/usr/bin/env python3

import sys
import re

x = len(sys.argv)
#print("parameters: ",x-1)
y = sys.argv[1:]
#print(y)
z = []
if x == 1:
    print("none")
else :
    arr = re.findall("z",str(y))
#    print(len(arr))
    if len(arr) != 0:
        print(*arr, sep='')
    else :
        print("none")

# * operator to unpack the list elements and the sep='' argument in the print()
# function to specify that no separator should be uesd between the elements.

