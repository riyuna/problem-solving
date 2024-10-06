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
road=[0]*n
for i in ' '*m:
    a,b,c=linput()
    road[a-1]+=c
    road[b-1]-=c
for i in range(n-1):
    road[i+1]+=road[i]
for i in range(n-1):
    q=road[i]//L[i]
    r=road[i]%L[i]
    print(r*(q+1)**2+(L[i]-r)*(q)**2)