import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
from atcoder.convolution import convolution_int

n,m=linput()
L1=linput()
L2=linput()

c=convolution_int(L1, L2)
for i in c:print(i%mod,end = ' ')