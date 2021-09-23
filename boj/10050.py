def solve(n, start):
    L=[]
    if n==3:
        L=[(2,-1),(5,2),(3,-3)]
    elif n==4:
        L=[(6,-1),(3,6),(0,3),(7,0)]
    elif n==5:
        L=[(8,-1),(3,8),(6,3),(0,6),(9,0)]
    elif n==6:
        L=[(10,-1),(7,10),(2,7),(6,2),(0,6),(11,0)]
    elif n==7:
        L=[(8,-1),(5,8),(12,5),(3,12),(9,3),(0,9),(13,0)]
    else:
        L=solve(n-4,4)
        L=[(2*n-2,-1),(3,2*n-2)]+L+[(0,2*n-5),(2*n-1,0)]
    newL=[]
    for i in range(len(L)):
        newL.append((L[i][0]+start,L[i][1]+start))
    return newL
n=int(input())
L=solve(n,0)
for a,b in L:
    print(a,end=' ')
    print('to',end=' ')
    print(b)