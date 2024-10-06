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

n,k=linput()
L=linput()
mem=[]
ct=0
d=dict()
for i in range(n):
    d[L[i]-1]=i
gap=1
while gap<n:
    for i in range(n-gap-1 ,-1, -1):
        a,b=d[i], d[i+gap]
        if a-b >= k:
            d[i], d[i+gap] = d[i+gap], d[i]
            L[a],L[b]=L[b],L[a]
            mem.append((b+1, a+1))
            ct+=1
            break
    if not ct:gap+=1
    else:gap=1
    ct=0
print(len(mem))
for a,b in mem:print(a,b)