import sys
from functools import cmp_to_key
input=sys.stdin.readline

class sgTree:
    def __init__(self,L):
        self.len=len(L)
        newL=[]
        for i in L:newL.extend([i,i,i,i])
        self.tree=[0]*(self.len*4)+newL
        for i in range(self.len-1, 0, -1):
            # L1=self.tree[i]
            # left=self.tree[2*i]
            # right=self.tree[2*i+1]
            #0th:lsum 1st:rsum 2nd:tot 3rd:max
            self.tree[4*i]=max([self.tree[8*i],self.tree[8*i+2]+self.tree[8*i+4]])
            self.tree[4*i+1]=max([self.tree[8*i+5],self.tree[8*i+6]+self.tree[8*i+1]])
            self.tree[4*i+2]=self.tree[8*i+2]+self.tree[8*i+6]
            self.tree[4*i+3]=max([self.tree[8*i+1]+self.tree[8*i+4],self.tree[8*i+3],self.tree[8*i+7],self.tree[4*i],self.tree[4*i+1]])
        
    def clean(self):
        self.tree=[0]*(self.len*8)

    #add d in point pt
    def update(self, pt, d):
        i=self.len+pt
        self.tree[4*i]+=d
        self.tree[4*i+1]+=d
        self.tree[4*i+2]+=d
        self.tree[4*i+3]+=d
        while i>1:
            i//=2
            #0th:lsum 1st:rsum 2nd:tot 3rd:max
            self.tree[4*i]=max([self.tree[8*i],self.tree[8*i+2]+self.tree[8*i+4]])
            self.tree[4*i+1]=max([self.tree[8*i+5],self.tree[8*i+6]+self.tree[8*i+1]])
            self.tree[4*i+2]=self.tree[8*i+2]+self.tree[8*i+6]
            self.tree[4*i+3]=max([self.tree[8*i+1]+self.tree[8*i+4],self.tree[8*i+3],self.tree[8*i+7],self.tree[4*i],self.tree[4*i+1]])
        


L=[]
dx=set()
dy=set()
L1=[]
L2=[]
for i in ' '*int(input()):
    a,b=map(int,input().split())
    L1.append((a,b))
    dx.add(a)
    dy.add(b)
for i in ' '*int(input()):
    a,b=map(int,input().split())
    L2.append((a,b))
    dx.add(a)
    dy.add(b)

c1,c2=map(int,input().split())
for x,y in L1:
    L.append([x,y,c1])
for x,y in L2:
    L.append([x,y,-c2])

n=len(L)

dx=sorted(list(dx))
dy=sorted(list(dy))
ddx=dict()
ddy=dict()
for i in range(len(dx)):
    ddx[dx[i]]=i
for i in range(len(dy)):
    ddy[dy[i]]=i

for i in range(n):
    L[i][0],L[i][1]=ddx[L[i][0]], ddy[L[i][1]]

def ptcmp(L1, L2):
    if L1[1]>L2[1]:return 1
    elif L1[1]==L2[1]:
        if L1[0]>L2[0]:return 1
        elif L1[0]==L2[0]:return 0
        else:return -1
    else:
        return -1
L=sorted(L, key=cmp_to_key(ptcmp))
numx=len(dx)
c=1
while c<numx:c*=2
segL=[0]*c
s=sgTree(segL)
ans=0

for i in range(n):
    if i and L[i][1]==L[i-1][1]:continue
    s.clean()
    for j in range(i, n):
        s.update(L[j][0], L[j][2])
        if j==n-1 or L[j][1]!=L[j+1][1]:
            ans=max(ans, s.tree[7])

print(ans)