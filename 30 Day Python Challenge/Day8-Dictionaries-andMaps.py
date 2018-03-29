#Task
#Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to # query your phone book for. For each  queried, print the
# associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for
# is not found, print Not found instead.

#Note: Your phone book should be a Dictionary/Map/HashMap data structure.

#Input Format
#The first line contains an integer, , denoting the number of entries in the phone book.
#Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line.
#The first value is a friend's name, and the second value is an -digit phone number.

#After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query)
#contains a  to look up, and you must continue reading lines until there is no more input.

#Note: Names consist of lowercase English alphabetic letters and are first names only.

#get input
n = int(input())
#set dictionary
w = { }
#loop for # of inputs and get dictionary inputs
for i in range(n):
  line = input()
  k, v = line.split()
  w[k] = v
#sample print of dictionary
#print(w)
while True:
    try:
        number = input()
    except EOFError:
        break
    if number in w:
        print("{}={}".format(number, w[number]))
    else:
        print("Not found")

