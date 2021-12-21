n = int(input())
s = set(map(int, input().split()))
com=int(input())
for i in range(com):
    sp=input().split()
    if sp[0]=="remove":
        s.remove(int(sp[1]))
    elif sp[0]=="discard":
        s.discard(int(sp[1]))
    else:
        s.pop()
print(sum(list(s)))