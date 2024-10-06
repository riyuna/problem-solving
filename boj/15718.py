import sys
sys.setrecursionlimit(30000)
dp=[[-1]*2500 for i in range(2500)]
def c97(x,y):
	m=97
	if x<y:
		dp[x][y]=0
		return 0
	if y==0 or y==x:
		dp[x][y]=1
		return 1
	if dp[x][y]!=-1:return dp[x][y]
	k=(c97(x-1,y-1)+c97(x-1,y))%m
	dp[x][y]=k
	return k
dp2=[[-1]*2500 for i in range(2500)]
def c1031(x,y):
	m=1031
	if x<y:
		dp2[x][y]=0
		return 0
	if y==0 or y==x:
		dp2[x][y]=1
		return 1
	if dp2[x][y]!=-1:return dp2[x][y]
	k=(c1031(x-1,y-1)+c1031(x-1,y))%m
	dp2[x][y]=k
	return k
for i in ' '*int(input()):
	n,k=map(int,input().split())
	if n==0 and k==1:
		print(1)
		continue
	if n==0:
		print(0)
		continue
	if k==1:
		print(0)
		continue
	n-=1
	k-=2
	if n<k:
		print(0)
		continue
	nmem=n
	kmem=k
	m1=97
	m2=1031
	count1=1
	count2=1
	while n or k:
		count1*=c97(n%m1, k%m1)
		count1%=m1
		n//=m1
		k//=m1
	n=nmem
	k=kmem
	while n or k:
		count2*=c1031(n%m2, k%m2)
		count2%=m2
		n//=m2
		k//=m2
	ct=count2
	for j in range(97):
		if (j*1031+ct)%97==count1:
			print(j*1031+ct)
			break