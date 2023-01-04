n,k=map(int,input().split())

res1=0
res2=0
visited = dict()
phi = list(range(1000001))
for i in range(2, 1000001):
	if i in visited:continue
	visited[i]=True
	for j in range(i, 1000001, i):
		phi[j] *= i-1
		phi[j] //= i
		visited[j]=True
res0=0
for i in range(1, n+1):
	res0+=(i*(i+1)//2)**2
	res0%=k
print(res0)
sumL=list(range(1000001))
visited = dict()
for i in range(2, n+1):
	if i in visited:continue
	visited[i]=True
	for j in range(i, n+1, i):
		ct=0
		jj=j
		while j%i==0:
			j//=i
			ct+=1
		sumL[jj]//=pow(i, ct)
		sumL[jj]*=(pow(i,2*ct+1)+1)
		sumL[jj]//=(i+1)
		visited[jj]=True
for i in range(1, n+1):
	sumL[i]=((sumL[i]+1)*i*pow(2,k-2,k)*2-i)%k
	sumL[i]+=sumL[i-1]
	sumL[i]%=k
for i in range(1, n+1):
	t = n//i
	res1 += phi[i] * (i * (t-1)*t*(2*t-1)//6 + t**2 * (1+n-i*t))
	res2 += sumL[i]
	res1%=k
	res2%=k
print((res1*res2)%k)