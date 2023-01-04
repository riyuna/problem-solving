import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	res=1
	for j in L:res*=j
	print((res+(n-1))*2022)