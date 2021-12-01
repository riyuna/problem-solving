while True:
    n=int(input())
    if n==0:break
    res=1
    for i in range(n+1, 2*n+1):res*=i
    for i in range(1, n+2):res//=i
    print(res)