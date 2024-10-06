n,t=map(int,input().split())
L=list(range(1,2*n))+list(range(2*n,1,-1))
print(L)
print(L[(t-1)%(len(L))])