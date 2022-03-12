n=int(input())
L=list(map(int,input().split()))
s=sum(L)
res=0
for i in L:
	s-=i
	res+=i*s
print(res)