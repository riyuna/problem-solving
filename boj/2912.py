import random
import bisect
import sys
input = sys.stdin.readline
n,c=map(int,input().split())
L=list(map(int,input().split()))
nums=[[]for i in range(10001)]
for i in range(n):
    nums[L[i]].append(i+1)
for i in ' '*int(input()):
    a,b=map(int,input().split())
    res=0
    for i in range(50):
        k=L[random.randrange(a-1,b)]
        c=bisect.bisect_right(nums[k],b)-bisect.bisect_left(nums[k], a)
        if c>(b-a+1)/2:
            res=k
            break
    if res==0:print('no')
    else:print(f'yes {res}')