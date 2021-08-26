import sys
from bisect import bisect_right, bisect_left
input=sys.stdin.readline

def mergeseg(L1, L2):
    if L1==None:return L2
    if L2==None:return L1
    pt1=0
    pt2=0
    L=[]
    for i in range(len(L1)+len(L2)):
        if pt2==len(L2):
            L+=L1[pt1:]
            break
        elif pt1==len(L1):
            L+=L2[pt2:]
            break
        elif L1[pt1]>L2[pt2]:
            L.append(L2[pt2])
            pt2+=1
        else:
            L.append(L1[pt1])
            pt1+=1
    return L

def find_bigger_than(L, k):
    ct=0
    for l in L: ct+=(len(l)-bisect_right(l,k))
    return ct

def init(node, start, end):
    if start==end:
        i=[L[start]]
        tree[node]=i
        return i
    else:
        mid=(start+end)//2
        tree[node]=mergeseg(init(node*2, start, mid), init(node*2+1,mid+1,end))
        return tree[node]
            
def partsum(node, start, end, left, right):
    if left>end or right<start:return []
    if left<=start and end<=right:return [tree[node]]
    mid=(start+end)//2
    return (partsum(node*2, start, mid, left, right)+partsum(node*2+1,mid+1,end,left,right))

n,m=map(int,input().split())
L=list(map(int,input().split()))
tree=[None]*270000
init(1,0,n-1)
