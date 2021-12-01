import sys
input=sys.stdin.readline
n,q=map(int,input().split())
s=list(input())
s.pop(-1)
ct=0
d=dict()
for i in range(n-2):
    if s[i]=='a' and s[i+1]=='b' and s[i+2]=='c':
        d[i]=True
        ct+=1

for _ in ' '*q:
    if n<3:
        print(0)
        continue
    i,c=input().split()
    i=int(i)
    if c==s[i-1]:
        print(ct)
        continue
    for k in range(i-3, i):
        if k in d and d[k]:
            d[k]=False
            ct-=1
    if c=='a':
        if i<n-1 and s[i]=='b' and s[i+1]=='c':
            d[i-1]=True
            ct+=1
    if c=='b':
        if i>1 and i<n and s[i-2]=='a' and s[i]=='c':
            d[i-2]=True
            ct+=1
    if c=='c':
        if i>2 and i<n+1 and s[i-3]=='a' and s[i-2]=='b':
            d[i-3]=True
            ct+=1
    print(ct)
    s[i-1]=c