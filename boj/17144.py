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

r,c,t=linput()
L=[]
for i in ' '*r:L.append(linput())
machine=-1
for i in range(r):
    if L[i][0]==-1:
        machine=i
        break

def spread(L):
    newL=[[0]*c for i in range(r)]
    newL[machine][0]=-1
    newL[machine+1][0]=-1
    for i in range(r):
        for j in range(c):
            now=L[i][j]
            if now==-1:continue
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                x=i+dx
                y=j+dy
                if 0<=x<r and 0<=y<c and newL[x][y]!=-1:
                    newL[x][y]+=(L[i][j]//5)
                    now-=(L[i][j]//5)
            newL[i][j]+=now
    return newL

def wind(L):
    for i in range(machine-1, 0, -1):
        L[i][0]=L[i-1][0]
    for i in range(c-1):
        L[0][i]=L[0][i+1]
    for i in range(machine):
        L[i][-1]=L[i+1][-1]
    for i in range(c-1, 1, -1):
        L[machine][i]=L[machine][i-1]
    L[machine][1]=0
    for i in range(machine+2, r-1):
        L[i][0]=L[i+1][0]
    for i in range(c-1):
        L[-1][i]=L[-1][i+1]
    for i in range(r-1, machine+1, -1):
        L[i][-1]=L[i-1][-1]
    for i in range(c-1, 1, -1):
        L[machine+1][i]=L[machine+1][i-1]
    L[machine+1][1]=0
    return L
for _ in range(t):
    # for i in spread(L):print(*i)
    # print()
    L=wind(spread(L))
# for i in L:print(*i)
ct=2
for i in L:ct+=sum(i)
print(ct)