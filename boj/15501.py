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
L1=linput()
L2=linput()

def solve(L1, L2):
    k=L1[0]
    pt=-1
    for i in range(len(L2)):
        if L2[i]==k:
            pt=i
            break
    n=len(L1)
    flag=True
    for i in range(n):
        if L1[i]!=L2[(pt+i)%n]:
            flag=False
            break
    if flag:return True
    flag=True
    for i in range(n):
        if L1[i]!=L2[(pt-i)%n]:
            flag=False
            break
    return flag

print(['bad','good'][solve(L1,L2)], 'puzzle')