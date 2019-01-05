#!/usr/bin/env python
#
n=int(input(">>> "))
for i in range(1,n+1):
    if i <= (n//2+1):
        ret=(n-2*i+1)//2 # (n-(i+(i-1)))/2
    else:
        ret=(2*i-1-n)//2  # (n-(n+1-i)-(n+1-i-1))//2

    print(" "*ret + "*"*(n-2*ret) + " "*ret)


