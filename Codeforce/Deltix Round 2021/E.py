import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def plus(L1, L2):
    if L1[2]:
        val1=L1[2]+L2[1]
    elif L1[0]:
        val1=L2[1]
    else:
        val1=L2[2]

    if L1[4]:
        val2=L1[4]+L2[3]
    elif L1[2]:
        val2=L2[3]
    elif L1[0]:
        val2=L2[5]
    else:
        val2=L2[4]

    if L1[5]:
        val3=L1[5]+L2[3]
    elif L1[1]:
        val3=L2[3]
    else:
        val3=L2[5]

    return [
    L1[0]+L2[0],
    L1[1]+L2[1],
    val1,
    L1[3]+L2[3],
    val2,
    val3
    ]

class sgTree:
    def __init__(self,L):
        self.len=1
        while self.len<len(L):
            self.len*=2
        newL=[]
        for i in L:
            if i=='a':newL.append([1,0,0,0,0,0])
            elif i=='b':newL.append([0,1,0,0,0,0])
            elif i=='c':newL.append([0,0,0,1,0,0])
        newL+=[[0,0,0,0,0,0] for i in range(self.len-len(newL))]
        self.tree=[[0,0,0,0,0,0] for i in range(self.len)]+newL
        for i in range(self.len-1, 0, -1):
            self.tree[i]=plus(self.tree[2*i],self.tree[2*i+1])

    def update(self, i, val):
        i+=(self.len-1)
        self.tree[i]=val
        while i>1:
            i//=2
            self.tree[i]=plus(self.tree[2*i],self.tree[2*i+1])

n,q=map(int,input().split())
s=input().strip()
T=sgTree(s)
for _ in ' '*q:
    i,c=input().split()
    i=int(i)
    if c=='a':val=[1,0,0,0,0,0]
    elif c=='b':val=[0,1,0,0,0,0]
    else: val=[0,0,0,1,0,0]
    T.update(i, val)
    L=T.tree[1]
    print(min([L[0],L[2],L[4]]))