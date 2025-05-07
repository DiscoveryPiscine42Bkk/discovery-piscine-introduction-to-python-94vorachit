#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 2:
    result = re.findall(sys.argv[1],sys.argv[2])
    print(len(result))
else :
    print("none")
