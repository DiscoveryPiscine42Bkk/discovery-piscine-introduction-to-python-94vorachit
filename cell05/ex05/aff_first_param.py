#!/usr/bin/env python3

import sys

x = len(sys.argv)
y = sys.argv[1:]

if len(sys.argv) == 1 :
    print("none")
else :
    for char in y:
        if char.isalpha():
            print(char, end=" ")
    print()