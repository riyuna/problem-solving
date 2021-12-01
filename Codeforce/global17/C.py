import sys
from collections import deque

input=sys.stdin.readline

def determine(L, k):
    stack=deque([])
    for a,b in L:
        if a>=k-1-len(stack) and b>=len(stack):stack.append((a,b))
    if len(stack)>=k:return True
    return False

def solve(L):
    hi=len(L)
    lo=0
    while hi>lo:
        mid=(lo+hi)//2+1
        if determine(L, mid):
            lo=mid
        else:
            hi=mid-1
    return hi

for _ in ' '*int(input()):
    n=int(input())
    L=[]
    for i in ' '*n:L.append(list(map(int,input().split())))
    print(solve(L))