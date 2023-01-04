import sys
input = sys.stdin.readline

def naive(L):
	ans=0
	mem=10**9
	for i in range(17):
		mxm=0
		for j in range(len(L)):
			mxm=max(mxm, L[j]^i)
		if mxm<mem:
			mem=mxm
			ans=i
	return (mem, ans)

for i in range(1, 11):
	for j in range(1, 11):
		for k in range(1, 11):
			L=[i,j,k]
			print(L)
			print(naive(L))