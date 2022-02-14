d=dict()
def solve(a,b,c):
	if (a,b,c) in d:return d[(a,b,c)]
	if a<=0 or b<=0 or c<=0:return 1
	if a>20 or b>20 or c>20:return 1048576
	if a<b<c:
		res=solve(a,b,c-1)+solve(a,b-1,c-1)-solve(a,b-1,c)
		d[(a,b,c)]=res
		return res
	res=solve(a-1,b,c)+solve(a-1,b-1,c)+solve(a-1,b,c-1)-solve(a-1,b-1,c-1)
	d[(a,b,c)]=res
	return res

while True:
	a,b,c=map(int,input().split())
	if a==b==c==-1:break
	print(f"w({a}, {b}, {c}) = {solve(a,b,c)}")