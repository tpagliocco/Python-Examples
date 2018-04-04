from itertools import combinations

#You are given a string X 
#Your task is to print all possible combinations, up to size N, of the string in lexicographic sorted order.

x = input().split()
y = list(x[0])
z = int(x[1])

#f = sorted(sorted(list(combinations(y, 1))))
combos = [ ]

for i in range(1, len(y)-1):
    #print(sorted(sorted(list(combinations(y, 1)))))
    #combos.append(y[i])
    combos.extend(sorted(sorted(list(combinations(y, i)))))

print (' '.join(map(str, combos)))
#for i in range(len(combos)):
#    print(list(combos[i]), sep='\n')
    


