import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
#print('なんでや!阪神関係ないやろ!')

n,k=linput()
L=linput()
dp=[[10**10]*(2*n-k+1)for i in range(2)]
check=[0]*(n+1)
for i in L:check[i]=1
kutsu=[]
for i in range(1, n+1):
	if check[i]:kutsu.append(i)
	else:
		kutsu.append(i)
		kutsu.append(i)

dp[0][0]=0
dp[1][1]=0
for i in range(2, len(dp[0])):
	dp[0][i]=dp[0][i-2]+abs(kutsu[i-2]-kutsu[i-1])

for i in range(3, len(dp[1])):
	dp[1][i]=min(dp[1][i-2]+abs(kutsu[i-2]-kutsu[i-1]), dp[0][i-1])

if k%2:print(dp[1][-1])
else:print(dp[0][-1])