#!/usr/bin/env python3

import sys
import re

x = len(sys.argv)
#print("parameters: ",x-1)
if x == 2:
    arr = re.findall("z",sys.argv[1])
    if len(arr) != 0:
        print(*arr, sep='')
    else :
        print("none")
else :
    print("none")

# * operator to unpack the list elements and the sep='' argument in the print()
# function to specify that no separator should be uesd between the elements.

