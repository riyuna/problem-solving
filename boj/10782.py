import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input())
k=(n+1)//2
L=list(map(int,input().split()))
tree=[10**12]*5000000
sumL=[]
ct=0
for i in range(k):ct+=L[i]
sumL.append(ct)
pt1=0
pt2=k
for i in range(n-1):
    ct-=L[pt1]
    ct+=L[pt2]
    pt1+=1
    pt2+=1
    sumL.append(ct)
    if pt2>=n:pt2-=n
L=sumL

def init(node, start, end):
    if start==end:
        i=L[start]
        tree[node]=i
        return i
    else:
        mid=(start+end)//2
        tree[node]=min(init(node*2, start, mid), init(node*2+1,mid+1,end))
        return tree[node]

def partsum(node, start, end, left, right):
    if left>end or right<start:return 10**12
    if left<=start and end<=right:return(tree[node])
    mid=(start+end)//2
    return min(partsum(node*2, start, mid, left, right),partsum(node*2+1,mid+1,end,left,right))

def update(node, start, end, index, diff):
    if index not in range(start, end+1):return
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

init(1,0,n-1)
mx=0
for i in range(n):
    pt1, pt2=i, i+k-1
    if pt2<n:res=partsum(1,0,n-1,pt1,pt2)
    else:res=min(partsum(1,0,n-1,0,pt2-n), partsum(1,0,n-1,pt1,n-1))
    mx=max(res,mx)
print(mx)