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
sys.setrecursionlimit(100000)
L=[]
while True:
    try:L.append(iinput())
    except:break
# print(L)
def solve(start, end):
    if start==end:
        print(L[start])
        return
    if start>end:return
    for i in range(start, end+1):
        if L[start]<L[i]:
            solve(start+1, i-1)
            solve(i, end)
            print(L[start])
            return
    solve(start+1, end)
    print(L[start])

solve(0,len(L)-1)