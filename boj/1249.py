mod = 1234567891
c = [[0]*27 for i in range(27)]
for i in range(27):
	for j in range(i+1):
		if i==j:c[i][j]=1
		elif j==0:c[i][j]=1
		else:
			c[i][j]=c[i-1][j-1]+c[i-1][j]
			c[i][j]%=mod

n,k=map(int,input().split())
a=[0]
for i in range(1,k+1):
	res = c[26][k]
	res*=pow(k,n,mod)
	res%=mod
	for j in range(i):
		res -= c[27+j-i][j+1]*a[i-j-1]
		res%=mod
	a.append(res)
print(sum(a)%mod)