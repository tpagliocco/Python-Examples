#input - integer N
#output - single integer notating N!
#Example , if N = 5 , 5 x 4 x 3 x 2 x 1

#!/bin/python3

import sys


def factorial(n):
    # Complete this function
    a = []
# first loop is to create a list of the integers
    for i in range(1, n + 1):
        a.append(i)
# second loop is to create the product of list elements
    theSum = 0
    for i in a:
        theSum = theSum * i

    return theSum


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
