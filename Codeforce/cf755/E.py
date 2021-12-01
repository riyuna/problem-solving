import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))

def solve(L):
    d=dict()
    safel=-10**20
    safeh=10**20
    ct=0
    M=[0]
    d[0]=1
    for i in range(len(L)):
        if i%2==0:
            k=M[-1]+L[i]
        else:
            k=M[-1]-L[i]
        if len(M)>1:
            a,b=M[-2],M[-1]
            safeh=min(safeh,max(a,b))
            safel=max(safel,max())