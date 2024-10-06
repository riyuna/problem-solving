import sys
input=sys.stdin.readline

def op(L, k):
    n=len(L)
    # print(f'before:{L}, k={k}')
    if k>0:
        for i in range(n-k):
            L[i]^=L[i+k]
    if k<0:
        for i in range(n-1, -k-1, -1):
            L[i]^=L[i+k]
    # print(f'after:{L}')
    return L

def solve(s1, s2):
    if '1' not in s2:
        if '1' not in s1:return []
        else:return -1
    if '1' not in s1:return -1
    
    L1=list(map(int, list(s1)))
    L2=list(map(int, list(s2)))
    n=len(s1)
    st1 = -1
    st2 = -1
    for i in range(len(L1)):
        if L1[i]==1:
            st1=i
            break
    for i in range(len(L2)):
        if L2[i]==1:
            st2=i
            break
    res = []
    if st1<st2:
        for i in range(st2, n):
            if L1[i]!=L2[i]:
                L1=op(L1, st1-i)
                res.append(st1-i)
        fin1=-1
        for i in range(n-1, -1, -1):
            if L1[i]==1:
                fin1=i
                break
        for i in range(st2-1, -1, -1):
            if L1[i]!=L2[i]:
                L1=op(L1, fin1-i)
                res.append(fin1-i)
    elif st1>st2:
        L1=op(L1, st1-st2)
        res.append(st1-st2)
        for i in range(st2, n):
            if L1[i]!=L2[i]:
                L1=op(L1, st2-i)
                res.append(st2-i)
    else:
        for i in range(st2, n):
            if L1[i]!=L2[i]:
                L1=op(L1, st2-i)
                res.append(st2-i)
    return res

for i in ' '*int(input()):
    n=int(input())
    s1=input().strip()
    s2=input().strip()
    res=solve(s1,s2)
    if res==-1:print(-1)
    else:
        print(len(res))
        if not len(res):continue
        for i in res:print(i,end=' ')
        print()