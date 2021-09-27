from random import randrange

n=int(input())
mod=10**9+7

def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

def millerrabin(n,a):
    r=0
    d=n-1
    while not d%2:
        r+=1
        d//=2
    x=pow(a,d,n)
    if x==1 or x==n-1:return True
    for i in ' '*(r-1):
        x=pow(x,2,n)
        if x==n-1:return True
    return False

def isPrime(n):
    pList=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    if n==1:return False
    if n<4:return True
    if not n%2:return False
    for p in pList:
        if p==n:return True
        if not millerrabin(n,p):return False
    return True
def pollard(n):
    if isPrime(n):return n
    if n==1:return 1
    if not n%2:return 2
    k=randrange(2,n)
    x=k
    r=randrange(1,n)
    d=1
    while d==1:
        k=(pow(k,2,n)+r)%n
        x=(pow(pow(x,2,n)+r,2,n)+r)%n
        d=gcd(abs(k-x),n)
        if d==n:return pollard(n)
    if isPrime(d):return d
    else:return pollard(d)

memdict=dict()

def pi(n):
    if n in memdict:return memdict[n]
    if n==1:
        memdict[n]=1
        return 1
    d=pollard(n)
    if n%(d**2)==0:res=d*pi(n//d)
    else: res=pi(n//d)*(d-1)
    memdict[n]=res
    return res

fdict=dict()

def f(x):
    if x in fdict:return fdict[x]
    res=0
    for i in range(2, x+1):
        res+=(i*i*pi(i))//2
        res%=mod
    fdict[x]=res
    return res

result = 0

for i in range(1, n+1):
    result+=f(n//i)*i
    result%=mod
print(result)