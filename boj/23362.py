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

div_mem = dict()

def div(n):
	if n in div_mem:return div_mem[n]
	ft = facto(n)
	d = dict()
	for i in ft:
		if i not in d:d[i]=0
		d[i]+=1
	L = [1]
	for i in d:
		memL=L[:]
		for j in range(d[i]):
			for k in memL:
				L.append(k*pow(i, j+1))
	L.sort()
	div_mem[n]=L
	return L

def pi(n):
	L=set(facto(n))
	for d in L:
		n//=d
		n*=(d-1)
	return n

def solve(n):
	res=0
	for d in div(n):
		res+=pi(d+1)
	return res

for i in ' '*int(input()):
	input()
	print(solve(int(input())))