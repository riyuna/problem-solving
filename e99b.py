for i in ' '*int(input()):
    x=int(input())
    k=int((2*x)**0.5)
    n=0
    for j in range(k-5,k+5):
        if j*(j-1)/2<x<=j*(j+1)/2:
            n=j
            break
    if x==n*(n+1)//2-1:print(n+1)
    else:print(n)