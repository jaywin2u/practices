#!/usr/bin/env python
#
for i in range(1,10):
    for j in range(1,i+1):
        sum=j*i
        print(str(j) + "*" + str(i) + "=" + str(sum) + "\t",end="")
    print("")
        
