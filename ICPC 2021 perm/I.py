L=[]
for i in ' '*int(input()):
    b,p,q,r=map(int,input().split())
    L.append((p*q*r, p+q+r, b))
L.sort()
print(L[0][-1], L[1][-1], L[2][-1])