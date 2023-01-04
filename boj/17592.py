import sys
input=sys.stdin.readline
n=int(input())
graph=[]
for i in ' '*n:graph.append(list(map(int,input().split())))

dp=[[-1]*(n+1) for i in range(n)]

def solve(a, k):
	global n
	a%=n
	if dp[a][k]!=-1:return dp[a][k]
	if k<0:return 0
	if k==0 or k==1:
		dp[a][k]=0
		return 0
	flag=graph[a][(a+k-1)%n]
	res=0
	if flag:res=solve(a+1, k-2)+flag
	res=max(res,solve(a,k-1))
	res=max(res,solve(a+1,k-1))
	dp[a][k]=res
	return res

for i in range(n):
	for j in range(n+1):
		solve(i,j)
res=0
for l in dp:
	print(l)
	res=max(res,max(l))
print(res)