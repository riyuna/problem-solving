def f(weight):
    L=[0]*26
    L[0]=weight
    pt=0
    while pt<25:
        if L[pt]<pt+3:break
        q=L[pt]//(pt+3)
        L[pt]%=(pt+3)
        L[pt+1]+=q
        pt+=1
    s=''
    for i in range(26):
        s+=chr(i+97)*L[i]
    return s

print(f('bcada'))