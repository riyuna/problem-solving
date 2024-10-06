d=dict()
d[0]=0
def solve(n):
	if n<0:return 0
	if n in d:return d[n]
	if n<10:
		res=0
		for i in range(n+1):res+=i
		d[n]=res
		return res
	first=n
	ct=0
	res=0
	while first>9:
		first//=10
		ct+=1
	k=solve(10**ct-1)
	for i in range(first):
		res+=i*10**ct+k
	other=n-first*10**ct
	res+=(solve(other)+(other+1)*first)
	d[n]=res
	return res
for i in ' '*int(input()):
	a,b=map(int,input().split())
	print(solve(b)-solve(a-1))