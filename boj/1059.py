l=int(input())
L=list(map(int,input().split()))
L.append(0)
L.sort()
n=int(input())
pt1=0
pt2=0
for i in range(l+1):
    if L[i]<=n:pt1=L[i]
    if L[i]>=n:
        pt2=L[i]
        break
if pt1==pt2==n:print(0)
else:
    print((n-pt1)*(pt2-n)-1)