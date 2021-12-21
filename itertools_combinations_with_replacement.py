from itertools import combinations_with_replacement
S,k=input().split()
l=list(combinations_with_replacement(sorted(S),int(k)))
for i in l:
    print(*i,sep="")