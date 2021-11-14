import sys
sys.setrecursionlimit(100000)
n=int(input())
L=list(map(int,input().split()))
ans=0
def merge(L1, L2):
    # print(L1, L2)
    global ans
    i1=0
    i2=0
    cnt=0
    L=[]
    while i1<len(L1) or i2<len(L2):
        if i1==len(L1):
            L.append(L2[i2])
            i2+=1
            cnt+=1
            continue
        if i2==len(L2):
            L.append(L1[i1])
            i1+=1
            ans+=cnt
            continue
        if L1[i1]<=L2[i2]:
            L.append(L1[i1])
            i1+=1
            ans+=cnt
        else:
            L.append(L2[i2])
            i2+=1
            cnt+=1
    return L
def mgsort(L):
    # print(f'L: {L}')
    if len(L)==1:return L
    ln=len(L)
    L1=mgsort(L[:ln//2])
    L2=mgsort(L[ln//2:])
    L=merge(L1, L2)
    return L
mgsort(L)
print(ans)