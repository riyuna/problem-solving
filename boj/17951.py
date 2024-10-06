n,k=map(int,input().split())
L=list(map(int,input().split()))

def check(L, k, score):
    ct=0
    s=0
    for i in L:
        s+=i
        if s>=score:
            ct+=1
            s=0
    return ct>=k

lo=0
hi=10**10
while lo<=hi:
    mid=(lo+hi)//2
    if check(L, k, mid):
        lo=mid+1
    else:
        hi=mid-1

print(hi)