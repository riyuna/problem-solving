from math import log
from decimal import Decimal

n,k=map(int,input().split())

mem = [0]

for i in range(1, 100001):
	mem.append(Decimal(mem[-1]+Decimal(1/i)))

def f(n):
	if n<=100000:
		return mem[n]
	return Decimal(log(n))+1/Decimal(2*n)+Decimal(0.5772156649015328606065120)

def taylor(n,k):
	added = Decimal(k/n)
	res=0
	ct=1
	while added*n*n>=1:
		res += Decimal(added/ct)
		ct+=1
		added *= Decimal(k/n)
	return res

def solve(n,k):
	newk=n-k
	if k==1:return 1
	if n<=100000:
		return n*(f(n)-f(newk))
	if newk<=100000:return n*Decimal(log(n))+Decimal(1/2)+n*Decimal(0.5772156649015328606065120) - n*f(newk)
	if n>10*k: return n*Decimal(taylor(n,k)) + Decimal(1/2) - Decimal(n/(2*n-2*k))
	return n*Decimal(log(Decimal(n/(n-k)))) + Decimal(1/2) - Decimal(n/(2*n-2*k))

print(solve(n,k))