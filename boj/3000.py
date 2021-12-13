import sys
input=sys.stdin.readline
xdict=dict()
ydict=dict()
L=[]
for i in ' '*int(input()):
    x,y=map(int,input().split())
    if x not in xdict:xdict[x]=[]
    xdict[x].append(y)
    if y not in ydict:ydict[y]=[]
    ydict[y].append(x)
    L.append([x,y])
ct=0
for x,y in L:
    ct+=(len(xdict[x])-1)*(len(ydict[y])-1)
print(ct)