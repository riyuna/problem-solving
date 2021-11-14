n=int(input())
d=dict()
for _ in ' ' *n:
    s1=input()
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]]=0
        d[s1[i]]+=10**(len(s1)-i-1)
L=[]
for i in d:
    L.append(d[i])
L.sort(reverse=True)
res=0
for i in range(len(L)):
    res+=(9-i)*L[i]
print(res)