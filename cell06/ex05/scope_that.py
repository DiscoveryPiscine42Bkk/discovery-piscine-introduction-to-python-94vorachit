#!/usr/bin/env python3

import sys

y = int(sys.argv[1])

def add_one():
    y + 1
#    print(y)
    
if len(sys.argv) > 1:
    print(y)
    add_one()
    print(y)
else :
    print("none")