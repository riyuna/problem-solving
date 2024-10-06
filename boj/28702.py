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

L=[]
for i in ' '*3:
    L.append(input().strip())
ct=0    
for i in range(3):
    try:
        ct=int(L[i])+(3-i)
    except:
        pass
if ct%3:
    if ct%5:print(ct)
    else:print('Buzz')
else:
    if ct%5:print('Fizz')
    else:print('FizzBuzz')