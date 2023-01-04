import sys
input=sys.stdin.readline

def check(L, k):
	dp=[[0]*len(L[0]) for i in range(len(L))]
	mem=0
	for i in range(len(L)):
		for j in range(len(L[0])):
			if L[i][j]>=k:
				dp[i][j]=1
				if i>0 and j>0:
					dp[i][j]=min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]])+1
				mem=max(mem, dp[i][j])
				if mem>=k:return True
	return False

for i in ' '*int(input()):
	n,m=map(int,input().split())
	L=[]
	for _ in ' '*n:L.append(list(map(int,input().split())))
	lo=1
	hi=10**6
	while lo<hi:
		mid=(lo+hi)//2+1
		if check(L, mid):
			lo=mid
		else:hi=mid-1
	print(hi)