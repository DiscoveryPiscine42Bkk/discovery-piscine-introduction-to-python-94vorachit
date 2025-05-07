#!/usr/bin/env python3

num = input("Give me a number: ")
float_number = float(num)

if  float_number % 1 ==  0:
    print("This number is an integer.")
else :
    print("This number is a decimal.")