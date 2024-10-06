import sys
input=sys.stdin.readline
def linput():return list(map(int,input().split()))

M,D=linput()
y,m,d=linput()

d+=1
if d>D:
	d=1
	m+=1
if m>M:
	m=1
	y+=1
print(y,m,d)