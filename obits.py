#!/usr/bin/env python
num = int(input('Input a number: '))
if num//10000:
    print("5")
elif num//1000:
    print("4")
elif num//100:
    print("3")
elif num//10:
    print("2")
else:
    print("1")
