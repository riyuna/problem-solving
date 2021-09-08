n,m=map(int,input().split())
s=input()
m=min(m, n*25)
L=[]
for i in s:
    L.append(122-ord(i))
print(L)