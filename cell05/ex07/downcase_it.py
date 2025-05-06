#!/usr/bin/env python3

import sys

x = len(sys.argv)
y = sys.argv[1:]

if len(sys.argv) == 1 :
    print("none")
else :
    for i in y:
        print(i.lower(), end=" ")
    print()