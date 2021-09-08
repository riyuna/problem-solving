p=input()
fail=[0]*len(p)
mx=0
for i in range(0, len(p)):
    k=0
    for j in range(i+1, len(p)):
        while k>0 and p[j]!=p[i+k]:k=fail[k-1]
        if p[j]==p[i+k]:
            k+=1
            mx=max(mx,k)
        fail[j-i]=k

print(mx)