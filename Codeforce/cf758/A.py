import sys
input=sys.stdin.readline

L=[True]*(10001)
L[0]=False
L[1]=False
pL=[]
for i in range(2, 10001):
    if not L[i]:continue
    pL.append(i)
    for j in range(i*2, 10001, i):
        L[j]=False

for i in ' '*int(input()):
    n=int(input())
    for j in range(n):
        print(pL[j],end=' ')
    print()