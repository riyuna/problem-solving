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
dp=[[0]*2001 for i in range(100)]
dpsum=[[0]*2001 for i in range(100)]

for i in range(1,n):
    for j in range(-1000, 1001):
        dp[i][j] = ((j-L[i]) in L[:i]) + dpsum[i-1][j-L[i]] if j!=L[i] else 
        dpsum[i][j]=dpsum[i-1][j]+dp[i][j]
        
for i in range(4):
    for j in range(-5,5):
        print(dp[i][j], end=' ')
    print()
print()
for i in range(4):
    for j in range(-5,5):
        print(dpsum[i][j], end=' ')
    print()
res=1
for i in dp:
    res+=sum(i)
    res%=mod
print(res)