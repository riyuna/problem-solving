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
output=sys.stdout.write
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()

dp=dict()
dp[1]=[0,0]
for i in range(2, 7):
    dp[i]=[0]*(i+1)
    for j in range(1, i+1):
        dp[i][j]=pow(i, mod-2, mod)

sixth = pow(6, mod-2, mod)

todo=dict()
q=deque()
q.append(n)
todo[n]=True
while True:
    l=len(q)
    for i in range(l):
        k=q.popleft()
        k1=(k*5)//6
        
        if k1 not in todo and k1>1:
            todo[k1]=True
            q.append(k1)
        if k%6:
            k2=k1+1
            if k2 not in todo and k2>1:
                todo[k2]=True
                q.append(k2)
    if len(q)==0:break
do=[]
for i in todo:do.append(i)
do.sort()

for i in do:
    if i<7:continue
    r0=i%6
    if not r0:r0=6
    if i not in dp:dp[i]=[0]*(i+1)
    for j in range(1, i+1):
        r=j%6
        if r==0:r=6
        for k in range(1, 7):
            if k==r:continue
            dp[i][j]+=dp[(i*5)//6+int(r0<k)][(j*5)//6+int(r<k)]*sixth
        dp[i][j]%=mod

for i in range(1, n+1):print(dp[n][i])

# def solve(n):
#     if check[n]:return
#     check[n]=True
#     rr=n%6
#     if rr==0:rr=6
#     solve((n*5)//6)
#     if n%6:solve((n*5)//6+1)
#     for i in range(1, n+1):
#         if (n, i) in dp:continue
#         res=0
#         r=i%6
#         if r==0:r=6
#         for ii in range(1, 7):
#             if ii==r:continue
#             res+=dp[((n*5)//6+int(rr<ii), (i*5)//6+int(r<ii))]*sixth
#             res%=mod
#         dp[(n,i)]=res
#     return
# solve(n)
# for i in range(1, n+1):
#     print(dp[(n,i)])