from math import gcd
import sys
from random import randrange
input=sys.stdin.readline
sys.setrecursionlimit(10000)

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
    pList=[2, 7, 61] if n < 4759123141 else [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
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

def primary_root(p):
	n=p-1
	factor=dict()
	while n>1:
		k=pollard(n)
		if k not in factor:factor[k]=True
		n//=k
	while True:
		k=randrange(2, p)
		state=True
		for d in factor:
			if pow(k,(p-1)//d,p)==1:
				state=False
				break
		if state:return k

def log(a,b,m):
	sqrt=int(m**0.5)+1
	d=dict()
	res=[]
	for i in range(1, sqrt+1):
		d[pow(a,i*sqrt,m)]=i
	
	for j in range(sqrt+1):
		k=pow(a,j,m)*b
		k%=m
		if k in d:return d[k]*sqrt-j

	return -1

def solve(m,p,a):
	if p<100:
		for i in range(1, p*(p-1)+1):
			if (pow(i,i,p)+pow(i,m,p))%p==a:return i
	k=primary_root(p)
	while pow(k,m,p)==a:
		t=2
		while gcd(p-1,t)>1:
			t+=1
		k=pow(k,t,p)
	y=log(k, (a-pow(k,m,p))%p, p)
	return ((y-k)*p+k)%(p*(p-1))

for i in ' '*int(input()):
	p,a,m=map(int,input().split())
	print('TAK', solve(m,p,a))