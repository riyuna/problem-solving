n,x=map(int,input().split())
L=list(map(int,input().split()))
pt=0
while True:
	if L[pt]<x:
		print(pt+1)
		break
	pt+=1
	if pt==n:pt=0
	x+=1