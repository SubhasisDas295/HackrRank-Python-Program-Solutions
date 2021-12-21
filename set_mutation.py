n1=int(input())
s1=set(map(int,input().split()))
p=int(input())
for i in range(p):
    ip=input().split()
    if ip[0]=="intersection_update":
        t1=set(map(int,input().split()))
        s1.intersection_update(t1)
    elif ip[0]=="update":
        t1=set(map(int,input().split()))
        s1.update(t1)
    elif ip[0]=="symmetric_difference_update":
        t1=set(map(int,input().split()))
        s1.symmetric_difference_update(t1)
    elif ip[0]=="difference_update":
        t1=set(map(int,input().split()))
        s1.difference_update(t1)
print(sum(s1))