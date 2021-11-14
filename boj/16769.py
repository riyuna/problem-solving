L=[0,0,0]
cap=[0,0,0]
for i in range(3):
    a,b=map(int,input().split())
    L[i]=b
    cap[i]=a
for i in range(100):
    a,b=L[i%3], L[(i+1)%3]
    c=cap[(i+1)%3]
    if a+b>c:
        L[i%3], L[(i+1)%3]=(a+b)-c, c
    else: L[i%3], L[(i+1)%3]=0,a+b
for i in L:print(i)