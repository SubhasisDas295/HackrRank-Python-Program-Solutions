n=int(input())
for i in range(n):
    n1=int(input())
    s1=set(input().split())
    n2=int(input())
    s2=set(input().split())
    if s1.issubset(s2):
        print(True)
    else:
        print(False)