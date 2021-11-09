for i in ' '*int(input()):
    input()
    n=int(input())
    L=[]
    for j in ' '*n:L.append(int(input()))
    if sum(L)%n:print('NO')
    else:print('YES')