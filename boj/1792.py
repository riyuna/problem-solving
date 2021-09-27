import sys
from math import gcd
from random import randrange
input = sys.stdin.readline

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

mo=[None]*50001
psum=[0]*50001

def mobi(n):
    if n==1:
        mo[n]=1
        return 1
    d=pollard(n)
    if (n//d)%d==0:
        mo[n]=0
        return 0
    res=mo[n//d]*-1
    mo[n]=res
    return res

for i in range(1, 50001):
    psum[i]+=psum[i-1]+mobi(i)

n=int(input())
def solve(a,b,d):
    res=0
    aa=a//d
    bb=b//d
    m=min(aa,bb)
    i=1
    while i<=m:
        dista=(aa%i)//(aa//i)
        distb=(bb%i)//(bb//i)
        dist=min(dista,distb)
        res+=(psum[i+dist]-psum[i-1])*(aa//i)*(bb//i)
        i+=(dist+1)
    return res

for i in ' '*n:
    a,b,d=map(int,input().split())
    print(solve(a,b,d))