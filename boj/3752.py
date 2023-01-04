import sys
input=sys.stdin.readline
pL=[]
L=[True]*100001
L[0]=False
L[1]=False
for i in range(2, 100001):
	if not L[i]:continue
	pL.append(i)
	for j in range(i*i, 100001, i):
		L[j]=False

def fact(n):
	res=[]
	for i in pL:
		if n%i==0:
			res.append(i)
		while n%i==0:n//=i
	if n==1:return res
	else: res.append(n)
	return res

def phi(n):
	res=n
	for p in fact(n):
		res*=p-1
		res//=p
	return res

for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	res=1
	for i in L:
		res*=phi(i)
		res%=1000000007
	print(res)