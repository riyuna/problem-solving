def check(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:return False
    return True
for i in ' '*int(input()):
    n,x=map(int,input().split())
    L=list(map(int,input().split()))
    ct=0
    while True:
        if check(L):break
        ct+=1
        changed=False
        for j in range(n):
            if L[j]>x:
                L[j],x=x,L[j]
                changed=True
                break
        if not changed:break
    if check(L):print(ct)
    else:print(-1)