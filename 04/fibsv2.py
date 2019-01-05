#!/usr/bin/env python
#
fron=1
last=2
num=3

while num <= 101:
    tmp=last
    last=fron+last
    fron=tmp
    num+=1
print(last)
