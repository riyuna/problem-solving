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
pisum2=[0]
pisum3=[0]

for i in range(1,10**6+1):
    pisum.append((pisum[-1]+pi[i])%mod)
    pisum2.append((pisum2[-1]+pi[i]*i)%mod)
    pisum3.append((pisum3[-1]+pi[i]*i*i)%mod)
     
val1=dict()
val2=dict()
val3=dict()

def getval1(n):
    if n<=10**6:return pisum[n]
    if n in val1:return val1[n]
    ret=0
    i=2
    while i<=n:
        la=n//(n//i)
        ret+=(la-i+1)*getval1(n//i)
        ret%=mod
        i+=(la+1)
    ret=(n*(n+1)//2-ret)%mod
    val1[n]=ret
    return ret

def getval2(n):
    if n<=10**6:return pisum2[n]
    if n in val2:return val2[n]
    ret=0
    i=2
    while i<=n:
        la=n//(n//i)
        ret+=(la*(la+1)//2-(i+1)*(i+2)//2)*getval2(n//i)
        ret%=mod
        i+=(la+1)
    ret=(n*(n+1)*(2*n+1)//6-ret)%mod
    val2[n]=ret
    return ret

def getval3(n):
    if n<=10**6:return pisum3[n]
    if n in val3:return val3[n]
    ret=0
    i=2
    while i<=n:
        la=n//(n//i)
        ret+=(la*(la+1)*(2*la+1)//6-(i+1)*(i+2)*(2*i+3)//6)*getval3(n//i)
        ret%=mod
        i+=(la+1)
    ret=((n*(n+1)//2)**2-ret)%mod
    val3[n]=ret
    return ret

print(getval1(10**9))
print(getval2(10**9))
print(getval3(10**9))