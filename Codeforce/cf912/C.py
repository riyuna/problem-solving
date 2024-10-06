import sys
input = sys.stdin.readline
for _ in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	M=[0]
	for i in L[::-1]:
		M.append(M[-1]+i)
	k=M.pop(-1)
	for i in M[1:]:
		if i>0:k+=i
	print(k)