s=input()
L=[]
for i in ' '*int(input()):
    ss=input()
    res=True
    for i in range(len(s)):
        if s[i]==ss[i] or s[i]=='*':continue
        res=False
        break
    if res:L.append(ss)
print(len(L))
for s in L:print(s)