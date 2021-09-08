def manachers(s,n):
    L=[-1]*n
    r=0
    p=0
    for i in range(n):
        if i<=r:
            L[i]=min(L[2*p-i],r-i)
        else:
            L[i]=0
        while (i-L[i]-1>=0 and i+L[i]+1<n and s[i-L[i]-1]==s[i+L[i]+1]):
            L[i]+=1
    if r<i+L[i]:
        r=i+L[i]
        p=i
    return L
def find(s):
    if len(s)==0:return []
    news=['*']*(len(s)*2-1)
    for i in range(len(s)):
        news[i*2]=s[i]
    L=manachers(news,len(news))
    return L
s=input()
L=find(s)
mx=1
for i in range(len(L)):
    if i%2:
        k=L[i]
        if k%2:k+=1
        if k>mx:mx=k
    if i%2==0:
        k=L[i]
        if k%2==0:k+=1
        if k>mx:mx=k
print(mx)