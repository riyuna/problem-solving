a,b=map(int,input().split())

t = (a/(2*b))**(2/3)-1
if t<0:print(a)
else:
	res=1e18
	t=int(t)
	for i in range(max(0, t-2), t+2):
		res = min(res, b*i+a/(i+1)**0.5)
	print(res)