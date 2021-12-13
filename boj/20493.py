import sys
input=sys.stdin.readline
n,t=map(int,input().split())
dir=[1,0]
def right(dir):
    if dir==[1,0]:
        dir=[0,-1]
    elif dir==[0,-1]:
        dir=[-1,0]
    elif dir==[-1,0]:
        dir=[0,1]
    else:dir=[1,0]
    return dir

L=[]
for i in ' '*n:
    L.append(input().split())
    L[-1][0]=int(L[-1][0])

start=0
x=0
y=0
L.append([t, 'end'])
for i in range(n+1):
    d=L[i][0]-start
    xx,yy=dir
    x+=xx*d
    y+=yy*d
    if L[i][1]=='right':dir=right(dir)
    else:
        for _ in ' '*3:dir=right(dir)
    start=L[i][0]
print(x,y)