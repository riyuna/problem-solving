import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

t,k=map(int,input().split())

result = [['-']*(2**k) for i in range(2**k)]

res_que = deque()

def solve(a, b, i, j, k):
    if k==0:return
    if k==1:
        result[a][b]='c'
        return
    size = 2**(k-1)
    pos_list=[
        (i,j,i+size-1,j+size-1),
        (i+size,j,i+size,j+size-1),
        (i,j+size,i+size-1,j+size),
        (i+size,j+size,i+size,j+size),
    ]
    for x, y, xx, yy in pos_list:
        if x<=a<x+size and y<=b<y+size:
            # @is in here
            res_que.append((a,b,x,y,k-1))
        else:
            result[xx][yy]='c'
            res_que.append((xx,yy,x,y,k-1))

for _ in ' '*t:
    a,b=map(int,input().split())
    a-=1
    b-=1
    res_que.append((a,b,0,0,k))
    while len(res_que):
        a0,b0,i0,j0,k0 = res_que.popleft()
        solve(a0, b0, i0, j0, k0) 
    result[a][b]='@'
    for i in range(2**k):
        for j in range(2**k):
            print(result[i][j] if result[i][j] == 'c' or i==a and j==b else 'ab'[(i//2+j//2)%2])
            result[i][j]='-'
        print('\n')