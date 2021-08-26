import random
for i in range(10):
    L1=[]
    L2=[]
    for i in range(3):
        L1.append(random.randint(1, 5))
        L2.append(random.randint(1, 5))

    print(L1)
    print(L2)

    res=0
    mxres=0
    for i in range(3):
        for j in range(3):
            k1=min(abs(L1[i]-L1[j]),abs(L2[i]-L2[j]))
            k2=max(abs(L1[i]-L1[j]),abs(L2[i]-L2[j]))
            print((k1,k2), end=' ')
            res+=k1
            mxres+=k2
        print()


    print(res)
    print(mxres)
    print()