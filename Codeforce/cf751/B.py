for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    a=L.count(1)
    b=L.count(0)
    print(a*pow(2,b))