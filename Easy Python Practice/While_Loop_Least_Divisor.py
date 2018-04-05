#Given an integer not less than 2. Print its smallest integer divisor greater than 1.

# Read an integer:
a = int(input())

#Error checking for if less than 2
if a < 2:
    print("Error")

#Set variable for division to check if legit
x = 2

#While loop to see what is first divisible number
while a % x != 0:
    x += 1

#Print x once true
print(x)





