for i in range(int(input())):
    L=input().split()
    res=True
    if L[1]=='+':
        if int(L[0])+int(L[2])!=int(L[4]):res=False
    else:
        if int(L[0])-int(L[2])!=int(L[4]):res=False
    print(f"Case {i+1}: {['NO','YES'][res]}")