import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    res=[0]*(n+1)
    M=[]
    for i in range(n):M.append((L[i], i))
    M.sort(reverse=True)
    ct=0
    for i in range(n):
        a,b=M[i]
        res[b+1]=(i//2+1) if i%2 else -(i//2+1)
        ct+=2*a*(i//2+1)
    print(ct)
    for i in res:print(i,end=' ')
    print()