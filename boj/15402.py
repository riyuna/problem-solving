n=int(input())
L=list(map(int,input().split()))
ct=0
for i in L:
    if i==1:ct+=1
res=True
if ct<n-2:res=False
elif ct==n:
    if n%3==0:res=False
    else:res=True
elif ct==n-1:
    res=True
elif n%3!=2 and 2 in L:res=True
else:res=False

print(['Lose','Win'][res])