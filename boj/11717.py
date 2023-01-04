import sys
input = sys.stdin.readline
h,w=map(int,input().split())
L=[]
for i in ' '*h:L.append(input().rstrip())

dp = [[[[-1]*21 for i in range(21)] for i in range(21)]for i in range(21)]

def grundy_number(x1, y1, x2, y2):
	if x1<0 or y1<0 or x2>=w or y2>=h:return 0
	if x1>x2 or y1>y2:return 0
	if dp[x1][y1][x2][y2]!=-1:return dp[x1][y1][x2][y2]
	d=dict()
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			if L[j][i]=='X':continue
			res = grundy_number(x1, y1, i-1, j-1)
			res ^= grundy_number(x1, j+1, i-1, y2)
			res ^= grundy_number(i+1, y1, x2, j-1)
			res ^= grundy_number(i+1, j+1, x2, y2)
			d[res]=True
	n=0
	while n in d:n+=1
	dp[x1][y1][x2][y2]=n
	return n

res = grundy_number(0, 0, w-1, h-1)
print("First" if res else "Second")