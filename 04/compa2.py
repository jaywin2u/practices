#!/usr/bin/env python

val=0
while True:
    number=int(input("Input number(00 for quit): "))
    if number > val:
        val=number
    elif number == 00:
        print(val)
        break
