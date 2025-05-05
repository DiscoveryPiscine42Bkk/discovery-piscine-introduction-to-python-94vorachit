#!/usr/bin/python3

age = int(input("Please tell me your age: "))
i = 1
print("you are currently", age , "years old.")
while i <=3 :
    print("In", i * 10 , "years, you'll be", age + i*10 ,"years old.")
    i += 1