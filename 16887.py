from math import ceil
grun=[]
for i in range(1000):
    L=[]
    for j in range(ceil(i**0.25), int(i**0.5)+1):
        if j==i:continue
        L.append(grun[i-j])
    pt=0
    while pt in L:
        pt+=1
    grun.append(pt)

for i in range(100):
    for j in range(10):
        print(grun[i*10+j], end=' ')
    print()