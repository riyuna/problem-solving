import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))
dL=list(range(n))
def f(L):
	ctL=[0]*20
	for i in L:
		for j in range(20):
			k=pow(2,j)
			if i&k:ctL[j]+=1
	return ctL
permL=[0]
for i in L:permL.append(permL[-1]^i)
L1=f(dL)
L2=f(permL)
start=0
for i in range(20):
	if L1[i]!=L2[i]:start+=pow(2,i)
for i in range(len(permL)):
	permL[i]^=start
for i in permL:print(i,end=' ')