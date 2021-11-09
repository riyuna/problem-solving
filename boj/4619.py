while True:
    b,n=map(int,input().split())
    if b==n==0:break
    k=int(pow(b,1/n))
    check=k
    for i in range(k-1, k+2):
        if abs(b-check**n)>abs(b-i**n):check=i
    print(check)