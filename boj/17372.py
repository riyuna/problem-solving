mod=10**9+7
pi=list(range(10**6+1))
prime=[True]*(10**6+1)
prime[0]=False
prime[1]=False
for i in range(2, 10**6+1):
    if prime[i]==True:
        pi[i]=i-1
        for j in range(i*2,10**6+1,i):
            prime[j]=False
            pi[j]//=i
            pi[j]*=(i-1)
pisum=[0]

for i in range(1,10**6+1):
    pisum.append((pisum[-1]+pi[i])%mod)
    
val1=dict()

def getval1(n):
    if n<=10**6:return pisum[n]
    if n in val1:return val1[n]
    ret=0
    i=2
    while i<=n:
        la=n//(n//i)
        ret+=(la-i+1)*getval1(n//i)
        ret%=mod
        i+=(la-i+1)
    ret=(n*(n+1)//2-ret)%mod
    val1[n]=ret
    return ret

def mul(a, b):
    x1 = (a[0]*b[0] + a[1]*b[2]) % mod
    x2 = (a[0]*b[1] + a[1]*b[3]) % mod
    x3 = (a[2]*b[0] + a[3]*b[2]) % mod
    x4 = (a[2]*b[1] + a[3]*b[3]) % mod
    return x1,x2,x3,x4

def fib(n):
    a, b = (1,0,0,1), (1,1,1,0)
    while n > 0:
        if n & 1:
            a = mul(a, b)
        b = mul(b, b)
        n >>= 1
    return a[2]

def solve(n):
    res=0
    a=set()
    for i in range(1, int(n**0.5)+1):
        a.add(i)
        a.add(n//i)
    L=list(a)
    L.sort()
    for i in range(len(L)):
        left=n//(L[i]+1)
        right=n//(L[i])
        f=fib(right+2)-fib(left+2)
        f%=mod
        g=2*getval1(L[i])-1
        g%=mod
        res+=(f*g)%mod
        res%=mod
    return res

print(solve(int(input())))