from collections import deque
n,s=map(int,input().split())
dp=[[0]*1001 for i in range(60)]
dp[2][0]=1
q=deque([])
q.append((2, 0))
flag=False
while len(q):
	a,b=q.popleft()
	for i in range(a+1, 60):
		newa=i
		newb=b+((i-a)*(i-a+1)//2)
		if newb>1000:break
		if dp[newa][newb]:continue
		dp[newa][newb]=1
		if newa==n and newb==s:
			flag=True
			break
		q.append((newa, newb))
	if flag:break
print(int(flag))