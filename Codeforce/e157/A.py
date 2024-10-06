import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	x,y,k=map(int,input().split())
	if x>y:print(x)
	elif x+k>=y:print(y)
	else:print(2*y-x-k)