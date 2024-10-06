while True:
	v,n,m=map(float,input().split())
	if v==n==m==0:break
	n=int(n)
	m=int(m)
	res=v
	if n%10000==m%10000:
		res*=3000
	elif n%1000==m%1000:
		res*=500
	elif n%100==m%100:
		res*=50
	elif (n-1)%100//4==(m-1)%100//4:res*=16
	else:res=0
	print(f"{res:.2f}")