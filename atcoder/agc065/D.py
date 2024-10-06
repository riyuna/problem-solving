import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=10**9+7

dp=[[0]*10 for i in range(10)]
for i in range(10):
	for j in range(i):
		if j==0:
			dp[i][j]=1
			continue
		dp[i][j]+=dp[i-1][j]
		for k in range(1, i):
			