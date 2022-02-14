D=list(map(int,input().split()))
k=sum(D)/2
if max(D)>=k:print(-1)
else:
	print(1)
	a,b,c=D
	print(k-c, k-b, k-a)