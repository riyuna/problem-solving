def pi(n):
    L=[]
    newn=n
    k=2
    for k in range(2,int(n**0.5+1)):
        if n%k==0:
            L.append(k)
            while n%k==0:
                n//=k
        if n<2:break
    if n>1:L.append(n)
    for i in L:newn*=(1-1/i)
    return int(newn)
L=[1, 2]
for i in range(2, 10001):L.append(L[-1]+pi(i))
for _ in ' '*int(input()):
    print(L[int(input())])