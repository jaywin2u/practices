#!/usr/bin/env python
#

number=0
while number <= 100000:
    for i in range(2,number):
        if number % i == 0:
            break
    else:
        print(str(number) + " is prime number")
    number+=1
