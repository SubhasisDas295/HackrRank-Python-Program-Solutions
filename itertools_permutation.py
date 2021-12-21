from itertools import permutations
s,p=input().split()
d=sorted(list(permutations(s,int(p))))
for i in d:
    print(*i,sep='')