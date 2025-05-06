#!/usr/bin/python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [x + 2 for x in a]
c = []
print(a)
print(b)
for num in b:
    if num > 5:
        c.append(num)
print(c)