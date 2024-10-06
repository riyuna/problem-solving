import sys
input=sys.stdin.readline

def solve(L,k, d, w):
    ct=0
    stack=0
    start=-1
    for i in range(len(L)):
        if stack==0 or start+d+w<L[i]:
            ct+=1
            start=L[i]
            stack=0
        stack+=1
        # print(L[i], stack, start)
        if stack==k:
            stack=0
    return ct

for i in ' '*int(input()):
    n,k,d,w=map(int,input().split())
    L=sorted(list(map(int,input().split())))
    print(solve(L,k,d,w))