import sys
input = sys.stdin.readline
n,k=map(int,input().split())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))
L.sort(reverse=True)
newL=[]
for a,b in L:
    if len(newL)==0:newL.append([a,b])
    else:
        if newL[-1][0]==a:newL[-1][1]+=b
        else:newL.append([a,b])
res=-1
ct=0
for a,b in L:
    if ct+b>k:
        res=a+1
        break
    ct+=b
if res==-1:res=1
print(res)