import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:L.append(int(input()))
mx=0
ct=0
for i in range(n-1, -1, -1):
    if L[i]>mx:
        mx=L[i]
        ct+=1
print(ct)