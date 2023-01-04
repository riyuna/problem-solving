res=[]
x,y,z=map(int,input().split())
def solve(x,y,z):
	L=[(x,1), (y,2), (z,3)]
	L.sort()
	xx,yy,zz=L[0][0], L[1][0], L[2][0]
	a,b,c=L[0][1], L[1][1], L[2][1]
	q=bin(yy//xx)[2:][::-1]
	for i in q:
		if i=='1':
			res.append((b,a))
			xx,yy=xx+xx,yy-xx
		else:
			res.append((c,a))
			xx,zz=xx+xx,zz-xx
	L=[(a,xx),(b,yy),(c,zz)]
	L.sort()
	return (L[0][1],L[1][1],L[2][1])

while True:
	x,y,z=solve(x,y,z)
	if x*y*z==0:break
print(len(res))
for a,b in res:print(a,b)