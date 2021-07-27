# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
lst=Counter(map(int,input().split(" ")))
N=int(input())
Total=0
for i in range(N):
    size,x_i=map(int,input().split())
    if size in lst and lst[size]>0:
        lst[size]-=1
        Total+=x_i
print(Total)
