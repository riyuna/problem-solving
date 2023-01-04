from math import gcd
xs, ys = map(int,input().split())
xe, ye, dx, dy = map(int,input().split())
dist = (xs-xe)**2+(ys-ye)**2
g=gcd(dx, dy)
dx//=g
dy//=g

while True:
	xe+=dx
	ye+=dy
	ndist = (xs-xe)**2+(ys-ye)**2
	if ndist>dist:break
	dist=ndist

print(xe-dx, ye-dy)