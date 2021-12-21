from itertools import combinations
s,p=input().split()
for i in range(1,int(p)+1):
    for j in combinations(sorted(s),i):
        print(*j,sep='')