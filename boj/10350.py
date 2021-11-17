n=int(input())
L=list(map(int,input().split()))
sumL=[0]
for i in L:sumL.append(sumL[-1]+i)
res=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:continue
        if (i<j and sumL[j]<sumL[i]) or (i>j and sumL[j]+sumL[n]<sumL[i]):
            k = sumL[i]-sumL[j] if i<j else sumL[i]-sumL[j]-sumL[n]
            res+=((k-1)//sumL[-1]+1)
print(res)