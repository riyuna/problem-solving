n=int(input())
L=list(map(int,input().split()))

def solve(L):
    if len(L)==1:return True
    L.sort()
    m=L[0]
    L1=[m]
    L2=[m]
    d1=L[1]-L[0]
    if d1==0:return False
    mem=m
    mem2=m
    d2=0
    for i in range(1, len(L)):
        if mem+d1==L[i]:
            mem+=d1
        elif mem2==m or mem2+d2==L[i]:
            if mem2==m:
                mem2=L[i]
                d2=L[i]-m
            else:
                mem2+=d2
        else:return False
    return True

print('Yes' if solve(L) else 'No')