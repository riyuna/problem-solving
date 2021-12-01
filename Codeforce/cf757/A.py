for i in ' '*int(input()):
    n,l,r,k=map(int,input().split())
    L=list(map(int,input().split()))
    L.sort()
    ct=0
    money=0
    for a in L:
        if a>r:break
        if a<l:continue
        if money+a>k:break
        ct+=1
        money+=a
    print(ct)