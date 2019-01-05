#!/usr/bin/env python
#
ret=0
for i in range(1,6):
    sum=1
    while i:
      if i == 1:
         i-=1
      else:
         tmp=i*(i-1)
         sum*=tmp
         i-=2
    ret+=sum

print(ret)
