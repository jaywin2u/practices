#!/usr/bin/env python
#
fron=1
last=2

print(fron)
while last <= 100:
    print(last)
    tmp=last
    last=fron+last
    fron=tmp
