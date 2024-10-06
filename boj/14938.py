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
n,m,r=linput()
mem=linput()
from math import inf
d=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:d[i][j]=inf

for i in ' '*r:
    a,b,c=linput()
    d[a-1][b-1]=min(d[a-1][b-1],c)
    d[b-1][a-1]=min(d[b-1][a-1],c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][j], d[i][k]+d[k][j])
res=0
for i in range(n):
    ct=0
    for j in range(n):
        if d[i][j]<=m:ct+=mem[j]
    res=max(res,ct)
print(res)
