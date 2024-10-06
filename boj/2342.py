#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
from math import inf
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

L=linput()
L.pop(len(L)-1)
n=len(L)
dp=[[[inf]*5 for i in range(5)]for j in range(n)]
dp[0][0][L[0]]=2
dp[0][L[0]][0]=2

def f(a, b):
    if a==b:return 1
    if a*b==0:return 2
    if abs(a-b)%2:return 3
    return 4
for i in range(1, n):
    for j in range(5):
        for k in range(5):
            if j==k:continue
            dp[i][L[i]][k] = min(dp[i-1][j][k]+f(j,L[i]), dp[i][L[i]][k])
            dp[i][j][L[i]] = min(dp[i-1][j][k]+f(k,L[i]), dp[i][j][L[i]])

res=inf
for i in range(5):
    for j in range(5):
        res=min(res, dp[-1][i][j])
print(res)