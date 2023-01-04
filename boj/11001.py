n,d=map(int,input().split())
T=list(map(int,input().split()))
V=list(map(int,input().split()))
dp = [0]*n
def C(i,j):
	return (j-i)*T[j] + V[i]

def solve(start, end, l, r):
	if start>end:
		return
	m = (start+end)//2
	optimal=m
	dp[m] = V[m]
	for i in range(l, min(r, m+d)+1):
		res = C(m, i)
		if res>dp[m]:
			dp[m]=res
			optimal = i
	
	solve(start, m-1, l, optimal)
	solve(m+1, end, optimal, r)

solve(0, n-1, 0, n-1)
print(max(dp))