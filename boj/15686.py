#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
from itertools import combinations
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,m=linput()
L=[]
chicken=[]
for i in range(n):
    L.append(linput())
    for j in range(n):
        if L[i][j]==2:chicken.append((i,j))
res=10**10
houses=[]
for i in range(n):
    for j in range(n):
        if L[i][j]==1:houses.append((i,j))
for tup in combinations(chicken, m):
    tot=0
    for i,j in houses:
        mn=2500
        for x,y in tup:
            mn=min(mn, abs(i-x)+abs(j-y))
        tot+=mn
    res=min(tot,res)
print(res)