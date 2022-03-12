import sys
input=sys.stdin.readline
n,m=map(int,input().split())
adj=[dict() for i in range(n)]
for i in ' '*m:
	a,b,c=input().split()
	a=int(a)
	b=int(b)
	if c not in adj[a-1]:adj[a-1][c]=[]
	if c not in adj[b-1]:adj[b-1][c]=[]
	adj[a-1][c].append(b-1)
	adj[b-1][c].append(a-1)

s=input()
dp=[0]*n
dp[0]=100

for i in s:
	newdp=[0]*n
	for j in range(n-1):
		if i in adj[j]:
			num=len(adj[j][i])
			for k in adj[j][i]:
				newdp[k]+=dp[j]/num
		else:newdp[j]+=dp[j]
	newdp[-1]+=dp[-1]
	dp=newdp

print(dp[-1])