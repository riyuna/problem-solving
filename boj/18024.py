n,m,k=map(int,input().split())
if n<=m:print(n*(n+1)//2)
else:
	r=(n-m+1)
	q=(r-1)//k+1
	res=r%k
	if res==0:res=k
	result=(n+res+m-1)*q//2
	print(result+(m-1)*m//2)