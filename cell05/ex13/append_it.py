#!/usr/bin/env python3

import sys
import re

x = len(sys.argv)
y = sys.argv[1:]
z = []
if x > 1:
#    array = re.findall(r".ism",str(sys.argv[1:]))
    for arg in y:
        if arg.endswith("ism"):
            z.append(arg)
        else :
            print(arg+"ism")
#    print(z)
#    print("")
else :
    print("none")
# * operator to unpack the list elements and the sep='' argument in the print()
# function to specify that no separator should be uesd between the elements.
