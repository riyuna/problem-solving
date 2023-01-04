import sys
input=sys.stdin.readline
g,y,r=map(int,input().split())
t=g+y+r
n=int(input())
g1,g2=0.5,0.5

def f(g1, g2, newg1, newg2):
	if g1>g2:g1-=t
	if newg1>newg2:newg1-=t
	return (max(g1, newg1), min(g2, newg2))

for i in range(n):
	a,b=input().split()
	a=int(a)%t
	if b=='green':
		newg1, newg2=(a-g)%t, a
	elif b=='yellow':
		newg1, newg2=(a-y-g)%t, (a-g)%t
	else:
		newg1, newg2=(a-r-y-g)%t, (a-y-g)%t
	
	if (g1,g2)==(0.5,0.5):
		g1, g2=newg1, newg2
	else: g1, g2=f(g1, g2, newg1, newg2)
	print(g1, g2)

a,b=input().split()
a=int(a)%t
if b=='green':
	newg1, newg2=(a-g)%t, a
elif b=='yellow':
	newg1, newg2=(a-y-g)%t, (a-g)%t
else:
	newg1, newg2=(a-r-y-g)%t, (a-y-g)%t

if g1>g2:g1-=t
if newg1>newg2:newg1-=t
print(g1, g2, newg1, newg2)
print(max(0,((min(g2, newg2)-max(g1, newg1))/(g2-g1))))

