n,k=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
L.sort()
print(L[k-1])