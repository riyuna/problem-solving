import sys
input = sys.stdin.readline
n,t=map(int,input().split())
L=list(map(int,input().split()))
psum = [0]
for i in range(n):
	psum.append(psum[-1]+L[i])

t%=sum(L)
for i in range(n+1):
	if psum[i] > t:
		print(i,t-psum[i-1])
		break