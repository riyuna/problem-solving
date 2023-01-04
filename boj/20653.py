import sys
input = sys.stdin.readline

mod = 10**9+7

pList = []
check = [True]*30001
check[0]=False
check[1]=True
for i in range(2, 30001):
	if not check[i]:continue
	pList.append(i)
	for j in range(i*2, 30001, i):
		check[j]=False

def fct(n):
	d=dict()
	for i in pList:
		if n%i==0:
			if i not in d:d[i]=0
			while n%i==0:
				d[i]+=1
				n//=i
	if n!=1:d[n]=1
	return d


for i in ' '*int(input()):
	n,g,l=map(int,input().split())
	if l%g != 0:
		print(0)
		continue
	k = l//g
	d=fct(k)
	res = 1
	for j in d:
		p = d[j]
		res *= pow(p+1, n, mod) - 2*pow(p, n, mod) + pow(p-1, n, mod)
		res	%=mod
	print(res)