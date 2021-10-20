n=int(input())
M=list(map(int,input().split()))
L=[]
pt=0
while pt<n:
    L.append(M[pt])
    pt+=M[pt]
for i in L:print(i,end=' ')