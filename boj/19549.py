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

def solve(m, n):
    res=0
    a=set()
    b=set()
    for i in range(1, int(n**0.5)+1):
        a.add(i)
        a.add(n//i)
    for i in range(1, int(m**0./5)+1):
        b.add(i)
        b.add(m//i)
    L=list(a)
    L.sort()
    M=list(b)
    M.sort()
    #L: n//d의 값으로 가능한 것들 저장
    #M: m//d의 값으로 가능한 것들 저장
    