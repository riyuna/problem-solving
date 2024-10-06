import sys
input = sys.stdin.readline
n, q=map(int,input().split())
L=list(map(int,input().split()))
def checkf(L, check, k):
	andall=(1<<63)-1
	for i in L:andall&=i
	res=0
	t=1<<check
	if andall&t:
		#case 1
		for i in L:
			res+=(t-1-i%t)
		if res>=k:return True
		return False
	else:
		#case 2
		for i in L:
			if not i&t:res+=(t-i%t)
		if res<=k:return True
		return False
for _ in ' '*q:
	k=int(input())
	check=64
	res=0
	L1=L[:]
	while check>0:
		check-=1
		# print(L1,check,k)
		# print(checkf(L1, check, k))
		if checkf(L1, check, k)==False:
			continue
		t=1<<check
		res^=(t)
		andall=(1<<63)-1
		for i in L1:andall&=i
		if andall&(t)==False:
			for i in range(n):
				if L1[i]&(t)==False:
					k-=(t-L1[i]%t)
					L1[i]=t
	print(res)
