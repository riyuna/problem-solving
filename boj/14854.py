import sys
input=sys.stdin.readline

dp=[[-1]*2010 for i in range(2010)]
def c(x,y,m):
	if x<y:
		dp[x][y]=0
		return 0
	if y==0 or y==x:
		dp[x][y]=1
		return 1
	if dp[x][y]!=-1:return dp[x][y]
	k=(c(x-1,y-1,m)+c(x-1,y,m))%m
	dp[x][y]=k
	return k

def solve_27(n,m):
	r=n-m
	orign, origm, origr = n,m,r
	nL=[]
	mL=[]
	rL=[]
	NL=[]
	ML=[]
	RL=[]
	ct=0
	while n or m or r or ct<3:
		NL.append(n)
		ML.append(m)
		RL.append(r)
		nL.append(n%3)
		mL.append(m%3)
		rL.append(r%3)
		n//=3
		m//=3
		r//=3
		ct+=1
	eL=[]
	for i in range(len(mL)):
		if mL[i]+rL[i]>2:eL.append(1)
		else:eL.append(0)
	
	print(nL)
	print(mL)
	print(rL)
	print()
	print(NL)
	print(ML)
	print(RL)
	print()
	print(eL)

print(solve_27(16, 5))