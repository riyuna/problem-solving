import sys
input=sys.stdin.readline
a,b,c,d=0,0,0,0
for i in range(int(input())):
	x,y=map(int,input().split())
	if not i:
		a,b,c,d=x+y,x+y,x-y,x-y
	else:
		a=max(x+y, a)
		b=min(x+y, b)
		c=max(x-y, c)
		d=min(x-y, d)

if (a==b or c==d) and (a!=b or c!=d):
	a+=1
print(a-b+c-d+4)