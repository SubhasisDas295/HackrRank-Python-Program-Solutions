s1=set(input().split())
n=int(input())
output=True
for i in range(n):
    s2=set(input().split())
    if not s2.issubset(s1):
        output=False
    if len(s2)>=len(s1):
        output=False
print(output)