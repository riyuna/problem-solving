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
def solve(L):
    if len(L)<3:return True
    changed=0
    M=[]
    for i in range(len(L)-1):
        M.append(L[i+1]-L[i])
        if M[-1]==0:return False
        if len(M)>1 and (M[-1]*M[-2])<0:changed+=1
    return changed<2
print('YNEOS'[1-solve(L)::2])