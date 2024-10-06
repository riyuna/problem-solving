import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
	n=int(input())
	L=[[0,0] for i in range(n)]
	ct=0
	for i in list(map(int,input().split())):
		L[ct][0]=i
		ct+=1
	ct=0
	for i in list(map(int,input().split())):
		L[ct][1]=i
		ct+=1
	L.sort()
	res=0
	for a,b in L:
		res+=abs(a-b)
	mem=[0]*(n)
	for i in range(n-1, 0, -1):
		mem[i-1]=max(mem[i], min(L[i]))
	# print(L)
	# print(mem)
	k=0
	for i in range(n):
		k=max(mem[i]-max(L[i]), k)
	# print(k)
	print(res+k*2)