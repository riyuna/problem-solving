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

n,m=linput()
L=linput()
mem=[0]*m
psum=deque([0])
mem[0]+=1
for i in range(n):
    psum.append((psum[-1]+L[i])%m)
    mem[psum[-1]]+=1

fin=psum[-1]
res=0
for i in range(n):
    k=psum.popleft()
    mem[k]-=1
    res+=mem[k]
    psum.append((psum[0]+fin)%m)
    mem[psum[-1]]+=1

if fin==0:res-=n
print(res)