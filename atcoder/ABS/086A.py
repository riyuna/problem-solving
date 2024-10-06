import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
a,b=linput()
if (a*b)%2:print('Odd')
else:print('Even')