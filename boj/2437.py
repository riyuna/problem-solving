n=int(input())
L=sorted(list(map(int,input().split())))
cumL=[0]
for i in L:cumL.append(cumL[-1]+i)
res=0
for i in range(n):
    if L[i]>cumL[i]+1:
        res=cumL[i]+1
        break
if res==0:res=cumL[-1]+1
print(res)