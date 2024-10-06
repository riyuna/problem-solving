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

L=[True]*(100001)
L[0]=False
L[1]=False
pL=[]
for i in range(2, 100001):
	if not L[i]:continue
	pL.append(i)
	for j in range(i*i, 100001, i):
		L[j]=False
	

def facto(n):
	res=set()
	for i in pL:
		if n%i:continue
		res.add(i)
		while n%i==0:
			n//=i
	while n>1:
		k=pollard(n)
		res.add(k)
		while n%k==0:n//=k
	return res
	

n=int(input())
L=list(map(int,input().split()))
factL=[]
pmem=dict()
grundy = 0 
for i in L:
	s=facto(i)
	smem=dict()
	for j in s:
		if j not in pmem:
			pmem[j]=1
		else: pmem[j]+=1
		smem[j]=True
	for p in pmem:
		if p not in smem and pmem[p]:
			grundy^=pmem[p]
			pmem[p]=0
for p in pmem:
	if pmem[p]:grundy^=pmem[p]
print("First" if grundy else "Second")