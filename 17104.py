import sys
input = sys.stdin.readline
p=469762049
def fft(L, inv=False):
    j=0
    n=len(L)
    for i in range(1, n):
        bit = n>>1
        while j>=bit:
            j-=bit
            bit>>=1
        j+=bit
        if i<j:L[i],L[j]=L[j],L[i]
    m=2
    while m<=n:
        u = pow(3, p//m, p)
        if inv: u=pow(u, p-2, p)
        for i in range(0, n ,m):
            w=1
            for k in range(i, i+m//2):
                tmp=L[k+m//2]*w
                L[k+m//2] = (L[k]-tmp)%p
                L[k] += tmp
                L[k]%=p
                w*=u
                w%=p
        m*=2
    if inv:
        inv_n = p-(p-1)//n
        for i in range(n):
            L[i]=(L[i]*inv_n)%p

def mul(L1):
    n=2
    while n<len(L1):n*=2
    n*=2
    L1+=[0]*(n-len(L1))
    fft(L1)
    res = [(i*i)%p for i in L1]
    fft(res,inv=True)
    return res

pList=[1]*(10**6+1)
pList[0]=0
pList[1]=0
pList2=[0]*(10**5*5+1)
for i in range(2, 10**6+1):
    if not pList[i]:continue
    for j in range(i*2, 10**6+1, i):pList[j]=0
    pList2[i//2]=1
res=mul(pList2)
res[1]=1
for _ in ' '*int(input()):
    print((res[int(input())//2-1]+1)//2)