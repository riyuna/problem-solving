x,n=map(int,input().split())
d=dict()
for i in range(n):
    a,b=map(int,input().split())
    if a not in d:d[a]=[]
    d[a].append((b, i+1))
for i in d:d[i].sort(reverse=True)
print(d)
