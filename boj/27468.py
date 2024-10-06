n=int(input())
print('YES')
if n%4==0 or n%4==1:
    for i in range(n//4):
        print(i*4+1,end=' ')
        print(i*4+3,end=' ')
        print(i*4+2,end=' ')
        print(i*4+4,end=' ')
    if n%4==1:print(n)
else:
    for i in range(n//4):
        print(i*4+2,end=' ')
        print(i*4+1,end=' ')
        print(i*4+3,end=' ')
        print(i*4+4,end=' ')
    if n%4==2:
        print(n,end=' ')
        print(n-1)
    else:
        print(n-1,end=' ')
        print(n-2,end=' ')
        print(n)