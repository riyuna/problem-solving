L=[[0]*1001 for i in range(1001)]
res=[]
for i in range(int(input())):
    res.append(0)
    a,b,c,d=map(int,input().split())
    for j in range(a, a+c):
        for k in range(b, b+d):
            L[j][k]=(i+1)
for i in range(len(res)):
    for j in range(1001):
        for k in range(1001):
            if L[j][k]==i+1:res[i]+=1
for i in res:print(i)