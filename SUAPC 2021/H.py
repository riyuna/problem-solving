n,x=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
for i in range(len(L)):
    if x==L[i]:break
if L[-1]!=x:i+=1
ct=n-i
L=L[:i]
pt1=0
pt2=len(L)-1
ct2=0
while pt1<pt2:
    if L[pt1]+L[pt2]>=x/2:
        ct2+=1
        pt1+=1
        pt2-=1
    else:
        pt1+=1

res=ct+ct2+(len(L)-ct2*2)//3
print(res)