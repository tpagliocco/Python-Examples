# For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X.
# Print the exponent value and the result of the expression 2ⁿ.

x = int(input())
n = 0
myList = []
while x >= 2 ** n:
    myList.append(n)
    n += 1

while len(myList) != 1:
    myList.pop(0)

n = n - 1
print(myList[0], 2 ** n)

# Teacher Answer
# x = int(input())
# n = 1
# while 2 ** n <= x:
#  n += 1
# print(n - 1, 2 ** (n - 1))