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
L=[]
for i in ' '*n:L.append(linput())

dp=[[[0]*3 for i in range(n)]for i in range(n)]
dp[0][1][0]=1

for i in range(2, n):
    if L[0][i]==0:dp[0][i][0]=dp[0][i-1][0]
    
for i in range(1, n):
    for j in range(1, n):
        if L[i][j]==0:
            if L[i-1][j]==0 and L[i][j-1]==0:
                dp[i][j][1] = dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][1]
            dp[i][j][2]=dp[i-1][j][1]+dp[i-1][j][2]

print(sum(dp[-1][-1]))