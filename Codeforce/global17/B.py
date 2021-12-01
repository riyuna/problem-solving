import sys
input=sys.stdin.readline

def ignorepal(L, k):
    pt1=0
    pt2=len(L)-1
    while pt1<pt2:
        while L[pt1]==k:pt1+=1
        while L[pt2]==k:pt2-=1
        if pt1>=pt2:break
        if L[pt1]!=L[pt2]:
            return False
        pt1+=1
        pt2-=1
    return True

def solve(L):
    pt1=0
    pt2=len(L)-1
    rem1=-1
    rem2=-1
    diff=False
    while pt1<pt2:
        if L[pt1]==L[pt2]:
            pt1+=1
            pt2-=1
            continue
        rem1=L[pt1]
        rem2=L[pt2]
        break
    
    return ignorepal(L, rem1) or ignorepal(L, rem2)
    
for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    print(['NO','YES'][solve(L)])