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
L=[1,9,9]
for i in range(40):
    L.append(L[-2]*10)
def solve(n):
    if n==1:return 0
    pt=0
    while n>0:
        n-=L[pt]
        pt+=1
        if n<=0:
            pt-=1
            n+=L[pt]
            break
    now=(10**((pt-1)//2))+n-1
    if pt%2:
        return str(now)+str(now)[::-1][1:]
    else:
        return str(now)+str(now)[::-1]
print(solve(n))