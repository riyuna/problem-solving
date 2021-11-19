import sys
input=sys.stdin.readline

tree=[0]*(10**6)

def init(node, start, end):
    if start==end:
        i=L[start]
        tree[node]=i
        return i
    else:
        mid=(start+end)//2
        tree[node]=init(node*2, start, mid)+init(node*2+1,mid+1,end)
        return tree[node]

def partsum(node, start, end, left, right):
    if left>end or right<start:return 0
    if left<=start and end<=right:return(tree[node])
    mid=(start+end)//2
    return partsum(node*2, start, mid, left, right)+partsum(node*2+1,mid+1,end,left,right)

def update(node, start, end, index, diff):
    if index not in range(start, end+1):return
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

n,q=map(int,input().split())
L=list(map(int,input().split()))
for i in range(n):
    if i%2:L[i]*=-1
init(1,0,n-1)
for _ in ' '*q:
    a,b,c=map(int,input().split())
    if a==1:
        print(abs(partsum(1,0,n-1,b-1,c-1)))
    else:
        k=1 if b%2 else -1
        update(1,0,n-1,b-1,k*c)