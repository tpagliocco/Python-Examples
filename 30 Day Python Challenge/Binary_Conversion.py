#!/bin/python3
#Given a base-10integer, N , convert it to binary (base-2). Then find and print the base-10 integer 
#denoting the maximum number of consecutive 1's in N's binary representation.

import sys

n = int(input().strip())

count= 0
maxcount = 0

for i in str(bin(n)):
    if i == '1':
        count +=1
    elif count > maxcount:
        maxcount = count;
        count = 0
    else:
        count = 0

if count > maxcount: 
    maxcount = count        

print(maxcount)
