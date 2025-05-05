#!/usr/bin/python3

num = input("Give me a number: ")
float_num = float(num)
int_num = int(float(num))

if float_num % 1 != 0 :
    x = int_num + 1
    print(x) 
else :
    print(int_num)
