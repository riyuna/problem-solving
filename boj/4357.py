def solve(a,b,m):
	sqrt=int(m**0.5)+1
	d=dict()
	res=[]
	for i in range(sqrt, 0, -1):
		d[pow(a,i*sqrt,m)]=i
	
	for j in range(sqrt+1):
		k=pow(a,j,m)*b
		k%=m
		if k in d:res.append(d[k]*sqrt-j)
	
	if len(res)==0:return -1
	return min(res)

while True:
	try:
		m,a,b=map(int,input().split())
	except:
		break
	k=solve(a,b,m)
	print(k if k!=-1 else "no solution")