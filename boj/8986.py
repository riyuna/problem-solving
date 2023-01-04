n=int(input())
L=list(map(int,input().split()))

def check(x):
	res=0
	for i in range(n):
		res+=abs(x*i-L[i])
	return res

lo=0
hi=L[-1]

while hi-lo>2:
	mid1=(hi+lo*2)//3
	mid2=(hi*2+lo)//3
	if check(mid1)<check(mid2):hi=mid2
	else:lo=mid1

res=10**18
for i in range(lo, hi+1):
	if check(i)<res:res=check(i)

print(res)