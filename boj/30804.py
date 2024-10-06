#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
L=linput()
if n==1:
    print(1)
else:
    res=2
    pt1=0
    pt2=1
    ct= 2 if L[pt1]!=L[pt2] else 1
    d=dict()
    d[L[pt1]]=1
    if L[pt2] not in d:d[L[pt2]]=1
    else:d[L[pt2]]+=1
    while pt1<n-1:
        while ct<3 and pt2<n:
            pt2+=1
            if pt2==n:break
            else:
                if L[pt2] not in d:
                    d[L[pt2]]=1
                    ct+=1
                else:
                    d[L[pt2]]+=1
                    if d[L[pt2]]==1:ct+=1
            if ct>=3:break
            else:
                res=max(res, pt2-pt1+1)
        pt1+=1
        if pt1==pt2:
            pt2=pt1+1
            if pt1==n-1:break
            if L[pt2] not in L:
                d[L[pt2]]=1
                ct+=1
            else:d[L[pt2]]+=1
        if d[L[pt1-1]]==1:ct-=1
        d[L[pt1-1]]-=1
        
    print(res)