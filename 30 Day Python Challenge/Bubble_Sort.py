#!/bin/python3

import sys
#number of items in list
n = int(input().strip())
#input for the list to sort
alist = list(map(int, input().strip().split(' ')))
# setting counter for number of swaps
swap = 0
for j in range(len(alist)-1,0,-1):
    for i in range(j):
        #loop to do the actual sorting
        if alist[i]>alist[i+1]:
            temp = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = temp
            #increment for each swap
            swap += 1


#calling function to sort the list
#bubbleSort(alist)

#validating my list sorted correctly
print(alist)

#printing the number of swaps
print("Array is sorted in", swap, "swaps")
#printing first element in list
print("First Element: ", alist[0])
#printing second element in list
print("Last Element: ", alist[-1])