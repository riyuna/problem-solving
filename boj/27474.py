n=int(input())
p1,q=map(int,input().split())
p=998244353
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

def mul_2(L1, L2):
    n=2
    while n<max(len(L1), len(L2)):n*=2
    n*=2
    L1+=[0]*(n-len(L1))
    L2+=[0]*(n-len(L2))
    fft(L1)
    fft(L2)
    res = [(i*j)%p for i,j in zip(L1, L2)]
    fft(res,inv=True)
    return res

def eqpow(L1, n):
    if n==0:return[1]
    if n==1:return L1
    res=[1]
    while n:
        LL=L1[:]
        if n&1:res=mul_2(res,L1)
        L1=mul(LL)
        n>>=1
    return res

r=(p1*pow(q,p-2,p))%p
L=[r, (1-r)%p]
nn=(n-1)//2
res=eqpow(L, nn)
a=0
for i in res:
    a+=pow(i,2,p)
    a%=p

ans=1
ans-=a
ans*=pow(2, p-2, p)
ans%=p

ans+=(a*r)
ans%=p
print(ans)