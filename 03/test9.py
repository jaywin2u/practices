#!/usr/bin/env python
#
number=int(input(">>> "))
for i in range(2,number):
    if number % i == 0:
        break
else:
    print(str(number) + " is prime number")
