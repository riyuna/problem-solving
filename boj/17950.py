import sys
input=sys.stdin.readline
h,x=map(int,input().split())
mod=10**9+7
res=0
for i in range(h):
    res+=int(input())*pow(x, i+1, mod)
    res%=mod
print(res)