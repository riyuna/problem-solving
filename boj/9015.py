import sys
input=sys.stdin.readline
def solve(L):
	mem = dict()
	mxm = 0
	for i in L:mem[tuple(i)]=True
	for i in range(len(L)):
		for j in range(i):
			pt1 = L[i]
			pt2 = L[j]
			midx = (pt1[0]+pt2[0])/2
			midy = (pt1[1]+pt2[1])/2
			dx = pt2[0]-midx
			dy = pt2[1]-midy
			pt3 = (midx-dy, midy+dx)
			pt4 = (midx+dy, midy-dx)
			if pt3 in mem and pt4 in mem:
				mxm = max((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2, mxm)
	return mxm
for i in ' '*int(input()):
	t=int(input())
	L=[]
	for _ in ' '*t:
		a,b=map(int,input().split())
		L.append([a,b])
	res=solve(L)
	if res%2:print(res/2)
	else:print(res//2)