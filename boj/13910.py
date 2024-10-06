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
from math import inf

n,m=linput()
L=linput()
L.append(0)
dp=[inf]*(n+1)
dp[0]=0
d=dict()
for i in range(m+1):
    for j in range(i):
        d[L[i]+L[j]]=True

for i in range(1, n+1):
    for j in d:
        if i-j>=0:dp[i]=min(dp[i-j]+1, dp[i])
print(dp[n] if dp[n]!=inf else -1)