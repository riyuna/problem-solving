import sys
input = sys.stdin.readline
def linput():return list(map(int,input().split()))
n,s=linput()
L=linput()
M=[None]*n
pt=0
k=L[0]
for i in range(n-1):
	M[i]=pt
	k+=L[i+1]
	while k>s:
		k-=L[pt]
		pt+=1
M[n-1]=pt
dp=[0]*n
for i in range(n):
	dp[i] = (0 if M[i]==0 else dp[M[i]-1])+(i+1)
print(sum(dp))