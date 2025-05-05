#!/usr/bin/python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
sum = first_number * second_number

if sum >0 :
    print(first_number , "x" , second_number , "=" , sum)
    print("The result is positive.")
elif sum <0 :
    print(first_number , "x" , second_number , "=" , sum)
    print("The result is negative.")
else :
    print(first_number , "x" , second_number , "=" , sum)
    print("The result is positive and negative.")