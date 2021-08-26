n=int(input())
L=[]
for i in range(1, n+1):
    if n%i==0:L.append(i)
mi=10**10
for i in range(len(L)):
    for j in range(i, len(L)):
        ii=L[i]
        jj=L[j]
        kk=n//ii//jj
        if kk<1:continue
        if n%(ii*jj)!=0:continue
        print(ii, jj, kk)
        mi=min((ii*jj+jj*kk+kk*ii)*2,mi)
print(mi)