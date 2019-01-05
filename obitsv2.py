#!/usr/bin/env python
num = int(input('Input number: '))
if num > 1000:
    if num > 10000:
        print('5')
    else:
        print('4')
else:
    if num > 100:
        print('3')
    elif num > 10:
        print('2')
    else:
        print('1')
