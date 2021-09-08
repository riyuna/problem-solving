import sys
from random import *
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

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

def solve(n):
    if n==4:return 1
    L=[]
    while n-1:
        d=pollard(n)
        n//=d
        if d in L:return -1
        L.append(d)
    res=1
    for i in range(1,len(L)+1):res*=i
    return res

for i in ' '*int(input()):
    print(solve(int(input())))