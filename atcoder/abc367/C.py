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
def gen(L):
    if len(L)==0:return []
    if len(L)==1:return [[i] for i in range(1, L[0]+1)]
    LL=L[1:]
    k=L[0]
    res=[]
    for i in range(1, k+1):
        for j in gen(LL):
            res.append([i]+j)
    return res

for i in gen(L):
    if sum(i)%k==0:print(*i)