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
tot=sum(L)
def check(L, k):
    flag=False
    for i in L:
        if i>=k:flag=True
        else:
            if flag:return False
    return True
def solve(L, k):
    if 0>=k>tot:return False
    L1=sorted(L)
    L2=L1[::-1]
    pL1=[0]
    pL2=[0]
    for i in L1:pL1.append(pL1[-1]+i)
    for i in L2:pL2.append(pL2[-1]+i)
    if check(pL1, k):return L1
    if check(pL2, k):return L2
    else:return False

res=solve(L, k)
if res==False:print('No')
else:
    print('Yes')
    print(*res)