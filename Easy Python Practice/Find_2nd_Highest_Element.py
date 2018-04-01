#Take a integer N and then N inputs 
#Find the second highest integer in the list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = [ ]
    for i in arr:
      l.append(i)
    
    #print(l)
    l.sort()
    #print(l)
    #print(l.count(max(l)))
    y = len(l)
    for i in l:
        while l[-1] == l[-2]:
            #print(l[-1])
            #print(l[-2])
        #if l[y-1] == l[y-2]:
            l.pop()
            #print(l)

    print(l[-2])

    
    #Other Answers
    #nums = [1, 2, 2]
    #print sorted(list(set(nums)))[-2]
    
    
