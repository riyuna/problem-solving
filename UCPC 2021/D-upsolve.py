import sys
input=sys.stdin.readline

class sgTree:
    def __init__(self,L):
        self.len=len(L)
        newL=[]
        for i in L:newL.append([i,0])
        self.tree=[[0,0]for i in range(self.len)]+newL
        for i in range(self.len-1, 0, -1):
            left=self.tree[2*i]
            right=self.tree[2*i+1]
            a,b,c,d=sorted(left+right)
            self.tree[i] = [d, c]

    def res(self, now, start, end, l, r):
        if end<l or r<start:return[-1000000]*2
        if l<=start and end<=r:return self.tree[now]
        mid=(start+end)//2
        L1=self.res(now*2,start,mid,l,r)
        L2=self.res(now*2+1,mid+1,end,l,r)
        a,b,c,d=sorted(L1+L2)
        return [d, c]
    
    def update(self, index, to):
        new_index = self.len+index
        self.tree[new_index][0] = to
        while new_index>1:
            new_index //= 2
            a,b,c,d=sorted(self.tree[new_index*2]+self.tree[new_index*2+1])
            self.tree[new_index]=[d,c]
        
dx=dict()
dy=dict()
ddx=dict()
ddy=dict()
Lx=[]
Ly=[]
n=int(input())
for i in ' '*n:
    x,y,v=map(int,input().split())
    if x in dx:
        dx[x]+=v
        ddx[x].append((y, v))
    else:
        dx[x]=v
        ddx[x]=[(y,v)]
    if y in dy:
        dy[y]+=v
        ddy[y].append((x, v))
    else:
        dy[y]=v
        ddy[y]=[(x,v)]


for i in range(10**6+1):
    if i in dx:
        Lx.append(dx[i])
    else:
        Lx.append(0)
    if i in dy:
        Ly.append(dy[i])
    else:
        Ly.append(0)

nx=len(Lx)
ny=len(Ly)
cx = 1
cy = 1
while cx<nx:cx*=2
while cy<ny:cy*=2

Lx+=[0]*(cx-nx)
Ly+=[0]*(cy-ny)

sx=sgTree(Lx)
sy=sgTree(Ly)

LLx=sorted(Lx)
LLy=sorted(Ly)
mx1=0
mx2=0
if len(LLx)<3:mx1=sum(Lx)
else:mx1=sum(LLx[len(LLx)-3:])
if len(LLy)<3:mx2=sum(Ly)
else:mx2=sum(LLy[len(LLy)-3:])
mx3=0
mx4=0

for x in ddx:
    for a,b in ddx[x]:
        sy.update(a, Ly[a]-b)
    mx3=max(mx3, sy.tree[1][0]+sy.tree[1][1]+dx[x])
    for a,b in ddx[x]:
        sy.update(a, Ly[a])
    
for y in ddy:
    for a,b in ddy[y]:
        sx.update(a, Lx[a]-b)
    mx4=max(mx4, sx.tree[1][0]+sx.tree[1][1]+dy[y])
    for a,b in ddy[y]:
        sx.update(a, Lx[a])

print(max([mx1, mx2, mx3, mx4]))