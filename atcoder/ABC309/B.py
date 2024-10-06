n=int(input())
L=[]
for i in ' '*n:L.append(list(input()))
res=[]
for i in range(n):
    newlis=[]
    if i==0:
        newlis=[L[1][0]]+L[i][:n-1]
    elif i==n-1:
        newlis=L[i][1:]+[L[i-1][-1]]
    else:
        newlis=[L[i+1][0]]+L[i][1:n-1]+[L[i-1][-1]]
    res.append(newlis)
for i in res:
    for j in i:
        print(j,end='')
    print()