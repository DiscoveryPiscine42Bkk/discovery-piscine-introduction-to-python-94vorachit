#!/usr/bin/env python3

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = []
for x in range (x-1,y,1):
    x += 1
    z.append(x)
print(z)
#if len(sys.argv) > 1:
