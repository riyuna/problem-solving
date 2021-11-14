n,m=map(int,input().split())
for i in range(n):
    for j in range(m):
        print(i*m+j+1,end='')
        if j!=m-1:print(' ',end='')
    print()