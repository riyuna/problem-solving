n,k=map(int,input().split())
def seq(n):
	if n==1:return [(0,1), (1,1)]
	a,b,c,d=0,1,1,n
	L=[]
	L.append((a,b))
	L.append((c,d))
	x=0
	y=0
	while y!=2.0:
		x=((b+n)//d)*c-a
		y=((b+n)//d)*d-b
		L.append((x,y))
		a,b,c,d=c,d,x,y
	return L
L=seq(n)
if k<len(L):res=L[k-1]
else:
	res1=L[len(L)*2-k-1]
	res=(res1[1]-res1[0], res1[1])
print(res[0], res[1])