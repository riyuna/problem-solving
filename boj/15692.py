import time
n,d,r=map(int,input().split())
start=time.time()
dp = [[-1]*501 for i in range(501)]
#주어진 r명에 대해, i명이 있고 j일이 지났을 때 r명 합 기댓값이 dp[i][j]
mem = dict()
cb=[[0]*1000 for i in range(1000)]
for i in range(1000):
	for j in range(i+1):
		if i==j or j==0:cb[i][j]=1
		else:cb[i][j]=cb[i-1][j]+cb[i-1][j-1]
def comb(n, k):
	return cb[n][k]

for i in range(len(dp)):
	dp[i][0] = min(i, r)
	for j in range(1,r+1):
		dp[j][i] = j+i

def solve(n, d):
	if n==0:return 0
	if dp[n][d]!=-1:return dp[n][d]
	count=0
	a = comb(n+d-1, d)
	for k in range(n+1):
		if d-n+k>=0:
			count += comb(n, k)*comb(d-1,d-n+k)*solve(n-k, d-n+k)
	count=count/a+r
	dp[n][d]=count
	return count

# for i in range(r+1, n+1):
# 	for j in range(1,d+1):
# 		count=0
# 		a = comb(i+j-1,j)
# 		for k in range(i+1):
# 			if j-i+k>=0:count += comb(i,k) * dp[i-k][j-i+k] * comb(j-1, j-i+k)
# 		dp[i][j]=count/a
# 		dp[i][j]+=r

print(solve(n,d))
print(f"{time.time()-start:.4f} sec")