from math import gcd
for i in ' '*int(input()):
    n=int(input())
    L=sorted(list(map(int,input().split())))[::-1]
    M=[]
    for i in range(n-1):
        M.append(L[i]-L[i+1])
    if len(M)==0:print(L[0])
    if len(M)==1:print(M[0])
    g=0
    for i in M:g=gcd(g, i)
    print(g if g else 'INFINITY')