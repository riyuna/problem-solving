n,k=map(int,input().split())
L=list(map(int,input().split()))
psum=[0]
for i in L:psum.append(psum[-1]+i)
