#!/usr/bin/env python3

import sys
def downcase_it():
    if len(sys.argv) > 1:
        for word in sys.argv[1:] :
            print(word.lower())
    else :
        print("none")

downcase_it()