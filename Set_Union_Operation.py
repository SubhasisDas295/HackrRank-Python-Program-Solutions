# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set(input().split(" "))
b=int(input())
s2=set(input().split(" "))
print(len(s1|s2))