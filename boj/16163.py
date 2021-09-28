def manacher(s):
    r=0
    p=0
    n=len(s)
    L=[0]*len(s)
    for i in range(n):
        if i<=r: L[i]=min(L[2*p-i], r-i)
        else: L[i]=0
        while L[i]+1<=i and i+L[i]+1<n and s[i-L[i]-1] == s[i+L[i]+1]:
            L[i]+=1
        if r<i+L[i]:
            r=i+L[i]
            p=i
    return L

s=input()
S=[]
S.append('#')
for i in s:
    S.append(i)
    S.append('#')
res=0
for i in manacher(S):
    res+=(i+1)//2
print(res)