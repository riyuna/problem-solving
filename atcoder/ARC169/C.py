import sys
input = sys.stdin.readline
def linput():return list(map(int,input().split()))
n=int(input())
L=linput()
mod=998244353
ct=0
r1=0
r2=0
k=-1
def check(L):
	for i in range(len(L)):
		if L[i]>0 and i+L[i]<len(L):
			check=True
			for j in range(i+1, i+L[i]+1):
				if L[j]!=L[i]:
					check=False
					break
			if check:return True
	return False
if check(L):print(0)
else:
	p=0
	for i in L:
		if i==-1:p+=1
	for i in range(n):
		if L[i]==-1:
			r1+=1
			r2+=1
		elif k==L[i]:
			r1=0
			r2+=1
		else:
			k=L[i]
			r1=0
			r2=r1+1
		if r1>1:
			for j in range(1,r1):
				end=(L[i-j-1]==-1)
				
		if r1<k and r2>k:ct+=1
		print(ct, r1, r2, k)

	print((pow(n, p, mod)-ct)%mod)