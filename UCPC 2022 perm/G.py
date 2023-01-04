import sys
input=sys.stdin.readline
n,m=map(int,input().split())
L=[]
for i in ' '*m:
	robot, _ , block = input().split()
	if robot=='A':robot = 1
	else:robot=0
	block=int(block)
	L.append((robot, block))

d = dict()