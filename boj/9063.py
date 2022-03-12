import sys
input=sys.stdin.readline
n=int(input())
minx=10**6
miny=10**6
maxx=-10**6
maxy=-10**6
for i in ' '*n:
	x,y=map(int,input().split())
	minx=min(minx, x)
	miny=min(miny, y)
	maxx=max(maxx, x)
	maxy=max(maxy, y)

print((maxx-minx)*(maxy-miny))