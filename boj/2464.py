def next(L):
    L=L[:]
    n=len(L)
    breaked=False
    for i in reversed(range(n-1)):
        if L[i]<L[i+1]:
            breaked=True
            break
    if not breaked:return ['0']

    j=n-1
    while not L[j]>L[i]:
        j-=1
    L[i],L[j]=L[j],L[i]
    L[i+1:]=reversed(L[i+1:])
    return L

def prev(L):
    L=L[:]
    n=len(L)
    breaked=False
    for i in reversed(range(n-1)):
        if L[i]>L[i+1]:
            breaked=True
            break
    if not breaked:return ['0']

    j=n-1
    while not L[j]<L[i]:
        j-=1
    L[i],L[j]=L[j],L[i]
    L[i+1:]=reversed(L[i+1:])
    return L

n=int(input())
b=['0']+list(bin(n))[2:]
nxb=''.join(next(b))
prb=''.join(prev(b))
print(int(prb,2),int(nxb,2))