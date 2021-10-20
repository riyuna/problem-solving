pList=[True]*(100000)
pList[0]=False
pList[1]=False
for i in range(2, 100000):
    if not pList[i]:continue
    for j in range(i*2, 100000, i):
        pList[j]=False

for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    s=sum(L)
    if not pList[s]:
        print(n)
        for i in range(1, n+1):print(i,end=' ')
        print()
    else:
        for i in range(n):
            if not pList[s-L[i]]:break
        print(n-1)
        for j in range(n):
            if i!=j:print(j+1,end=' ')
        print()