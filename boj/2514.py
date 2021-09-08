m=int(input())
k=int(input())
L=[]
for i in ' '*8:L.append(list(map(int,input().split())))
row=[0]*8
col=[0]*8

r=[0]*8
c=[0]*8
ans=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        L[i][j]-=m
        row[i]+=L[i][j]
        col[j]+=L[i][j]

for i in range(8):
    for j in range(8):
        k=(row[i]+col[j]-L[i][j])%2
        ans[i][j]=k
        r[i]+=k
        c[j]+=k

new=[[0]*8 for i in range(8)]
rr=[0]*8
cc=[0]*8
for i in range(8):
    for j in range(8):
        new[i][j]=r[i]+c[j]-ans[i][j]
        rr[i]+=new[i][j]
        cc[j]+=new[i][j]
minus=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        res=rr[i]+cc[j]-new[i][j]
        if (row[i]+col[j]-L[i][j]-res)%4==2:
            minus[i][j]=1

for i in range(8):
    for j in range(8):
        if ans[i][j]:
            if minus[i][j]:print('-',end=' ')
            else:print('+',end=' ')
        else:print('.',end=' ')
    print()