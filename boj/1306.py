import sys
input=sys.stdin.readline

def initmax(node, start, end):
    if start==end:
        i=L[start]
        maxtree[node]=i
        return i
    else:
        mid=(start+end)//2
        maxtree[node]=max(initmax(node*2, start, mid),initmax(node*2+1,mid+1,end))
        return maxtree[node]

def partmax(node, start, end, left, right):
    if left>end or right<start:return 0
    if left<=start and end<=right:return(maxtree[node])
    mid=(start+end)//2
    return max(partmax(node*2, start, mid, left, right),partmax(node*2+1,mid+1,end,left,right))

n,m=map(int,input().split())
L=list(map(int,input().split()))
maxtree=[0]*3000000

initmax(1,0,n-1)
for i in range(n-2*m+2):
    print(partmax(1,0,n-1,i,i+2*m-2), end=' ')
print()