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

m,n=linput()
L=linput()
next_state=dict()
for i in range(1,m+1):
	next_state[i]=[]
for i in range(1, m+1):
    next_state[L[i-1]].append(i-1)
dp=[[0]*(2**m) for i in range(n+1)]
dp[0][0]=1

for j in range(n):
    for k in range(2**m):
        if dp[j][k]==0:continue
        for i in range(m):
            if not k&(1<<i):
                post=k+(1<<i)
                for s in next_state[i+1]:
                    if post&(1<<s):post-=(1<<s)
                dp[j+1][post]+=dp[j][k]
                dp[j+1][post]%=mod
# print(dp)
print(sum(dp[-1])%mod)