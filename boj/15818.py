n,m=map(int,input().split())
L=list(map(int,input().split()))
res=1
for i in L:
	res*=(i%m)
	res%=m
print(res)