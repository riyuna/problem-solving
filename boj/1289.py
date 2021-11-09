import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
d=dict()
mod=10**9+7

for i in ' '*(n-1):
    a,b,w=map(int,input().split())
    if a not in d:d[a]=[]
    if b not in d:d[b]=[]
    d[a].append([b,w])
    d[b].append([a,w])

res=0

def solve(now, prev):
    global res
    rem=1
    for i in range(len(d[now])):
        next, dist=d[now][i]
        if next==prev:continue

        k=solve(next,now)*dist
        ans=(k*rem)%mod
        res+=ans
        res%=mod
        rem+=k
        rem%=mod
    return rem

solve(1,0)
print(res)