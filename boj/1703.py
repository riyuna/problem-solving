while True:
    L=list(map(int,input().split()))
    if L[0]==0:break
    L.pop(0)
    res=1
    for i in range(len(L)//2):
        res*=L[i*2]
        res-=L[i*2+1]
    print(res)