#!/usr/bin/env python
#
val=int(input('>>> '))
if val >= 1000:
    if val >= 10000:
        print("5")
        n=5
    else:
        print("4")
        n=4
else:
    if val >= 100:
        print("3")
        n=3
    elif val >= 10:
        print("2")
        n=2
    else:
        print("1")
        n=1

for i in range(n):
    ret=val%10
    print(ret)
    val=val//10
   
    
