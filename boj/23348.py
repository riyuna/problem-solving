a,b,c=map(int,input().split())
ans=0
for i in ' '*int(input()):
	res=0
	for _ in ' '*3:
		x,y,z=map(int,input().split())
		res+=(a*x+b*y+c*z)
	ans=max(ans,res)
print(ans)