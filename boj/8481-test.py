with open("genzaw/gen1.out", 'r') as f:
    line=f.readline()
    L=[]
    for i in line:
        if len(L)==0 or L[-1][0]!=i:
            L.append([i, 0])
        L[-1][-1]+=1
    # print(L)
    # for i,j in L:
        # print(i,end='')
    for i,j in L:
        print(j, end=' ')
        if j<100:print()