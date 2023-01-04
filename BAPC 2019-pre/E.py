import sys
input=sys.stdin.readline
n,m=map(int,input().split())
up=[]
down=[]
for i in range(m):
	a,b=map(int,input().split())
	if a<b:up.append(i+1)
	else:down.append(i+1)
res=up if len(up)<len(down) else down
print(len(res))
for i in res:print(i)