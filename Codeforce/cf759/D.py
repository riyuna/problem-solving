import sys
input=sys.stdin.readline

def merge(L1, L2):
    inv=0
    pt1=0
    pt2=0
    res=[]
    for i in range(len(L1)+len(L2)):
        if len(L1)==pt1:
            res.append(L2[pt2])
            pt2+=1
        elif len(L2)==pt2:
            res.append(L1[pt1])
            pt1+=1
        else:
            if L1[pt1]>L2[pt2]:
                res.append(L2[pt2])
                inv+=len(L1)-pt1
                pt2+=1
            else:
                res.append(L1[pt1])
                pt1+=1
    return (res, inv)

def mergeSort(L1):
    if len(L1)<2:return (L1, 0)
    left=L1[:len(L1)//2]
    right=L1[len(L1)//2:]
    left, inv1=mergeSort(left)
    right, inv2=mergeSort(right)
    res, inv=merge(left, right)
    return (res, inv+inv1+inv2)
 
for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    res, inv=mergeSort(L)
    double=False
    for i in range(n-1):
        if res[i]==res[i+1]:
            double=True
            break

    if double or inv%2==0:
        print('YES')
    else:print('NO')