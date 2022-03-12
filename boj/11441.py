import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))
sumL=[0]
for i in L:sumL.append(sumL[-1]+i)
for i in ' '*int(input()):
	a,b=map(int,input().split())
	print(sumL[b]-sumL[a-1])