# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Constraints
#
# Output Format
#
# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = [ ]
    for i in arr:
        l.append(i)

    # print(l)
    mySet = set(l)
    # print(mySet)
    myList = list(mySet)
    print(myList)
    print(myList.index(max(myList)))




