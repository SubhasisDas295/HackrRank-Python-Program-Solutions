N=int(input())
arr=list(map(int,input().split()))
print([False,any(map(lambda x:str(x)==str(x)[::-1],arr))][all(map(lambda x:x>0,arr))])