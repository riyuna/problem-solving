import sys
from random import randrange
from math import gcd
input=sys.stdin.readline

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

prime_mem = dict()
def isPrime(n):
    if n in prime_mem:return prime_mem[n]
    pList=[2, 7, 61] if n < 4759123141 else [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    if n==1:return False
    if n<4:return True
    if not n%2:return False
    res= n in pList or all(millerrabin(n, p) for p in pList)
    prime_mem[n]=res
    return res

def pollard(n):
    if n==1:return 1
    if n%2==0:return 2
    if isPrime(n):return n
    x=randrange(1,n)
    c=randrange(1,n)
    g,y=1,x
    while g==1:
        x=(x**2+c)%n
        y=(y**2+c)%n
        y=(y**2+c)%n
        g=gcd(abs(x-y),n)
    if g==n:return pollard(n)
    return g

facto_mem = dict()

def facto(n):
    if n in facto_mem:return facto_mem[n]
    if n==1:
        facto_mem[n]=[]
        return []
    if n%2==0:
        facto_mem[n]=[2]+facto(n//2)
        return facto_mem[n]
    if isPrime(n):
        facto_mem[n]=[n]
        return [n]
    k=pollard(n)
    facto_mem[n] = facto(k)+facto(n//k)
    return facto_mem[n]

def sqrt(n):
    L=facto(n)
    d=dict()
    for i in L:
        if i not in d:d[i]=1
        else:d[i]+=1
    res=1
    for i in d:
        res*=pow(i,d[i]//2)
    return res

def howmany(n):
    f_list=facto(n)
    facto_dict=dict()
    for i in f_list:
        if i in facto_dict:facto_dict[i]+=1
        else:facto_dict[i]=1
    state=True
    state_2=True
    for d in facto_dict:
        if facto_dict[d]%2:state=False
        if d%4==3 and facto_dict[d]%2:state_2=False
    
    if state:return 1
    if state_2:return 2

    while n%4==0:n//=4
    if n%8!=7:return 3
    return 4

def tonelli(p):
    #assume that solve x^2=-1(mod p)
    q=p-1
    s=0
    while q%2==0:
        q//=2
        s+=1
    z=randrange(2,p)
    while pow(z, (p-1)//2, p)==1:
        z=randrange(2,p)
    m=s
    c=pow(z,q,p)
    t=pow(p-1,q,p)
    r=pow(p-1,(q+1)//2,p)

    if t==0:return 0
    while t!=1 and t!=0:
        tt=t
        i=0
        while t%p!=1:
            t=pow(t,2,p)
            i+=1
        b=pow(c, pow(2, m-i-1, p), p)
        m=i
        c=pow(b,2,p)
        t=(tt*c)%p
        r*=b
        r%=p
    return r

def cornacchia(p):
    #to solve x^2+y^2=p
    if p%4==3:return False
    if p==2:return 1
    r=tonelli(p)
    rr=p
    while r**2>p:
        rr%=r
        if rr**2<p:return rr
        r%=rr
    return r

def get_1(n):
    return [sqrt(n)]

def get_2(n):
    mem=facto(n)
    facto_dict=dict()
    for i in mem:
        if i in facto_dict:facto_dict[i]+=1
        else:facto_dict[i]=1
    mem=facto_dict
    mul=1
    L=[]
    for d in mem:
        mul*=pow(d,mem[d]//2)
        if mem[d]%2:L.append(d)
    ans=[1,0]
    for dd in L:
        k=cornacchia(dd)
        res=[k, sqrt(dd-k**2)]
        a,b=ans
        c,d=res
        ans=[a*d+b*c, abs(a*c-b*d)]
    
    ans[0]*=mul
    ans[1]*=mul
    return ans

def get_3(n):
    f_list=facto(n)
    facto_dict=dict()
    for i in f_list:
        if i in facto_dict:facto_dict[i]+=1
        else:facto_dict[i]=1
    mul=1
    new_n=1
    for d in facto_dict:
        mul*=pow(d, facto_dict[d]//2)
        new_n*=pow(d, facto_dict[d]%2)
    t=1
    while howmany(new_n-t**2)!=2:
        t+=1
    res = get_2(new_n-t**2)+[t]
    res[0]*=mul
    res[1]*=mul
    res[2]*=mul
    return res

def get_4(n):
    ct=0
    while n%4==0:
        ct+=1
        n//=4
    res=get_3(n-1)
    pow_ct=pow(2,ct)
    res[0]*=pow_ct
    res[1]*=pow_ct
    res[2]*=pow_ct
    return res+[pow_ct]

n=int(input())
k=howmany(n)
print(k)
if k==1:
    for i in get_1(n):print(i,end=' ')
if k==2:
    for i in get_2(n):print(i,end=' ')
if k==3:
    for i in get_3(n):print(i,end=' ')
if k==4:
    for i in get_4(n):print(i,end=' ')
print()