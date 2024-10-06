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
L=[]
for i in ' '*n:
    M=input().split()
    M[1]=int(M[1])
    M[2]=int(M[2])
    # M[0],M[1]=M[1],M[0]
    L.append(M)
L.sort(key=lambda x:x[1])
for a,b,c in L:
    s=a[c-1]
    s=s.capitalize()
    print(s,end='')
    